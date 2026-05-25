from system_info import get_system_info
from suid_scan import scan_suid
from permission_scan import scan_permissions
from cron_scan import scan_cron
from sudo_scan import scan_sudo
from service_scan import scan_services
from kernel_scan import scan_kernel
from capability_scan import scan_capabilities
from report_generator import save_report

def main():

    print("""
    =====================================
    Linux Privilege Escalation Toolkit
    =====================================
    """)

    # Run all scans
    get_system_info()
    scan_suid()
    scan_permissions()
    scan_cron()
    scan_sudo()
    scan_services()
    scan_kernel()
    scan_capabilities()

    # Summary Section
    print("\n=====================================")
    print("SCAN SUMMARY")
    print("=====================================")

    print("System Information Scan: Complete")
    print("SUID Binary Scan: Complete")
    print("Weak Permission Scan: Complete")
    print("Cron Job Scan: Complete")
    print("Sudo Privilege Scan: Complete")
    print("Service Scan: Complete")
    print("Kernel Scan: Complete")
    print("Capability Scan: Complete")

    # Report Content
    report = """
Linux Privilege Escalation Toolkit Report

Scans Completed:
- System Information Scan
- SUID Binary Scan
- Weak Permission Scan
- Cron Job Scan
- Sudo Privilege Scan
- Service Scan
- Kernel Scan
- Capability Scan

Status:
Scan completed successfully.
"""

    # Save report
    save_report(report)

if __name__ == "__main__":
    main()
