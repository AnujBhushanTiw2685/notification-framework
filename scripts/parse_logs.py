import os
import json


with open("artifacts/failed_job.json", "r") as file:
    failed_job = json.load(file)

repository = failed_job["repository"]
workflow = failed_job["workflow_name"]
run_id = failed_job["run_id"]
run_url = failed_job["html_url"]
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

    with open(log_file, "r", encoding="utf-8") as file:
        log_content = file.read()

    lines = log_content.splitlines()

    component = ""
    status = ""
    timestamp = ""
    error_message = ""
    exit_code = ""

    # Loop through all lines
    for line in lines:

        line = line.strip()

        if "COMPONENT :" in line:
            component = line.partition("COMPONENT :")[2].strip()

        elif "STATUS :" in line:
            value = line.partition("STATUS :")[2].strip()
            if value:
                status = value

        elif "TIME" in line:
            timestamp = line.partition("TIME")[2].replace(":", "", 1).strip()

        elif "python:" in line:
            error_message = line

        elif "exit code" in line.lower():
            exit_code = line.partition("exit code")[2].replace(".", "").strip()

    # Create summary AFTER loop finishes
    failure_summary = {

        "repository": repository,
        "workflow": workflow,
        "component": component,
        "job": job_name,
        "status": status,
        "timestamp": timestamp,
        "error": error_message,
        "run_id": run_id,
        "run_url": run_url,
        "exit_code": exit_code

    }

    with open("artifacts/failure_summary.json", "w") as file:
        json.dump(failure_summary, file, indent=4)

    print("\n===== FAILURE SUMMARY =====")
    print(json.dumps(failure_summary, indent=4))

else:
    print("\nNo matching log file found.")