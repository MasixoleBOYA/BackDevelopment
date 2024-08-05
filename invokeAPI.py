import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
)

for i in response.json()['items']:
    print(f"\n----item-----\n {i}")