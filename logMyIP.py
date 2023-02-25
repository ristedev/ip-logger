import requests

resp = requests.get('https://ipinfo.io')
with open("log.txt", "w") as f:
    f.write(resp.text)
