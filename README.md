# Linux Privilege Escalation Automation Toolkit

## Project Overview

The Linux Privilege Escalation Automation Toolkit is a Python-based security auditing tool designed to identify common Linux privilege escalation vulnerabilities and misconfigurations.

This toolkit automates the enumeration process used in penetration testing and security auditing by scanning Linux systems for:

- SUID/SGID binaries
- Weak file permissions
- Writable cron jobs
- Misconfigured services
- Sudo privilege issues
- Kernel information
- Potential privilege escalation vectors

The toolkit is developed for educational and defensive security purposes only.

---

# Features

## System Information Collection
- Current user detection
- Group enumeration
- Kernel version extraction
- Linux distribution detection
- Root/non-root execution check

## SUID/SGID Binary Enumeration
- Scans common binary directories
- Detects potentially dangerous SUID binaries
- Identifies binaries associated with privilege escalation techniques

## Weak Permission Scanning
- Detects world-writable files and directories
- Checks sensitive system locations
- Highlights insecure permissions

## Cron Job Analysis
- Enumerates system cron jobs
- Displays scheduled tasks
- Identifies potentially writable cron scripts

## Sudo Privilege Analysis
- Executes `sudo -l`
- Displays available sudo permissions
- Detects dangerous sudo configurations

## Systemd Service Enumeration
- Lists active system services
- Displays running services for security review

## Kernel Analysis
- Extracts Linux kernel version
- Assists in identifying outdated kernels and potential vulnerabilities

---

# Technologies Used

- Python 3
- Linux System Utilities
- Bash Commands
- Kali Linux
- WSL2

---

# Tools & Commands Used

- `find`
- `sudo`
- `uname`
- `systemctl`
- `ls`
- `grep`
- `awk`
- `sed`
- `crontab`

---

# Project Structure

```text
linux-privesc-toolkit/
│
├── main.py
├── README.md
├── requirements.txt
├── screenshots/
├── report/
└── sample_output/

## Usage

### Clone the repository
```bash
git clone https://github.com/supersecret134/linux-privesc-toolkit.git
cd linux-privesc-toolkit





