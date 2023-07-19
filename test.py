
import requests

url = 'https://api.datadoghq.com/api/v2/metrics'
headers = {
    'DD-APPLICATION-KEY': '',
    'DD-API-KEY': ''
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    metrics = response.json()

