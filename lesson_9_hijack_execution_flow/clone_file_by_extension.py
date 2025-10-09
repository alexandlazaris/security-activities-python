import os
import shutil


def clone_file_by_extension(target_extension, print_contents=False):
    """
    Supported only on Mac + Linux. 
    
    Pass in a file extension (e.g .zshrc) which commonly exists in the Home or '~' directory. 
    
    Clone this file and read its contents, enabling the user to overwrite existing PATH or alias configurations with malicious intent.
    """
    home_directory = os.path.expanduser("~")
    os.chdir(home_directory)
    list = os.listdir()
    list.sort()
    for index in list:
        if index == target_extension:
            match = index
    if os.path.isfile(f"{match}-copy"):
        os.remove(f"{match}-copy")
        print(f"{match} exists, removing now.")
    else:
        print(f"{match} does not exist.")

    print(f"creating new copy of target {target_extension}")

    try:
        copied_file = shutil.copy(match, f"{match}-copy")
        if os.path.isfile(copied_file):
            print(f"{match} has been successfully copied to {copied_file}")
    except Exception as e:
        print(f"Error when copying target file.\n -> {e}")

    print(f"full path to copied file is {os.path.abspath(copied_file)}")
    if(print_contents):
        try:
            print(
                f"------------------------READING CONTENTS OF {copied_file}------------------------\n"
            )
            with open(copied_file, "r") as file:
                file_content = file.read()  # Reads entire content as a single string
                # Or:
                # file_content = file.readlines() # Reads all lines into a list of strings
            print(file_content)
        except FileNotFoundError:
            print(f"file {copied_file} not found")

clone_file_by_extension(".zshrc")
