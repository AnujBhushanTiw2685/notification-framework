import os
import json
import urllib.request

OWNER = os.environ["OWNER"]
TOKEN = os.environ["GITHUB_TOKEN"]
components = os.environ["COMPONENTS"].split()

nightly_runs = []

for repository in components:

    print("="*60)
    print(f"Fetching latest nightly run for {repository}")
    print("="*60)

    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{repository}/actions/runs"
        f"?event=repository_dispatch&per_page=1"
    )

    request = urllib.request.Request(url)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {TOKEN}")

    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read())

    workflow_runs = data.get("workflow_runs", [])

    if workflow_runs:
        run = workflow_runs[0]

        nightly_runs.append({

            "owner": OWNER,
            "repository": repository,
            "run_id": run["id"],
            "status": run["status"],
            "conclusion": run["conclusion"],
            "run_url": run["html_url"]
            
        })
    else:
        nightly_runs.append({

            "owner": OWNER,
            "repository": repository,
            "run_id": "",
            "status": "not_triggered",
            "conclusion": "",
            "run_url":  ""
            
        })

os.makedirs("artifacts", exist_ok=True)

with open("artifacts/nightly_runs.json", "w") as file:
    json.dump(nightly_runs, file, indent=4)

print("\n===== NIGHTLY SUMMARY =====")
print(json.dumps(nightly_runs, indent=4))



    