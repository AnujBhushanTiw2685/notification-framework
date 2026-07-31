import os
import json
import urllib.request

OWNER = os.environ["OWNER"]
REPOSITORY = os.environ["REPOSITORY"]
RUN_ID = os.environ["RUN_ID"]
TOKEN = os.environ["TOKEN"]

url = (
    f"https://api.github.com/repos/"
    f"{OWNER}/{REPOSITORY}/actions/runs/{RUN_ID}/jobs"
)

request = urllib.request.Request(url)
request.add_header("Accept", "application/vnd.github+json")
request.add_header("Authorization", f"Bearer {TOKEN}")

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read())

jobs = data["jobs"]

print("===== RAW GITHUB API RESPONSE =====")
print(json.dumps(data, indent=4))

print("\n\n===== WORKFLOW JOB SUMMARY =====")

failed_job = None

for job in data["jobs"]:
    if job["conclusion"] == "failure":
        failed_job = job
        break

if failed_job:
    print("=" * 60)
    print("FAILED JOB FOUND")
    print("=" * 60)

    print(f"Job Name      : {failed_job['name']}")
    print(f"Job ID        : {failed_job['id']}")
    print(f"Status        : {failed_job['status']}")
    print(f"Conclusion    : {failed_job['conclusion']}")
    print(f"Started At    : {failed_job['started_at']}")
    print(f"Completed At  : {failed_job['completed_at']}")
else:
    print("No failed jobs found.")