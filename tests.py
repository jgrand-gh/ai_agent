from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test_get_files_info():
    function_name = "get_files_info"
    first_arg = "calculator"
    second_arg = ""

    second_arg = "."
    result = get_files_info(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}':")
    print(result + "\n")

    second_arg = "pkg"
    result = get_files_info(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}':")
    print(result + "\n")

    second_arg = "/bin"
    result = get_files_info(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}':")
    print(result + "\n")

    second_arg = "../"
    result = get_files_info(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}':")
    print(result + "\n")

def test_get_file_content():
    function_name = "get_file_content"
    first_arg = "calculator"
    second_arg = ""

    second_arg = "main.py"
    result = get_file_content(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}'")
    print(result + "\n")

    second_arg = "pkg/calculator.py"
    result = get_file_content(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}'")
    print(result + "\n")

    second_arg = "/bin/cat"
    result = get_file_content(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}'")
    print(result + "\n")

    second_arg = "lorem.txt"
    result = get_file_content(first_arg, second_arg)
    print(f"Testing '{function_name}' for '{first_arg}' and '{second_arg}'")
    print(result + "\n")

if __name__ == "__main__":
    test_get_file_content()