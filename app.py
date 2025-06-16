import streamlit as st
import os
from dotenv import load_dotenv
from planner import planner, tool_agent, reflector
import time

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Agentic Workflow Task Planner",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state
if 'state' not in st.session_state:
    st.session_state.state = None

# Title and description
st.title("🎯 Agentic Workflow Task Planner")

# User input section
col1, col2 = st.columns([2, 1])
with col1:
    query = st.text_area("Enter your task or query:", height=100, placeholder="e.g., write a report about AI developments and analyze its impact on society")
    if st.button("Plan and Execute"):
        # Reset state
        st.session_state.state = None
        
        # Initialize state with query
        state = {'query': query}
        
        # Plan tasks
        with st.spinner("Planning tasks..."):
            state = planner(state)
            
        # Update session state
        st.session_state.state = state
        
        # Process each task
        for i in range(len(state['tasks'])):
            with st.spinner(f"Executing Task {i+1} of {len(state['tasks'])}"):
                # Solve task
                state = tool_agent(state)
                
                # Get reflection
                if i < len(state['tasks']) - 1:  # Don't reflect on last task
                    state = reflector(state)
                    
                # Update session state
                st.session_state.state = state
                
                # Add a small delay for better UX
                time.sleep(1)

# Display results if available
if st.session_state.state:
    state = st.session_state.state
    
    # Display planned tasks
    st.header("Planned Tasks")
    for i, task in enumerate(state['tasks']):
        st.write(f"**Task {i+1}:** {task}")
    
    # Display results and feedback
    st.header("Execution Results")
    for i in range(len(state['results'])):
        with st.expander(f"Task {i+1} Result"):
            st.write("**Task:**", state['tasks'][i])
            st.write("**Result:**", state['results'][i])
            
            # Show reflection if available
            if i < len(state['results']) - 1:
                with st.expander("Feedback"):
                    try:
                        # Get feedback from results
                        feedback = state['results'][i+1].split("Feedback Analysis:")[1]
                        st.write(feedback)
                    except IndexError:
                        pass

    # Final summary
    st.header("Final Summary")
    st.write("All tasks have been completed!")
    st.write("**Total Tasks Completed:**", len(state['results']))
