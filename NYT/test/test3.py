from pyhtml2pdf import converter

# converter.convert("~/Desktop/AllWorkspaces/PythonWorkspaces/Space1/web_spider_test/NYT/donald trump michael flynn qanon.html", "trump.pdf")

import pdfkit

# pdfkit.from_file("~/Desktop/AllWorkspaces/PythonWorkspaces/Space1/web_spider_test/NYT/donald trump michael flynn qanon.html", "trump.pdf")
# pdfkit.from_url('https://www.nytimes.com/2024/06/23/us/politics/biden-trump-debate-stakes.html', 'trump.pdf')
from bs4 import BeautifulSoup
import html2text

with open("donald trump michael flynn qanon.html", 'r') as fi:
    soup = BeautifulSoup(fi, features="html.parser")
    # div
    #
    #
    # class ="vi-gateway-container" data-testid="vi-gateway-container
    # text = soup.find("body").find('div', {"class":"vi-gateway-container", "data-testid":"vi-gateway-container"})
    # text = soup.find("body").find('div', {"class":"vi-gateway-container", "data-testid":"vi-gateway-container"})
    # # print(text.text)
    # text = soup.find("div", {"id": 'app'})
    # print(html2text.html2text(text))
    # html = open("donald trump michael flynn qanon.html").read()
    # print(html2text.html2text(html))