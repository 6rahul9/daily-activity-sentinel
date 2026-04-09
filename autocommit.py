import datetime
import os

LOG_FILE = "daily_logs.md"

def update_logs():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(LOG_FILE):
        count = 1
        with open(LOG_FILE, "w") as f:
            f.write("# Daily Activity Log\n\n")
    else:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            try:
                last_line = [l for l in lines if "Count:" in l][-1]
                count = int(last_line.split("Count:")[1].strip()) + 1
            except (IndexError, ValueError):
                count = 1

    journal_entry = f"## Entry {count}\n"
    journal_entry += f"- **Timestamp:** {now} IST\n"
    journal_entry += f"- **Status:** System operational. Automated sentinel check-in completed.\n"
    journal_entry += f"- **Count:** {count}\n"
    journal_entry += "---\n\n"

    with open(LOG_FILE, "a") as f:
        f.write(journal_entry)

if __name__ == "__main__":
    update_logs()
