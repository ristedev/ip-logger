import requests
import datetime
import json

# Get datetime & convert it to a string
ct = str(datetime.datetime.now())

# Get IP, add timestamp & log to txt file
resp = requests.get('https://ipinfo.io')
with open("log.txt", "a") as f:
    respData = resp.json()
    respData["timestamp"] = ct
    f.write(json.dumps(respData, indent=2))

# Print data
print(json.dumps(respData, indent=2))
