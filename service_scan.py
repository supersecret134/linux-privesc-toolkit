import subprocess

def scan_services():
    print("\n[+] SYSTEMD SERVICE ANALYSIS\n")

    services = subprocess.getoutput(
        "systemctl list-units --type=service --state=running"
    )

    print(services)
