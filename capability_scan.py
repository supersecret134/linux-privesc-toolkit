import subprocess

def scan_capabilities():
    print("\n[+] SCANNING LINUX CAPABILITIES\n")

    directories = [
        "/usr/bin",
        "/usr/sbin",
        "/bin",
        "/sbin"
    ]

    found = False

    for directory in directories:
        try:
            print(f"[+] Checking: {directory}\n")

            output = subprocess.check_output(
                f"getcap -r {directory} 2>/dev/null",
                shell=True,
                text=True
            )

            if output.strip():
                print(output)
                found = True

        except Exception:
            pass

    if not found:
        print("No capabilities found")
