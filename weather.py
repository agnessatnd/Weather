import requests
import json
from datetime import datetime

# Tallinna koordinaadid
url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=59.4370&lon=24.7536'

headers = {
    'User-Agent': 'MyUniqueUserAgent/1.0'
}
response = requests.get(url, headers=headers)
try:
    data = response.json()
except json.decoder.JSONDecodeError as e:
    print("Response text:", response.text)
    data = None

for forecast in data['properties']['timeseries'][:10]:
    timestamp = forecast['time']
    temperature = forecast['data']['instant']['details']['air_temperature']
    formatted_time = datetime.fromisoformat(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')
    print(f'{formatted_time} {temperature}°C')
