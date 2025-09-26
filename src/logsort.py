# Log file sorting - Python assignment part 2
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
            # For every line containing "error" (case-insensitive), save the line to a new file called errors.txt in the data folder
            error_lines = [line for line in lines if "error" in line.lower()]
            with open(os.path.join("data", "errors.txt"), "w", encoding="utf-8") as error_file:
                for line in error_lines:
                    error_file.write(line + "\n")
            print(f"{len(error_lines)} fejl-linjer til errors.txt")
            # For every line containing "warning" (case-insensitive), save the line to a new file called warnings.txt in the data folder
            warning_lines = [line for line in lines if "warning" in line.lower()]
            with open(os.path.join("data", "warnings.txt"), "w", encoding="utf-8") as warning_file:
                for line in warning_lines:
                    warning_file.write(line + "\n")
            print(f"{len(warning_lines)} advarsels-linjer til warnings.txt")
            # For every line containing "info" (case-insensitive), save the line to a new file called info.txt in the data folder
            info_lines = [line for line in lines if "info" in line.lower()]
            with open(os.path.join("data", "info.txt"), "w", encoding="utf-8") as info_file:
                for line in info_lines:
                    info_file.write(line + "\n")    
            print(f"{len(info_lines)} info-linjer til info.txt")
            # For every line containing "success" (case-insensitive), save the line to a new file called success.txt in the data folder
            success_lines = [line for line in lines if "success" in line.lower()]
            with open(os.path.join("data", "success.txt"), "w", encoding="utf-8") as success_file:
                for line in success_lines:
                    success_file.write(line + "\n")
            print(f"{len(success_lines)} succes-linjer til success.txt")
            # Print total number of lines in the original log file
            print(f"Totalt antal linjer i logfilen: {len(lines)}")
            # Print original log file content to console
            print(f"Original logfil indhold:")
            print(content)           
except FileNotFoundError:
    print(f"Kunne ikke finde filen: {file_path}")
except PermissionError:
    print(f"Adgang nægtet ved læsning af: {file_path}")
except Exception as e:
    print(f"Der opstod en fejl: {e}")
