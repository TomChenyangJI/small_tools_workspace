PROJECT_BASE_DIRECTORY = "~/Desktop/web_spider_test/image_downloader"

config_edx_img = {
}

headers = {
    'Host': 'http://example.com/',
    'lang': 'zh',
    'nflag': '1',
    'osTarget': '1',
    'Connection': 'keep-alive',
    'networkType': 'LTE',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
}

cookies = {
    'edxloggedin': 'true'
}

config1 = {}
config2 = {}
config3 = {}
config4 = {}
config5 = {}
config6 = {}
config7 = {}
config8 = {}
config9 = {}

config9 = {}

config10 = {}

config11 = {}

config12 = {}

config13 = {}

config14 = {}

config15 = {}

config16 = {}

config17 = {}

Configs = [config1, config2, config3, config4, config5, config6, config7, config8, config9, config10, config11,
           config12, config13, config14, config15, config16, config17]


def request_get(uri, 8config):
    import requests
    response = ""
    if config8.get("cookies"):
        if config.get("headers"):
            if config.get("params"):
                response = requests.get(uri, cookies=config.get("cookies"),
                                        headers=config.get("headers"),
                                        params=config.get("params"), verify=False)
            else:
                response = requests.get(uri, cookies=config.get("cookies"),
                                        headers=config.get("headers"), verify=False)
        else:
            response = requests.get(uri, cookies=config.get("cookies"), verify=False)
    return response
