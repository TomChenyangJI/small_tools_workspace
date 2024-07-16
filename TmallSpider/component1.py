import requests

proxies = {
    'http': 'http://localhost:9090',
    'https': 'http://localhost:9090',
}

cookies = {
    '_nk_': '%5Cu676F%5Cu660C94',
    '_tb_token_': 'eee3bbee85b0e',
    'cookie2': '1ed6ed8adfce8927bc4912fde99bca14',
    'csg': '7f188cef',
    'munb': '2209890789',
    'sgcookie': 'W100AfiwPkKjhgskYVK7OLdQ0HhQEj5RJqhWpuTe66tJr00%2BmYiPEXHVVNzolfSxgG1cTx6ZkdIyeADIP4lYdcAKqjIOIp%2FTOlm%2FienRd2IB4FZtyU7GoHL%2F%2B7aixovKZ2xc',
    't': '516915a793534a28da21dc1c22f2fd29',
    'unb': '2209890789',
}

headers = {
    'Host': 'h5.m.goofish.com',
    'Connection': 'keep-alive',
    'f-refer': 'wv_h5',
    'Accept': 'text/html,application/javascript,application/x-kun,application/vnd.kraken.bc1',
    'User-Agent': 'Kun (Kun/1.1.8.2-v7.16.20) Mozilla/5.0 (iPad; CPU OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) AliApp(FM/7.16.20) TTID/201200@fleamarket_iphone_7.16.20 WindVane/8.7.2  iPad8,6',
    'f-pTraceId': 'WVNet-41',
    'Referer': 'https://h5.m.goofish.com/cea/idleFish-F2e/idle-personal/pages/home?kun=true&url_pattern=fleamarket%3A%2F%2FpersonalPage&isOldFriendly=false&handlerName=FMPersonalPageHandler&userId=515013218&kun_downgrade_url=https%3A%2F%2Fh5.m.goofish.com%2Fapp%2FidleFish-F2e%2Fpersonal%2FHome%3Fwh_weex%3Dtrue%26url_pattern%3Dfleamarket%253A%252F%252FpersonalPage%26isOldFriendly%3Dfalse%26handlerName%3DFMPersonalPageHandler%26userId%3D515013218&wh_ttid=native',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Cookie': '_nk_=%5Cu676F%5Cu660C94; _tb_token_=eee3bbee85b0e; cookie2=1ed6ed8adfce8927bc4912fde99bca14; csg=7f188cef; munb=2209890789; sgcookie=W100AfiwPkKjhgskYVK7OLdQ0HhQEj5RJqhWpuTe66tJr00%2BmYiPEXHVVNzolfSxgG1cTx6ZkdIyeADIP4lYdcAKqjIOIp%2FTOlm%2FienRd2IB4FZtyU7GoHL%2F%2B7aixovKZ2xc; t=516915a793534a28da21dc1c22f2fd29; unb=2209890789',
}

params = {
    'kun': 'true',
    'url_pattern': 'fleamarket://personalPage',
    'isOldFriendly': 'false',
    'handlerName': 'FMPersonalPageHandler',
    'userId': '515013218',
    'kun_downgrade_url': 'https://h5.m.goofish.com/app/idleFish-F2e/personal/Home?wh_weex=true&url_pattern=fleamarket%3A%2F%2FpersonalPage&isOldFriendly=false&handlerName=FMPersonalPageHandler&userId=515013218',
    'wh_ttid': 'native',
}

response = requests.get(
    'https://h5.m.goofish.com/cea/idleFish-F2e/idle-personal/pages/home',
    params=params,
    cookies=cookies,
    headers=headers,
    # proxies=proxies,
    verify=False
)




import requests
import binascii
print(binascii.hexlify(response.content).decode('utf-8'))