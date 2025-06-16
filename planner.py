import re
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def planner(state):
    """
    Breaks down a query into sub-tasks using common delimiters.

    Args:
        state (dict): A dictionary containing a 'query' key with the task description

    Returns:
        dict: A dictionary containing:
            - tasks: List of sub-tasks
            - results: Empty list for storing results
            - current: Index of the current task (starts at 0)
    """
    if 'query' not in state:
        raise ValueError("State dictionary must contain a 'query' key")
    
    query = state['query']
    delimiters = ['and', ',', ';', 'then']
    pattern = '|'.join(map(re.escape, delimiters))
    subtasks = re.split(f'\s*({pattern})\s*', query)
    subtasks = [task.strip() for task in subtasks if task.strip() and task.lower() not in delimiters]
    
    if len(subtasks) < 3:
        if subtasks:
            longest_task = max(subtasks, key=len)
            idx = subtasks.index(longest_task)
            split_idx = len(longest_task) // 2
            subtasks[idx:idx+1] = [longest_task[:split_idx].strip(), longest_task[split_idx:].strip()]
    elif len(subtasks) > 5:
        while len(subtasks) > 5:
            shortest_task = min(subtasks, key=len)
            idx = subtasks.index(shortest_task)
            if idx < len(subtasks) - 1:
                subtasks[idx] = f"{subtasks[idx]} and {subtasks[idx+1]}"
                del subtasks[idx+1]
    
    return {
        'tasks': subtasks,
        'results': [],
        'current': 0
    }

def tool_agent(state):
    """
    Solves the current task using ChatOpenAI and updates the state with results.

    Args:
        state (dict): A dictionary containing:
            - tasks: List of tasks
            - results: List of results
            - current: Index of the current task

    Returns:
        dict: Updated state with the new result appended
    """
    required_keys = ['tasks', 'results', 'current']
    if not all(key in state for key in required_keys):
        raise ValueError("State dictionary must contain 'tasks', 'results', and 'current' keys")

    current_task = state['tasks'][state['current']]

    try:
        chat = ChatOpenAI(temperature=0.7)
        messages = [HumanMessage(content=f"Please solve this task: {current_task}")]
        response = chat(messages)

        state['results'].append(response.content)
        state['current'] += 1
        return state

    except Exception as e:
        state['results'].append(f"Error solving task: {str(e)}")
        return state

def reflector(state):
    """
    Uses ChatOpenAI to reflect on the last result of the current task.

    Args:
        state (dict): A dictionary containing:
            - tasks: List of tasks
            - results: List of results
            - current: Index of the current task

    Returns:
        dict: Updated state (unchanged except for printed feedback)
    """
    try:
        task = state['tasks'][state['current'] - 1]
        result = state['results'][-1]

        chat = ChatOpenAI(temperature=0.3)
        messages = [HumanMessage(content=f"Task: {task}\nResult: {result}\nPlease review the result and provide feedback.")]
        feedback = chat(messages)

        print("\nReflection Feedback:")
        print(feedback.content)

    except Exception as e:
        print("Error in reflection:", str(e))

    return state