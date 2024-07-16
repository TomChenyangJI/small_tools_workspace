import requests
from parse_homepage import get_article_urls
import datetime
import time
from config import headers


s = requests.session()


def get_home_page(nyt_url="https://www.nytimes.com/", s=s):
    response = s.get(nyt_url, verify=False)
    if response.status_code == 200:
        return response.text


def get_article_title(article_url):
    if "/" in article_url:
        li = article_url.split("/")
        title = li[-1]
        title = title.replace("-", " ")
        return title
    return str(datetime.datetime.now().strftime("%Y/%m/%d/%h/%M/%s")) + '.html'


def convert_txt_to_pdf(in_file, out_file):
    # text file to pdf file
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_font('Arial', '', "Arial Unicode.ttf", uni=True)

    # Open the text file and read its contents
    with open(in_file, 'r') as f:
        text = f.read()

    # Add a new page to the PDF
    pdf.add_page()

    # Set the font and font size
    pdf.set_font('Arial', size=12)

    # Write the text to the PDF
    pdf.write(5, text)

    # Save the PDF
    pdf.output(out_file)


def dispose_text(text):
    lines = text.split("\n")
    lines = list(filter((lambda x: (not x.strip().startswith("*") or x.strip() == "")), lines))
    text = "\n".join(lines)
    return text


def get_and_save_each_article(article_url, s=s):
    """
    check the url first, to see if it is today's news
    return a text article
    :param article_url:
    :return:
    """
    # print(datetime.datetime.now())
    today = datetime.datetime.now()
    delta = datetime.timedelta(days=-1)
    yesterday = today + delta
    # date_component = datetime.datetime.now().strftime("%Y/%m/%d")
    yesterday_date_component = str(yesterday.strftime("%Y/%m/%d"))
    today_date_component = str(today.strftime("%Y/%m/%d"))
    # print(article_url)
    # print("is it right: ", (yesterday_date_component in article_url or today_date_component in article_url))
    if ((yesterday_date_component in article_url or today_date_component in article_url) and
            article_url.endswith("html")):
        response = s.get(article_url, verify=False, headers=headers)
        print(response.status_code)

        if response.status_code == 200:
            import os
            article_name_base_path = f"./html/{today_date_component}"
            os.makedirs(article_name_base_path, exist_ok=True)
            article_name = article_name_base_path + "/" + get_article_title(article_url)
            with open(article_name, "w") as fi:
                fi.write(response.text)

            import html2text
            text = html2text.html2text(response.text)
            txt_base_path = f"./txt/{today_date_component}"
            os.makedirs(txt_base_path, exist_ok=True)
            text_file_name = article_name.replace("html", "txt")
            with open(text_file_name, "w") as txt_fi:
                txt_fi.write(dispose_text(text))

            pdf_base_path = f"./pdf/{today_date_component}"
            os.makedirs(pdf_base_path, exist_ok=True)
            convert_txt_to_pdf(text_file_name, article_name.replace("html", "pdf").title())


def send_news_to_email():
    pass


def customized_nyt_service():
    home_page = get_home_page()
    article_urls = get_article_urls(home_page)
    print(article_urls)
    for article in article_urls:
        get_and_save_each_article(article)
        time.sleep(2)


def get_and_save_specific_article(article_url, s=s):
    # print(datetime.datetime.now())
    today = datetime.datetime.now()
    delta = datetime.timedelta(days=-1)
    yesterday = today + delta
    # date_component = datetime.datetime.now().strftime("%Y/%m/%d")
    yesterday_date_component = str(yesterday.strftime("%Y/%m/%d"))
    today_date_component = str(today.strftime("%Y/%m/%d"))
    response = s.get(article_url, verify=False, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        import os
        article_name_base_path = f"./html/{today_date_component}"
        os.makedirs(article_name_base_path, exist_ok=True)
        article_name = article_name_base_path + "/" + get_article_title(article_url)
        with open(article_name, "w") as fi:
            fi.write(response.text)


# customized_nyt_service()

# TODO
"""
pack up the program to an executable program
create a scheduled task to download new articles.
"""

if __name__ == "__main__":
    # customized_nyt_service()
    get_and_save_specific_article("https://www.nytimes.com/2024/07/05/business/media/stephanopoulos-biden-interview.html")