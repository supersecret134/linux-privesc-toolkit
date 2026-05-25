import os
from findings import print_finding
import subprocess

dangerous_bins = [
    "find", "vim", "nmap", "bash",
    "perl", "python", "awk"
]

def scan_suid():

    print("\n[+] SCANNING SUID BINARIES\n")

    directories = [
        "/bin",
        "/usr/bin",
        "/usr/local/bin",
        "/sbin",
        "/usr/sbin"
    ]

    for directory in directories:

        print(f"\n[+] Checking: {directory}\n")

        command = f"find {directory} -perm -4000 2>/dev/null"

        result = subprocess.getoutput(command)

        binaries = result.split("\n")

        for binary in binaries:

            if binary.strip() == "":
                continue

            print(binary)

            for risky in dangerous_bins:

                if risky in binary:
                    print(f"[HIGH RISK] {binary}")
