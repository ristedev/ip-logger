import requests

resp = requests.get('https://ipinfo.io')
print(resp.json())
