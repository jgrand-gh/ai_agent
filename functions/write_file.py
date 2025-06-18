import os

def write_file(working_directory, file_path, content):
    abs_w_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_w_dir, file_path))

    if not abs_path.startswith(abs_w_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.isfile(abs_path):
            return f"Error: {file_path} is not a file"
        if not os.path.exists(os.path.dirname(abs_path)):
            os.makedirs(os.path.dirname(abs_path))
        with open(abs_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'