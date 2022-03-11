import sys
import pendulum
from ctypes import windll
from pathlib import Path

OUTPUT_FILE = Path(r".\tim.csv")
HEADERS = "TASK,SUB-TASK,START TIME,END TIME,HOURS\n"
LAST_MONDAY = "2022-03-07"

def create_csv_if_needed(output_file=OUTPUT_FILE):
    if not output_file.is_file():
        with open(output_file, "w") as file:
            file.write(HEADERS)
            last_line = ""

def save_csv(output_file=OUTPUT_FILE):
    """Saves the contents of (global) lines to CSV file"""
    global lines
    with open(output_file, "w") as file:
        file.writelines(lines)

def create_message_box(message):
        windll.user32.MessageBoxW(0, message, "Easy Time Recorder")

def fetch_lines(input_file=OUTPUT_FILE):
    global lines, last_line
    with open(input_file, "r") as file:
        lines = file.readlines()
        last_line = str(lines[-1])

def create_backup():
    backup = OUTPUT_FILE.with_stem(OUTPUT_FILE.stem+"_backup")
    save_csv(backup)
    print(f"\nBackup file created: {backup}\n")

def add_hours():
    """ Adds missing hours to rows which only have start and end times"""
    fetch_lines()
    create_backup()
    global lines
    new_lines = [lines[0]]  # Include header
    for line in lines[1:]:
        columns = line.split(",")
        if len(columns) == 5:
            continue
        start = pendulum.from_format(columns[2].rstrip(), "YYYY-MM-DD HH:mm:ss")
        end = pendulum.from_format(columns[3].rstrip(), "YYYY-MM-DD HH:mm:ss")
        hours = round((end - start).total_hours(), 2)
        last_line = f"{','.join(columns).rstrip()},{hours}\n"
        new_lines += [last_line]
    lines = new_lines
    save_csv()

def calculate_totals():
    fetch_lines()
    global lines
    lines = [line.split(",") for line in lines[1:]]
    output = f"{len(lines)-1} work sessions\n\n"
    clients = {line[0] for line in lines}
    for client in clients:
        client_hours = sum([float(line[-1].rstrip()) for line in lines if line[0] == client and len(line) > 3])
        output += f"{round(client_hours, 2)} hours for client: {client}\n"
    tasks = {line[1] for line in lines}
    for task in tasks:
        task_hours = sum([float(line[-1].rstrip()) for line in lines if line[1] == task and len(line) > 3])
        output += f"{round(task_hours, 2)} hours on task: {task}\n"
    first = lines[1][2]
    last = lines[-1][3]
    output += f"\nFrom:\t{first}\nTo:\t{last}\n\n"
    create_message_box(output)

def process_command_line_input():
    global lines, last_line
    columns = last_line.split(",")
    if len(sys.argv) == 1:
        sys.argv += ["TOTALS"]
    if sys.argv[1] == "TOTALS":
        calculate_totals()
        return
    if len(sys.argv[1].split("-")) == 3:  # Date Format: "2022-02-17"
        hours_since()
        return
    if sys.argv[1] == "STOP":
        if len(columns) == 3:
            # Complete a time recording
            start = pendulum.from_format(columns[2].rstrip(), "YYYY-MM-DD HH:mm:ss")
            hours = round((now - start).total_hours(), 2)
            last_line = f"{last_line.rstrip()},{now_str},{hours}\n"
            lines = lines[:-1] + [last_line]
            message = "COMPLETED time recording:"
        else:
            message = "⚠ ERROR.  Please start new recording first.  Last entry:"
    else:
        # Create a new time recording
        if len(columns) == 3:
            message = "⚠ ERROR.  Please STOP previous recording first:"
        else:
            if len(sys.argv) < 3:
                sys.argv.append("(No further details)")
            _, task, details = sys.argv
            last_line = ",".join([task, details, now_str])
            lines += [last_line]
            message = "STARTED time recording:"
    save_csv()
    create_message_box(message + f"\n\n{last_line}")

def hours_since(date=LAST_MONDAY):
    fetch_lines()
    found = False
    for n, line in enumerate(lines):
        if date in line:
            found = True
            break
    if found:
        lines_since = [x.strip() for x in lines[n:]]
        hours = [x.split(",")[-1] for x in lines_since]
        hours_since = round(sum([float(x) for x in hours if x]), 2)
        message = f"⏰ {hours_since} hours worked since {date}\n\n"
        message += "\n".join(lines_since)
    else:
        message = f"⚠ No hours found for '{date}'"
    create_message_box(message)

if __name__ == "__main__":
    now = pendulum.now()
    now_str = now.format('YYYY-MM-DD HH:mm:ss')
    create_csv_if_needed()
    fetch_lines()
    process_command_line_input()
    save_csv
