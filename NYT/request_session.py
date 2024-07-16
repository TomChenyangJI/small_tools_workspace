import requests


# s = requests.session()
# s.get("https://www.nytimes.com/", verify=False)

def NYTSession(url="https://www.nytimes.com/"):
    with requests.session() as s:
        s = requests.session()
        response = s.get(url, verify=False)
        headers = response.headers
        cookies = headers.get("Set-Cookie")
        headers["cookie"] = cookies
        headers.pop("Set-Cookie")
        print(headers)
        print(">>>><<<<")
        response = s.get("https://www.nytimes.com/2024/06/23/world/europe/the-nation-resurgent-and-borders-too.html",
        # headers=headers,
                         verify=False)
        print(response.status_code)


    # track_url = "https://a.et.nytimes.com/track"
    # data = '[{"context_id":"Jv60W4MmIPtC4RS9Le8CYo0e","pageview_id":"H2RCRVw65P09YpUbIHY5Jwy8","event_id":"H2RCRVw65P09YpUbIHY5Jwy8","client_lib":"v1.3.0","sourceApp":"nyt-vi","subject":"page","how":"beacon","client_ts":1719117219403,"data":{"canonicalUrl":"https://www.nytimes.com/","nyt_uri":"nyt://programmingnode/1999c500-b740-5ba9-b2c1-57ff6b183315","url":"https://www.nytimes.com/","client_tz_offset":-480}}]'
    # # print(headers)
    # headers["cookie"] = headers.get("Set-Cookie")
    # headers.pop("Set-Cookie")
    # response = s.get(track_url, verify=False, headers=headers, data=data)
    # headers = response.headers
    # print(headers)
    # print(">>>>>><<<<<<<")
    # return s, headers

NYTSession()
# print(s.headers)
# print(headers)
# response = s.get("https://www.nytimes.com/2024/06/23/world/europe/the-nation-resurgent-and-borders-too.html", verify=False, headers=headers)

# print(response.status_code)

