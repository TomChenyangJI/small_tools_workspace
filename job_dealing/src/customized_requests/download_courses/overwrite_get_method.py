import os
import requests
from config import headers, cookies


def get_request(url, output, new_cookies="./cookies.json", jsondata=None, params=None):
    if os.path.exists(new_cookies):
        with open(new_cookies, "r") as fi:
            import json
            cookies = json.loads(fi.read())
    try:
        if jsondata is not None and params is not None:
            response = requests.get(url=url, headers=headers, cookies=cookies, verify=False, json=jsondata, params=params)
        elif jsondata is not None:
            response = requests.get(url=url, headers=headers, cookies=cookies, verify=False, json=jsondata)
        elif params is not None:
            response = requests.get(url=url, headers=headers, cookies=cookies, verify=False, params=params)
        else:
            response = requests.get(url=url, headers=headers, cookies=cookies, verify=False)

    except Exception as e:
        raise e
    if output is None or output == "":
        output = "./output"
    url_component = url.strip().split("/")
    file_name = url_component[-1]
    if "." not in file_name:
        file_name = "temp.txt" if file_name.strip() == "" else file_name + ".txt"

    # print("output is %s now" % output)

    os.makedirs(output, exist_ok=True)

    with open(output + "/" + file_name, "wb") as fi:
        fi.write(response.content)
    return response
