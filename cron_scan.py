import subprocess

def scan_cron():
    print("\n[+] CRON JOB ANALYSIS\n")

    cron = subprocess.getoutput("ls -la /etc/cron*")
    print(cron)

    system_cron = subprocess.getoutput("cat /etc/crontab")
    print(system_cron)
