import os, subprocess

def run_python_file(working_directory, file_path):
    abs_w_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_w_dir, file_path))

    if not abs_path.startswith(abs_w_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", abs_path], capture_output=True, text=True, cwd=abs_w_dir, timeout=30)
    except subprocess.TimeoutExpired as e:
        return f"Process timed out: {e}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    output = []
    if result.stdout:
        output.append(f"STDOUT: {result.stdout}")
    if result.stderr:
        output.append(f"STDERR: {result.stderr}")
    if result.returncode != 0:
        output.append(f"Process exited with code {result.returncode}")

    if not output:
        return "No output produced."
    else:
        return "\n".join(output)