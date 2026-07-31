import os
import urllib.request
import zipfile

OWNER = os.environ["OWNER"]
REPOSITORY = os.environ["REPOSITORY"]
RUN_ID = os.environ["RUN_ID"]
TOKEN = os.environ["GITHUB_TOKEN"]

url = (
    f"https://api.github.com/repos/"
    f"{OWNER}/{REPOSITORY}/actions/runs/{RUN_ID}/logs"

)

request = urllib.request.Request(url)
request.add_header("Accept", "application/vnd.github+json")
request.add_header("Authorization", f"Bearer {TOKEN}")

response = urllib.request.urlopen(request)

# download the logs as a zip file

with open("workflow_logs.zip", "wb") as file:
    file.write(response.read())

print("Workflow logs downloaded successfully.")

# Extract the logs from the zip file

extract_folder = "workflow_logs"

with zipfile.ZipFile("workflow_logs.zip", "r") as zip_ref:
    zip_ref.extractall(extract_folder)

print(f"Logs extracted to '{extract_folder}'")


# Display the extracted log files

print("\nExtracted log files:\n")

for root, dirs, files in os.walk(extract_folder):
    for  file in files:
        print(os.path.join(root,file))

