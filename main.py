import os
from dotenv import load_dotenv
from planner import planner, tool_agent, reflector

def main():
    # Load environment variables
    load_dotenv()
    
    # Get OpenAI API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    os.environ["OPENAI_API_KEY"] = api_key
    
    print("Welcome to the Agentic Workflow System!")
    print("Please enter your query:")
    
    # Get user input
    query = input("Query: ")
    
    # Initialize state with the query
    state = {'query': query}
    
    # Plan the tasks
    state = planner(state)
    print("\nTasks Planned:")
    print("-" * 50)
    for i, task in enumerate(state['tasks']):
        print(f"Task {i+1}: {task}")
    print("-" * 50)
    
    # Process each task
    while state['current'] < len(state['tasks']):
        print(f"\nProcessing Task {state['current']+1} of {len(state['tasks'])}:")
        print("-" * 50)
        
        # Solve the task
        state = tool_agent(state)
        print(f"\nTask {state['current']}: {state['tasks'][state['current']-1]}")
        print("Result:")
        print("-" * 50)
        print(state['results'][-1])
        print("-" * 50)
        
        # Get reflection
        if state['current'] < len(state['tasks']):  # Don't reflect on last task
            state = reflector(state)
            
    # Print final summary
    print("\nWorkflow Complete!")
    print("Final Results:")
    print("-" * 50)
    for i, result in enumerate(state['results']):
        print(f"\nTask {i+1} Result:")
        print("-" * 50)
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    main()
