import requests

cookies = {
  
}

headers = {
  
   
}

response = requests.get('https://www.nytimes.com/2024/06/23/us/politics/biden-trump-debate-stakes.html', headers=headers, verify=False)

print(response.status_code)
print(response.text)
