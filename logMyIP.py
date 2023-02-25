import requests
import datetime

# Get datetime & convert it to a string
ct = str(datetime.datetime.now())

# Get IP & log to txt file
resp = requests.get('https://ipinfo.io')
with open("log.txt", "a") as f:
    f.write("-------------------------")
    f.write("\n" + ct + "\n")
    f.write("IP Address: " + resp.text + "\n")
