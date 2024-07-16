

def get_weather_detail(lat=33.553098, lng=119.036716) -> str:
    import http.client
    from config import weather_x_api_key
    # https://docs.ambeedata.com/DeveloperTools/?refId=weather&subRefId=weather-latest
    # this is the website
    import ssl
    context = ssl.SSLContext()
    conn = http.client.HTTPSConnection("api.ambeedata.com", context=context)

    headers = {
        'x-api-key': weather_x_api_key,
        'Content-type': "application/json"
    }

    # 33.553098, 119.036716 N, E
    conn.request("GET", f"/weather/latest/by-lat-lng?lat={lat}&lng={lng}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return data.decode("utf-8")


def process_response(res):
    import json
    res = json.loads(res)
    return res.get("data").get('summary')
