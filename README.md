# Agentic Workflow Task Planner

An intelligent task planning and execution system that breaks down complex tasks into manageable sub-tasks and solves them using AI.

## Key Features

- **Planner**: Breaks down complex tasks into 3-5 manageable sub-tasks using natural language processing
- **Tool Agent**: Uses OpenAI's GPT to solve each sub-task intelligently
- **Reflector**: Provides constructive feedback on task execution results

## Technologies Used

- Python
- LangChain
- OpenAI API

## Folder Structure

```
agentic_workflow_task_planner/
├── .env              # Environment variables (DO NOT share publicly)
├── main.py           # Main application entry point
├── planner.py        # Core task planning and execution logic
├── test_planner.py   # Test cases for the planner
├── requirements.txt  # Project dependencies
├── .gitignore        # Git ignore rules
└── README.md        # Project documentation
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd agentic_workflow_task_planner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env` file and replace `sk-your-api-key-here` with your actual OpenAI API key
   - **Important**: Never share your `.env` file publicly

## Running the Application

1. Ensure your `.env` file is properly configured
2. Run the main application:
```bash
python main.py
```

The application will:
1. Prompt you for a query
2. Break down the query into tasks
3. Solve each task using AI
4. Provide feedback on results
5. Display final output

## Sample Usage

Input:
```
Query: write a report about AI developments and analyze its impact on society
```

Output:
```
Tasks Planned:
----------------------------------------
Task 1: write a report about AI developments
Task 2: analyze its impact on society
----------------------------------------

Task 1 Result:
----------------------------------------
[Generated report about AI developments]
----------------------------------------

Task 2 Result:
----------------------------------------
[Analysis of AI's impact on society]
----------------------------------------

Final Results:
----------------------------------------
[Combined output of all tasks]
----------------------------------------
```

## Security Note

- NEVER share your `.env` file containing API keys
- Keep your OpenAI API key secure
- Add `.env` to your `.gitignore` (already included)

## License

This project is licensed under the MIT License - see the LICENSE file for details
