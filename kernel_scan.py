import platform
from findings import print_finding

def scan_kernel():
    kernel = platform.release()

    print("\n[+] KERNEL ANALYSIS\n")
    print(f"Kernel: {kernel}")

    if "5." in kernel:
        print_finding("MEDIUM", "Possible Dirty Pipe vulnerability")

    if "4." in kernel:
        print_finding("HIGH", "Possible Dirty COW vulnerability")
