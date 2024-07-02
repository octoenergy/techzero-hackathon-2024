import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

# Define the endpoint and parameters
baselink = 'https://api.octopus.energy'

urlMeter = f"{baselink}/v1/electricity-meter-points/1413985791007/meters/21J0016813/consumption/"
params = {
    "period_from": "2024-01-01T00:00:00",
    "period_to": "2024-06-30T00:00:00",
    "page_size": 2000
}

# Define the authentication details
auth = HTTPBasicAuth('', '')

# Make the request
response = requests.get(urlMeter, params=params, auth=auth)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    consumption_data = data['results']
    df = pd.DataFrame(consumption_data)
    print(data)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
    
    
productsUrl = f'{baselink}/v1/products/'
response = requests.get(productsUrl, params=params, auth=auth)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    consumption_data = data['results']
    df = pd.DataFrame(consumption_data)
    print(data)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")