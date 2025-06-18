import os

def get_file_content(working_directory, file_path):
    abs_w_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_w_dir, file_path))

    if not abs_path.startswith(abs_w_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000

    try:
        with open(abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error reading file: {e}"

    return file_content_string