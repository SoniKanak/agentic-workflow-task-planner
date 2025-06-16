from planner import planner, tool_agent, reflector
import os

def test_tool_agent():
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "your_api_key_here"
    
    # Create a test state
    state = {
        'tasks': ['write a short story about a robot', 'analyze the story for themes'],
        'results': [],
        'current': 0
    }
    
    print("\nTesting tool_agent:")
    print("\nInitial state:")
    print(state)
    
    # Solve first task
    state = tool_agent(state)
    print("\nAfter solving first task:")
    print(state)
    
    # Solve second task
    state = tool_agent(state)
    print("\nAfter solving second task:")
    print(state)

def test_reflector():
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "your_api_key_here"
    
    # Create a test state with some results
    state = {
        'tasks': ['write a short story about a robot', 'analyze the story for themes'],
        'results': ['Once upon a time, in a world...', 'The story explores themes of...'],
        'current': 2
    }
    
    print("\nTesting reflector:")
    print("\nInitial state:")
    print(state)
    
    # Get feedback on the results
    state = reflector(state)
    print("\nAfter reflection:")
    print(state)

def test_planner():
    # Test case 1: Multiple delimiters
    state1 = {'query': 'write a report and analyze the data; create a presentation'}
    result1 = planner(state1)
    print("\nTest 1:")
    print("Input:", state1['query'])
    print("Output:", result1)
    
    # Test case 2: Single task
    state2 = {'query': 'write a long report'}
    result2 = planner(state2)
    print("\nTest 2:")
    print("Input:", state2['query'])
    print("Output:", result2)
    
    # Test case 3: Too many tasks
    state3 = {'query': 'do this, do that; do another thing, do one more thing, and finally do something else'}
    result3 = planner(state3)
    print("\nTest 3:")
    print("Input:", state3['query'])
    print("Output:", result3)

if __name__ == "__main__":
    test_planner()
