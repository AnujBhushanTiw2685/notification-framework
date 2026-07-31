import os
import json


with open("artifacts/failed_job.json", "r") as file:
    failed_job = json.load(file)

job_name = failed_job["name"]

print(f"Failed Job : {job_name}")

# Define log folder
logs_folder = "artifacts/extracted_logs"
log_file = None

# Search for the matching log file
for file in os.listdir(logs_folder):
    file_path = os.path.join(logs_folder, file)

    if os.path.isfile(file_path):
        if job_name in file:
            log_file = file_path
            break

# print log file path if found
if log_file:

    print("\nMatching log file found:")
    print(log_file)
    with open (log_file, "r", encoding="utf-8") as file:
        log_content = file.read()
        print("\n" + "="*60)
        print("LOG PREVIEW")
        print("="*60)

        print(log_content[-2000:])
else:
    print("\nNo matching log file found.")

