# AI Coding Agent

This project is an AI-powered coding assistant that can list files, read file contents, execute Python scripts, and write files within a secure working directory. It includes a calculator application as an example target for code operations.

## Features

- List files and directories within a working directory
- Read file contents securely
- Execute Python files with optional arguments
- Write or overwrite files (with directory constraints)
- Calculator application for evaluating mathematical expressions (can be used to test AI Agent capabilities)

## Requirements

- Python 3.12 or newer
- `google-genai` (see [requirements.txt](requirements.txt))
- `python-dotenv` for environment variable management

## Getting Started

1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up your Gemini API key:**
   - Create a `.env` file with:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
4. **Run the AI assistant:**
   ```sh
   python main.py "your prompt here"
   ```
   Add `--verbose` for detailed output.

> **Caution:**  
> While the AI Agent is designed to operate within a secure working directory, it is possible to request or generate code that, if executed, could interact with files or resources outside this directory. Always review generated scripts and exercise caution when running code produced by the agent, especially if it was created dynamically or based on user prompts.

## Calculator Application

The calculator is located in [`calculator/`](calculator/README.md) and supports basic arithmetic expressions. Run it directly with:
```sh
python calculator/main.py "3 + 5"
```

## Running Tests

Function tests for the AI agent are in [`tests.py`](tests.py):
```sh
python tests.py
```
Unit tests for the calculator are in [`calculator/tests.py`](calculator/tests.py). Run them with:
```sh
python calculator/tests.py
```

## Project Structure

- `main.py` — Entry point for the AI assistant
- `call_function.py` — Function dispatch logic for agent operations
- `prompts.py` — System prompt for the AI agent
- `functions/` — Secure file and code operation functions
- `calculator/` — Calculator application and its modules
- `tests.py` — Function-level tests for agent operations

## Example Workflow: Debugging with the AI Agent

Suppose you introduce a bug into the calculator app by editing `calculator/main.py` and changing the operator from `+` to `-`:

```python
# ...existing code...
result = eval(expression.replace("+", "-"))
print(result)
# ...existing code...
```

Now, running the calculator:

```sh
python calculator/main.py "3 + 5"
```

will output `-2` instead of `8`.

You can then ask the AI Agent to help fix the bug:

```sh
python main.py "The calculator returns -2 for '3 + 5'. How do I fix this?"
```

The agent will analyze the code and suggest a correction to restore the intended behavior.

## License

This project is for educational purposes as part of a Boot.dev learning module.
