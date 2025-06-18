import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    if not directory:
        directory = "."

    abs_w_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_w_dir, directory))

    if not abs_path.startswith(abs_w_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    output_list = []

    try:
        for file in os.listdir(abs_path):
            fpath = os.path.join(abs_path, file)
            output_list.append(f"- {file}: file_size={os.path.getsize(fpath)} bytes, is_dir={os.path.isdir(fpath)}")
    except Exception as e:
        return f"Error generating output: {e}"

    return "\n".join(output_list)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)