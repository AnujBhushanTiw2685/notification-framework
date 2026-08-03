import json

with open("artifacts/failure_summary.json", "r") as file:
    failure = json.load(file)
    component = failure["component"]
    job = failure["job"]
    status = failure["status"]
    timestamp = failure["timestamp"]
    error = failure["error"]
    exit_code = failure["exit_code"]

html = f"""
<!DOCTYPE html>
<html>

<head>
    <Title> CI/CD Failure Notification </Title>
</head>

<body>

<h1>CI/CD Failure Notification</h1>

<hr>

<p><b>Component:</b>{component}</p>
<p><b>Job:</b>{job}</p>
<p><b>Status:</b>{status}</p>
<p><b>Time:</b>{timestamp}</p>

<hr>

<h3>Error</h3>

<pre>{error}</pre>

<hr>

<p><b>Exit Code:</b>{exit_code}</p>

</body>

</html>

"""

with open("artifacts/notification.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML notification generated successfully.")
print("Location: artifacts/notification.html")

