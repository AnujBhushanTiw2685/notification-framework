import json

with open("artifacts/failed_job.json", "r") as file:
    failed_job = json.load(file)

job_name = failed_job["name"]

print(f"Failed Job : {job_name}")