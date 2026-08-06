import os
import glob
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("config/smtp_config.json", "r") as file:
    config = json.load(file)

SMTP_SERVER = config["smtp_server"]
SMTP_PORT = config["smtp_port"]
SENDER_NAME = config["sender_name"]
RECIPIENTS = config["recipients"]

SMTP_EMAIL = os.environ["SMTP_EMAIL"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]

# Read Generated HTML

with open("artifacts/notification.html", "r", encoding="utf-8") as file:
    html_body = file.read()

if MODE == "manual":
    with open("artifacts/failure_summary.json", "r") as file:
        summary = json.load(file)

    repository = summary["repository"]
    job = summary["job"]
    workflow = summary["workflow"]

    subject = (
        f"🚨 CI/CD Failure | "
        f"{repository} | "
        f"{job}"
    )
else:
    summary_files = glob.glob("artifacts/*_summary.json")

    total = len(summary_files)
    passed = 0
    failed = 0

    for file in summary_files:

        with open(file, "r") as f:
            summary = json.load(f)

        if summary["status"].upper() == "SUCCESS":
            passed += 1
        else:
            failed += 1

    subject = (
        f"🌙 Nightly Pipeline Report | "
        f"Passed: {passed} | "
        f"Failed: {failed} | "
        f"Total: {total}"
    )

# Build Email 

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
message["To"] = ", ".join(RECIPIENTS)

message.attach(MIMEText(html_body, "html"))

# Send Email

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()

    server.login(SMTP_EMAIL, SMTP_PASSWORD)

    server.sendmail(SMTP_EMAIL, RECIPIENTS, message.as_string())

    server.quit()

    print("="*60)
    print("Email notification sent successfully.")
    print("="*60)
    print(f"Recipients : {len(RECIPIENTS)}")

    for recipient in RECIPIENTS:
        print(recipient)
except Exception as e:
    print("="*60)
    print("Failed to send email notification.")
    print("="*60)
    print(e)
    raise

