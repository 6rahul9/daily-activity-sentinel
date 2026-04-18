import datetime
import os

LOG_FILE = "daily_logs.md"

def update_logs():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    count = 1

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            content = f.read()
        count = content.count("## Entry ") + 1

    journal_entry = f"## Entry {count}\n"
    journal_entry += f"- **Timestamp:** {now} IST\n"
    journal_entry += f"- **Status:** System operational. Automated sentinel check-in completed.\n"
    journal_entry += f"- **Count:** {count}\n"
    journal_entry += "---\n\n"

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# Daily Activity Log\n\n")

    with open(LOG_FILE, "a") as f:
        f.write(journal_entry)

if __name__ == "__main__":
    update_logs()
