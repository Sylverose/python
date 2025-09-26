# error_log.py - Python assignment part 3
import os

# Set file path to source_data.csv
file_path = os.path.join("data", "source_data.csv")

# Try to check if the file exists before attempting to open it
try:
    if not os.path.exists(file_path):
        print(f"Filen blev ikke fundet: {file_path}")
    else:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Read file line by line
            lines = content.splitlines()
            # Parse lines and check for errors
            for line_number, line in enumerate(lines, start=1):
                # Check for empty lines and create a log .txt file in csv_log folder under data
                if not line.strip():
                    with open(
                        os.path.join("data", "csv_log", "empty_lines.txt"), "a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"Linje {line_number} er tom.\n")
                # Check if the customer id is not an integer and log these lines in id_errors.txt   
                if not any(char.isnumeric() for char in line):
                    with open(
                        os.path.join("data", "csv_log", "id_errors.txt"), "a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"Linje {line_number} har ugyldig id: {line}\n")
                # Check if the email column contains an "@" symbol and log these lines in email_errors.txt
                if "@" not in line:
                    with open(
                        os.path.join("data", "csv_log", "email_errors.txt"), "a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"Linje {line_number} har ugyldig email: {line}\n")
            print(
                "Færdig med at analysere filen. Tjek csv_log mappen for detaljer."
            )
            # Print total number of empty lines by counting lines in empty_lines.txt
            empty_lines_count = 0
            empty_lines_path = os.path.join("data", "csv_log", "empty_lines.txt")
            if os.path.exists(empty_lines_path):
                with open(empty_lines_path, "r", encoding="utf-8") as log_file:
                    empty_lines_count = len(log_file.readlines())
            print(f"Tomme linjer: {empty_lines_count}")

            # Print total number of lines with wrongly formatted IDs by counting lines in id_errors.txt
            id_errors_count = 0
            id_errors_path = os.path.join("data", "csv_log", "id_errors.txt")
            if os.path.exists(id_errors_path):
                with open(id_errors_path, "r", encoding="utf-8") as log_file:
                    id_errors_count = len(log_file.readlines())
            print(f"Linjer med ugyldige id'er: {id_errors_count}")

            # Print total number of lines with wrongly formatted emails by counting lines in email_errors.txt
            email_errors_count = 0
            email_errors_path = os.path.join("data", "csv_log", "email_errors.txt")
            if os.path.exists(email_errors_path):
                with open(email_errors_path, "r", encoding="utf-8") as log_file:
                    email_errors_count = len(log_file.readlines())
            print(f"Linjer med ugyldige emails: {email_errors_count}")
            
except FileNotFoundError:
    print(f"Kunne ikke finde filen: {file_path}")
except PermissionError:
    print(f"Adgang nægtet ved læsning af: {file_path}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")