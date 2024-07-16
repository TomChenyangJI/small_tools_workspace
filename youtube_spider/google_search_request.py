import requests
# print(requests.get('https://httpbin.org/ip').json())

# import os
# def set_proxy(user='*', passwd='*', address='ftq-hk.02ijp4uos1.download', port=int('13018')):
#     proxy_addr = 'http://{user}:{passwd}@{address}:{port}'.format(
#         user=user, passwd=passwd,
#         address=address, port=port)
#     os.environ['http_proxy'] = proxy_addr
#     os.environ['https_proxy'] = proxy_addr
#
#
# def unset_proxy():
#     os.environ.pop('http_proxy')
#     os.environ.pop('https_proxy')
# set_proxy()
# unset_proxy()

response = requests.get("https://www.google.com/search?q=hello")
# print(">>>", response)
print(">>>", response.text)
# with open("logo.google.png", 'wb') as img:
#     img.write(response.content)

# response = requests.post('https://rr3---sn-i3belne6.googlevideo.com/videoplayback', params=params, headers=headers, data=data, verify=False)
response = requests.get("https://www.reddit.com/user/chevignon93/", verify=False)
# unset_proxy()
print(response.status_code)
print("*" * 10)
print(response.content)
with open("test/test.txt", "wb") as fi:
    fi.write(response.content)
    # https://rr3---sn-i3belne6.googlevideo.com/videoplayback?expire=1718303468&ei=jOZqZq7iB9eSvcAP9smn2As&ip=23.158.104.167&id=o-AOPR7XccKMS9b5C1MMywlUVBKPl22tkre09YtDIWZ5SO&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=aM&mm=31%2C26&mn=sn-i3belne6%2Csn-un57snee&ms=au%2Conr&mv=m&mvi=3&pl=24&initcwndbps=3116250&siu=1&spc=UWF9f8_xs5O6PUot-q-K7Zt2nfIyWlwjfhu_KcUmrTm8ST1st8H_FcctGzYBO7EIAWR9o6FPxQ&svpuc=1&ns=Z-PIhfhwM_q5Bq9rN9uUweYQ&sabr=1&rqh=1&mt=1718281507&fvip=5&keepalive=yes&c=WEB&smc=1&n=F3YCXezCIwy7aQ&sparams=expire%2Cei%2Cip%2Cid%2Csource%2Crequiressl%2Cxpc%2Csiu%2Cspc%2Csvpuc%2Cns%2Csabr%2Crqh&sig=AJfQdSswRQIgI0fOWRIqzBI2OrH5ylnAYTsrTp-xqJiM_8YSTmlEeQkCIQCOCpl3sgjifjY4e9mRaVGEwT3FzmyPbV5n9L2Evai22Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHlkHjAwRgIhAK93fHWVhd4uh6whwg9XTSphJeWIgrGrg24F6EuA8bqHAiEAh1z1DPaKbY_GOuolEn_ef05VHgqOlKMi7GzwZTNTq34%3D&cpn=lOWRPeA7wTQUXiD5&cver=2.20240612.01.00&rn=27
