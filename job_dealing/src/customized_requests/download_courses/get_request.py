import time

from overwrite_get_method import get_request
from to_update_request_params import *


def url_downloader(url, output="", response=None, new_cookies="./cookies.json", recursive_count=0, jsondata=None, params=None):
    """
    to download the url, using recursive call
    :param url: url
    :param output: the directory where the response content will be saved
    :param response: in order to use the recursive call of this function
    :param new_cookies: the path to the new_cookies_json file
    :return: the response to the url get request
    """
    recursive_count += 1
    if response is None or ('Log in with a  account.' in response.text or '"errorCode":"1000"' in response.text):
        try:
            # first, try to use the existing cookies to make get request
            response = get_request(url, output, new_cookies, jsondata=jsondata, params=params)
        except Exception as e:
            get_and_save_new_cookies(new_cookies)
            time.sleep(1)
            if recursive_count <= 5:
                url_downloader(url, output, response, new_cookies, recursive_count, jsondata, params=params)
            else:
                print(e)
                print("Above exception happened. I cannot handle it, you need to intervene in this business.")
                return None

        if 'Log in with a  account.' in response.text or '"errorCode":"1000"' in response.text:
            # first, update the request headers and cookies, etc.
            get_and_save_new_cookies(new_cookies)
            time.sleep(1)
            # get method called
            response = get_request(url, output, new_cookies, jsondata=jsondata, params=params)
            if recursive_count > 5:
                print("I cannot download this url, you need to intervene in this business.")
                return None
            return url_downloader(url, output, response, new_cookies, recursive_count, jsondata, params=params)
        else:
            return response
    else:
        return response

