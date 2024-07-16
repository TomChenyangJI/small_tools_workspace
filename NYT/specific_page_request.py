from config import headers
import requests
import datetime


def get_article_title(article_url):
    if "/" in article_url:
        li = article_url.split("/")
        title = li[-1]
        title = title.replace("-", " ")
        return title
    return str(datetime.datetime.now().strftime("%Y/%m/%d/%h/%M/%s")) + '.html'


def get_specific_page(article_url):
    with requests.session() as s:
        response = s.get(article_url, verify=False, headers=headers)
    base_dir = "./specific_page"
    html_path = base_dir + "/html"
    import os
    os.makedirs(html_path, exist_ok=True)
    with open(html_path + "/" + get_article_title(article_url), "w") as fi:
        print("path is :", html_path + "/" + get_article_title(article_url))
        fi.write(response.text)


if __name__ == "__main__":
    url = "https://www.nytimes.com/2024/07/12/us/politics/biden-trump-foreign-policy.html"
    get_specific_page(url)
