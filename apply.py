import json
import hmac
import hashlib
import requests
import os
from datetime import datetime, timezone

data = {
    "name": "Shepherd Umanah",
    "email": "goldofonime@gmail.com", 
    "resume_link": "https://docs.google.com/document/d/1RsBMH8J29oi3KLF6hhqVPNyx6c46pnZLeFhgQxJbBbI/edit?usp=sharing",
    "repository_link": f"https://github.com/{os.getenv('GITHUB_REPOSITORY')}",
    "action_run_link": f"https://github.com/{os.getenv('GITHUB_REPOSITORY')}/actions/runs/{os.getenv('GITHUB_RUN_ID')}",
    "timestamp": datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z")
}

payload = json.dumps(data, separators=(',', ':'), sort_keys=True).encode('utf-8')

secret = b"hello-there-from-b12"
signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()
headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}"
}

response = requests.post("https://b12.io/apply/submission", data=payload, headers=headers)

if response.status_code == 200:
    print("Application submitted successfully!")
else:
    print(f"Failed with status {response.status_code}: {response.text}")
    exit(1) 