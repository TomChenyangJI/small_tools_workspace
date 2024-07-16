import requests

cookies = {
   
}

headers = {
    
}

response = requests.get(
    'https://www.nytimes.com/2024/06/22/us/politics/klain-kaufman-biden-campaign-election.html',
    # cookies=cookies,
    headers=headers,
)
print(response.status_code)
print(response.text)