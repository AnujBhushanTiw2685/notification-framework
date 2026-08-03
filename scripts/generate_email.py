import json

with open("artifacts/failure_summary.json", "r") as file:
    failure = json.load(file)

    repository = failure["repository"]
    workflow = failure["workflow"]
    component = failure["component"]
    job = failure["job"]
    status = failure["status"]
    timestamp = failure["timestamp"]
    error = failure["error"]
    run_id = failure["run_id"]
    run_url = failure["run_url"]
    exit_code = failure["exit_code"]

    

with open("templates/email_template.html", "r", encoding="utf-8") as file:
    html = file.read()

# Replace placeholders with actual values
html = html.replace("{{REPOSITORY}}", repository)
html = html.replace("{{WORKFLOW}}", workflow)
html = html.replace("{{COMPONENT}}", component)
html = html.replace("{{JOB}}", job)
html = html.replace("{{STATUS}}", status)
html = html.replace("{{TIMESTAMP}}", timestamp)
html = html.replace("{{ERROR}}", error)
html = html.replace("{{RUN_ID}}", str(run_id))
html = html.replace("{{RUN_URL}}", run_url)
html = html.replace("{{EXIT_CODE}}", exit_code)

with open("artifacts/notification.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML notification generated successfully.")
print("Location: artifacts/notification.html")

