import os, shutil, winreg

def add_exe_to_logon_script():
    """
    Supported on Windows only.

    This script adds the generated 'beningn.exe' application to the UserInitMprLogonScript registry. 

    1. run `python logon_script.py` 
    2. view Windows Registry -> HKEY_CURRENT_USER -> Environment (refresh if needed)
    3. new entry added "UserInitMprLogonScript" 
    4. logout + login to see the script run on logon
    """

    file_dir = os.path.join(os.getcwd(), "Temp")
    file_name = "beningn.exe"
    file_path = os.path.join(file_dir, file_name)

    if os.path.isfile(file_path):
        os.remove(file_path)

    os.system("python build_exe.py")

    shutil.move(file_name, file_dir)

    reg_hive = winreg.HKEY_CURRENT_USER
    reg_path = "Environment"

    reg = winreg.ConnectRegistry(None, reg_hive)
    key = winreg.OpenKey(reg, reg_path, 0, access=winreg.KEY_WRITE)
    winreg.SetValueEx(key, "UserInitMprLogonScript", 0, winreg.REG_SZ, file_path)


add_exe_to_logon_script()