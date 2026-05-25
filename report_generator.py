def save_report(content):
    with open("report.txt", "w") as f:
        f.write(content)

    print("\n[+] Report saved as report.txt")
