import subprocess

def scan_sudo():
    print("\n[+] SUDO PRIVILEGES\n")

    result = subprocess.getoutput("sudo -l")
    print(result)

    if "NOPASSWD" in result:
        print("[HIGH RISK] NOPASSWD DETECTED")
