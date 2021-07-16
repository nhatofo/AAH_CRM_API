import requests
import json

url = ('http://10.72.0.216:5000/')
for response in url.json():
  response = requests.get(url)
  data = response.json()
  with open('data.json', 'w') as f:
    json.dump(data, f)
    