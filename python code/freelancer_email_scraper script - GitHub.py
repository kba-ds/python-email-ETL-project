import imaplib
import email
import os
import re
import pandas as pd
from bs4 import BeautifulSoup
from email.utils import parsedate_to_datetime

EMAIL = "........................" # Email address removed. Protection from hacking
PASSWORD = "...................."  # Gmail app password used. Password removed. Protection from hacking

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(EMAIL, PASSWORD)
imap.select("INBOX")

status, messages = imap.search(None, '(FROM "noreply@notifications.freelancer.com")')
email_ids = messages[0].split()
print(f"Found {len(email_ids)} Freelancer emails")

## ########### STEP 2-4: FETCH, SAVE HTML, EXTRACT JOB DETAILS (one pass per email)

os.makedirs("emails/html", exist_ok=True)
os.makedirs("output", exist_ok=True)

email_metadata = []
jobs = []

pattern = re.compile(
    r'(?P<title>.+?)\n'
    r'(?P<description>.+?)\n'
    r'\.\.\.\n'
    r'See more\n'
    r'Skills:\n'
    r'(?P<skills>.+?)\n'
    r'(?P<budget>\$.+?)\n'
    r'Bid now'
)

for email_id in email_ids:
    _, msg_data = imap.fetch(email_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    sender = msg["From"]
    subject = msg["Subject"]
    email_date = parsedate_to_datetime(msg["Date"])

    email_metadata.append({
        "email_id": email_id.decode(),
        "sender": sender,
        "subject": subject,
        "email_date": email_date,
    })

    # Grab the HTML body (if present) and save it to disk
    html_content = None
    try:
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                payload = part.get_payload(decode=True)
                if payload is not None:
                    html_content = payload.decode(errors="ignore")
                break
    except Exception as e:
        print(f"[{email_id.decode()}] error extracting HTML: {e}")
        continue

    if not html_content:
        print(f"[{email_id.decode()}] no HTML part found, skipping")
        continue

    filename = email_date.strftime("%Y-%m-%d_%H-%M-%S.html")
    with open(f"emails/html/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)

    # Extract clean, newline-separated text from the HTML for regex matching
    soup = BeautifulSoup(html_content, "html.parser")
    email_text = soup.get_text("\n", strip=True)

    match_count = 0
    for match in pattern.finditer(email_text):
        match_count += 1
        jobs.append({
            "email_date": email_date,
            "job_title": match.group("title").strip(),
            "job_description": match.group("description").replace("\n", " ").strip(),
            "skills": match.group("skills").replace("\n", " ").strip(),
            "budget": match.group("budget").strip(),
        })
    if match_count == 0:
        print(f"[{email_id.decode()}] HTML saved but regex found 0 job matches")

## ########### STEP 5. CONVERT TO DATAFRAMES

log_df = pd.DataFrame(email_metadata)
jobs_df = pd.DataFrame(jobs)
print(f"\nTotal emails processed: {len(email_metadata)}")
print(f"Total job listings extracted: {len(jobs_df)}")
print("\nPreview (first 5 rows):")
print(jobs_df.head())

## ########### STEP 6. SAVE DATA AS CSV

jobs_df.to_csv("output/freelancer_jobs.csv", index=False, encoding="utf-8")
print(f"\nSaved {len(jobs_df)} rows to output/freelancer_jobs.csv")

imap.logout()
