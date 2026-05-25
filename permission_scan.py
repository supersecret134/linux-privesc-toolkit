import subprocess

def scan_permissions():

    print("\n[+] SCANNING WEAK PERMISSIONS\n")

    directories = [
        "/tmp",
        "/var",
        "/home",
        "/etc"
    ]

    for directory in directories:

        print(f"\n[+] Checking: {directory}\n")

        command = (
            f"find {directory} "
            "-type f "
            "-perm -0002 "
            "2>/dev/null "
            "| head -20"
        )

        result = subprocess.getoutput(command)

        files = result.split("\n")

        for file in files:

            if file.strip() == "":
                continue

            print(file)
