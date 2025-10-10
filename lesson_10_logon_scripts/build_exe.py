import PyInstaller.__main__
import shutil
import os


def run_installer():
    """
    https://pyinstaller.org/en/stable/usage.html

    This function shows how pyinstaller can be used to help obfuscate & distribute nasty software.
    1. take a file with a hidden agenda (e.g "./script.py")
    2. creating an exe with it
    3. remove any post-generated folders + files
    """
    filename = "malicious.py"
    exename = "beningn.exe"
    icon = "bing.ico"
    pwd = os.getcwd()

    if os.path.isfile(exename):
        os.remove(exename)

    print("creating exe")

    PyInstaller.__main__.run(
        [
            filename,
            "--onefile",
            "--clean",
            "--log-level=ERROR",
            "--name=" + exename,
            "--icon=" + icon,
        ]
    )
    # below command fails in Windows VM: "PermissionError: [WinError 5] Access is denied: 'Z:\\dist\\beningn.exe' -> 'Z:\\'"
    shutil.copy(os.path.join(pwd, "dist", exename), pwd)

    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")
    os.remove(exename + ".spec")


run_installer()
