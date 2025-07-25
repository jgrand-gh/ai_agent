from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test_get_files_info():
    function_name = "get_files_info"

    working_dir, file_path = "calculator", "."
    result = get_files_info(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}':")
    print(result + "\n")

    working_dir, file_path = "calculator", "pkg"
    result = get_files_info(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}':")
    print(result + "\n")

    working_dir, file_path = "calculator", "/bin"
    result = get_files_info(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}':")
    print(result + "\n")

    working_dir, file_path = "calculator", "../"
    result = get_files_info(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}':")
    print(result + "\n")

def test_get_file_content():
    function_name = "get_file_content"

    working_dir, file_path = "calculator", "main.py"
    result = get_file_content(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "pkg/calculator.py"
    result = get_file_content(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "/bin/cat"
    result = get_file_content(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "lorem.txt"
    result = get_file_content(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

def test_write_file():
    function_name = "write_file"

    working_dir, file_path, content = "calculator", "lorem.txt", "wait, this isn't lorem ipsum"
    result = write_file(working_dir, file_path, content)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}' and '{content}'")
    print(result + "\n")

    working_dir, file_path, content = "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    result = write_file(working_dir, file_path, content)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}' and '{content}'")
    print(result + "\n")

    working_dir, file_path, content = "calculator", "/tmp/temp.txt", "this should not be allowed"
    result = write_file(working_dir, file_path, content)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}' and '{content}'")
    print(result + "\n")

def test_run_python_file():
    function_name = "run_python_file"

    working_dir, file_path = "calculator", "main.py"
    result = run_python_file(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "main.py"
    result = run_python_file(working_dir, file_path, "10 + 10")
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "tests.py"
    result = run_python_file(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "../main.py"
    result = run_python_file(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

    working_dir, file_path = "calculator", "nonexistent.py"
    result = run_python_file(working_dir, file_path)
    print(f"Testing '{function_name}' for '{working_dir}' and '{file_path}'")
    print(result + "\n")

if __name__ == "__main__":
    test_run_python_file()