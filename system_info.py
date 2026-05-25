import os
import platform
import subprocess
import getpass

def get_system_info():

    print("\n[+] SYSTEM INFORMATION\n")

    username = getpass.getuser()
    print(f"User: {username}")

    groups = subprocess.getoutput("groups")
    print(f"Groups: {groups}")

    kernel = platform.release()
    print(f"Kernel Version: {kernel}")

    os_info = subprocess.getoutput(
        "cat /etc/os-release | grep PRETTY_NAME"
    )
    print(os_info)

    if os.geteuid() == 0:
        print("[!] Running as ROOT")
    else:
        print("[+] Running as Standard User")
