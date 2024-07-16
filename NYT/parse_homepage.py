from bs4 import BeautifulSoup
import json

# with open("./nyt_home.html", "r") as fi:
#     content = fi.read()
#     soup = BeautifulSoup(content, features="html.parser")
#
# scripts = soup.find_all("script", {"data-rh": "true", "type": "application/ld+json"})
#
# article_urls = []
# # count = 0
# for script_ele in scripts:
#     # count += 1
#     # print(count)
#     # print(script_ele.text)
#     text = script_ele.text
#     text = json.loads(text)
#     # print(text.get("mainEntity").get("itemListElement"))
#     try:
#         item_list = text.get("mainEntity").get("itemListElement")
#         for item in item_list:
#             article_url = item.get("url")
#             article_urls.append(article_url)
#             # print(article_url)
#     except Exception:
#         break
# print(article_urls)
# for article in article_urls:
#     pass


def get_article_urls(html_content):
    soup = BeautifulSoup(html_content, features="html.parser")

    scripts = soup.find_all("script", {"data-rh": "true", "type": "application/ld+json"})

    article_urls = []
    for script_ele in scripts:
        text = script_ele.text
        text = json.loads(text)
        try:
            item_list = text.get("mainEntity").get("itemListElement")
            for item in item_list:
                article_url = item.get("url")
                article_urls.append(article_url)
        except Exception as e:
            break

    return article_urls
