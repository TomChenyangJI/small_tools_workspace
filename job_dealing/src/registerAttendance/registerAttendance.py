import requests


def register_attendance():
    with requests.Session() as s:
        headers = {
            'Host': 'example.com',
            'lang': 'zh',
            'nflag': '1',
            'deviceName': 'iPhone10,3',
            'osTarget': '1',
            'networkType': 'LTE',
            'Accept': '*/*',
        }

        data = 'loginName=JCJ9H/yevOtY23/DV'

        s.post('https://example.com//', headers=headers, data=data, verify=False)
        params = {
            'numType': '2',
            'users': 'example',
        }
        s.get("https://example.com//examplet/mservice/person/", params=params)
        json_data = {
            'locale': 'cn',
            'employeeNumber': 'example',
            'deviceType': '0',
        }
        s.get('https://example.com/examplet/mattend-new/service/getrecord', json=json_data
              , verify=False)

        params = {
            'comVer': '1077',
            'allowBreak': 'true',
            'method': 'postMap',
        }

        data = {
            'installParas': '{}],"lastTime":0}',
        }

        s.post(
            'https://example.com/examplet/services/example/com.example.works/16.7.1/1/513',
            params=params,
            data=data, verify=False
        )

        json_data = {
            'lastUpdateDate': '2000-01-01 00:00:00',
        }

        s.post(
            'https://example.com/examplet/mcontact/services/userbehavior',
            json=json_data, verify=False
        )

        params = {
            'validateUser': 'false',
        }

        json_data = {
            'locale': 'cn',
            'meapip': '45.249.212.73',
            'x': '1.6322350',
            'employeeNumber': 'example',
            'deviceType': '0',
            'y': '3',
            'deviceVersionId': '16.7.1',
            'deviceModel': 'iPhone10,3',
        }

        response = s.post(
            'https://example.com//examplet/mbm-new/rest/mattend/registerAttendance',
            params=params,
            json=json_data, verify=False
        )
        print(response.status_code)
        print("*" * 10)
        print(response.text)
        # print("*" * 10)
        # print(response.content)


# register_attendance()
