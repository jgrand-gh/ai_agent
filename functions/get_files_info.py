import os

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

if __name__ == "__main__":
    get_files_info("calculator")