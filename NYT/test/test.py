import requests


s = requests.session()

nyt_home = "https://www.nytimes.com/"

response = s.get(nyt_home, verify=False)


print(response.cookies)
print(response.headers)
print(response.headers.get('Set-Cookie'))