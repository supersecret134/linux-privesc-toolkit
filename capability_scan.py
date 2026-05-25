import subprocess

def scan_capabilities():
    print("\n[+] SCANNING LINUX CAPABILITIES\n")

    try:
        output = subprocess.check_output(
            "getcap -r / 2>/dev/null",
            shell=True,
            text=True
        )

        if output:
            print(output)
        else:
            print("No capabilities found")

    except Exception as e:
        print(f"Error: {e}")
