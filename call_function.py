from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python import schema_run_python_file, run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

def call_function(function_call_part, verbose=False):
    working_directory = "./calculator"

    try:
        func_name = function_call_part.name
        func_args = function_call_part.args
    except AttributeError:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name="unknown",
                response={"error": f"Invalid argument sent to call_function: {function_call_part}"},
            )
        ],
    )

    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    else:
        print(f" - Calling function: {func_name}")

    function_names = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if func_name not in function_names:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    
    func_call_result = function_names[func_name](working_directory, **dict(func_args))
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"result": func_call_result},
            )
        ],
    )