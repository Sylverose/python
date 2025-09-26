# Log file sorting - Python assignment part 2 extra task
import os

# Set file path
file_path = os.path.join("data", "app_log (logfil analyse) - random.txt")

# Try to check if the file exists before attempting to open it
try:
    if not os.path.exists(file_path):
        print(f"Filen blev ikke fundet: {file_path}")
    else:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Read file line by line
            lines = content.splitlines()
            # For every type of log, save the lines to a new file with corresponding name (not case-sensitive) inside the data/logsort folder
            log_types = ["error", "warning", "info", "success"]
            for log_type in log_types: 
                log_lines = [line for line in lines if log_type in line.lower()]
                with open(os.path.join("data", "logsort", f"{log_type}s.txt"), "w", encoding="utf-8") as log_file:
                    for line in log_lines:
                        log_file.write(line + "\n")
                print(f"Der er {len(log_lines)} {log_type} linjer til {log_type}s.txt")
                
except FileNotFoundError:
    print(f"Kunne ikke finde filen: {file_path}")
except PermissionError:
    print(f"Adgang nægtet ved læsning af: {file_path}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")

