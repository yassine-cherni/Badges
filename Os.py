import os

def list_files_and_directories(path="."):
    try:
        # Get the list of items in the specified directory
        items = os.listdir(path)

        print(f"Contents of {os.path.abspath(path)}:")
        for item in items:
            item_path = os.path.join(path, item)

            if os.path.isfile(item_path):
                print(f"File: {item}")
            elif os.path.isdir(item_path):
                print(f"Directory: {item}")
            else:
                print(f"Other: {item}")

    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")

# Call the function to list files and directories in the current directory
list_files_and_directories()
