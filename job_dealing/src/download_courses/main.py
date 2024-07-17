import json
import time

from get_request import url_downloader
from web_spider_test.image_downloader.src.video_downloader import process_function


def get_val_of_key_in_response(dictionary, target="resourceApplyId"):
    if dictionary is None:
        return None
    elif isinstance(dictionary, dict):
        if target in dictionary.keys() and dictionary.get(target) is not None:
            return dictionary.get(target)
        for k, v in dictionary.items():
            if type(v) in [dict, list]:
                return_val = get_val_of_key_in_response(v, target)
                if return_val is not None:
                    return return_val
        return None
    elif isinstance(dictionary, list):
        for ele in dictionary:
            return_val = get_val_of_key_in_response(ele, target)
            if return_val is not None:
                return return_val
        return None
    else:
        return None


def get_m3u8_json_file_from_search(code, resourceApplyId_url="https://example.com/"):
    time.sleep(2)
    resourceApplyId_url = (f"{resourceApplyId_url}?code={code}&courseId=")
    applyId_response = url_downloader(resourceApplyId_url)
    # print(">>>>:  ", applyId_response.text)
    # now process it and find the resourceApplyId from the response
    applyId_response = json.loads(applyId_response.text)
    # print(applyId_response)
    resourceApplyId = get_val_of_key_in_response(applyId_response, "resourceApplyId")
    print(">>>> course id: ", resourceApplyId)
    title = get_val_of_key_in_response(applyId_response, "title")
    time.sleep(3)
    m3u8_url = (f"https://{resourceApplyId_url}/{resourceApplyId}?all=true&filterType=video")
    m3u8_json = url_downloader(m3u8_url)
    # print(">>>> : : ", m3u8_json.text)
    return m3u8_json


def get_m3u8_json_file_from_search2(course_key):
    time.sleep(2)
    course_key_url = (f"{resourceApplyId_url}%3A{course_key}&nav_depth=3&requested_fields=")
    course_key_response = url_downloader(course_key_url)  # this is the file with m3u8 urls
    # course_key_response = json.loads(course_key_response.text)

    return course_key_response


def get_all_val_of_key_in_response(response, target, result: list):
    if response is None:
        return
    elif isinstance(response, dict):
        for key in response.keys():
            if key == target and response.get(key) is not None:
                result.append(response.get(key))
            elif isinstance(response.get(key), dict) is not None and (
                    isinstance(response.get(key), dict) or isinstance(response.get(key), list)):
                get_all_val_of_key_in_response(response.get(key), target, result)
    elif isinstance(response, list):
        for ele in response:
            if ele is not None:
                get_all_val_of_key_in_response(ele, target, result)
    return


def get_search_result(search_key):
    content = None
    if search_key is not None:
        search_url = (f"https://example.com/"
                      f"search/all?accuracyType=0&aggType=0&applet=1&pageNum=1&pageSize=5&scopeType=0&"
                      f"subTitleLan=zh&title={search_key}")
        search_response = url_downloader(search_url)
        # with open("temp_response_text.json", "w") as fi:
        #     fi.write(search_response.text)
        search_response_dict = json.loads(search_response.text)
        content = search_response_dict.get('data').get("content")
    return content


def get_course_code(search_content, course_name):
    code = "8086"
    if search_content is not None:
        for obj in search_content:
            title = obj.get("title")
            if title == course_name or course_name in title or title in course_name:  # find the course
                code = obj.get("number").strip()
                break
    return code


def get_course_key(search_content, course_name):
    course_key = None
    if search_content is not None:
        for obj in search_content:
            title = obj.get("title")
            if title == course_name or course_name in title or title in course_name:  # find the course
                course_key = obj.get("key").strip()
                # print(">>> <<<< the code is: ", code)
                break
    return course_key


def download_vid_from_search(search_key, course_name=None):
    time.sleep(2)
    search_content = get_search_result(search_key)
    course_code = get_course_code(search_content, course_name)
    time.sleep(1)

    m3u8_json_response = get_m3u8_json_file_from_search(course_code)  # I need to make this method more robust.
    m3u8_json_dict = json.loads(m3u8_json_response.text)
    if "errorMessage" in m3u8_json_dict.keys() and "errorCode" in m3u8_json_dict.keys():
        # when the error happens, try to use the course key to get the m3u8 files
        # There are two versions of the current database based on my observation.
        # This one is the older version structure, the above one is the new-version structure.
        course_key = get_course_key(search_content, course_name)
        m3u8_json_response = get_m3u8_json_file_from_search2(course_key)  # I need to make this method more robust.
        m3u8_json_dict = json.loads(m3u8_json_response.text)

        m3u8_url2 = (f"https://example.com/?"
                     f"all_blocks=true&block_counts=video&course_id=course-v1%3A{course_key}%2Bmicrocourse&depth=all&"
                     f"nav_depth=3&requested_fields=graded%2Cformat%2Cstart%2Cstudent_view_multi_device&")
        # in this version, I have downloaded the json file and saved it, but I didn't use it.
        m3u8_json = url_downloader(m3u8_url2)

        if "errorMessage" in m3u8_json_dict.keys() and "errorCode" in m3u8_json_dict.keys():
            print(m3u8_json_dict)
            print(">>>>>>>> I cannot handle this situation, please help me out ! <<<<<<<<")
            return

    m3u8_file_name = search_key + ".json"
    m3u8_json_path = ("~/Desktop/web_spider_test/image_downloader"
                      "/test_script/jsons/") + m3u8_file_name
    with open(m3u8_json_path, "w") as fi:
        fi.write(m3u8_json_response.text)

    param = [search_key, m3u8_file_name]
    process_function(param)


def download_vid_from_search_wrapper(params):
    search_key, course_name = params
    if course_name == "":
        course_name = None
    download_vid_from_search(search_key, course_name)


if __name__ == "__main__":
    params = [
        ["communication", "communication"]
    ]
    params_dict = {
        "params1": [
            ["communication", "communication"]
        ]
    }

    # download the videos with the search keys in a list
    for ele in params_dict.get(f"params13"):
        download_vid_from_search_wrapper(ele)
        time.sleep(10)

    # using multiprocessing to speed up downloading the videos.
    # using multiprocessing in this module doesn't work very well
    # because the downloaded video files will be in no order

    # for i in range(5, 6):
    #     with Pool(5) as p:
    #         time.sleep(2)
    #         p.map(download_vid_from_search_wrapper, params_dict.get(f"params{i}"))
    #     time.sleep(10 * 5)

    # download a specific video by searching the name of it.
    # # download_vid_from_search("communication", "communication")

# Note: the coming optimization on this app should be focused on the order of the m3u8 files
# because in this app, when I get m3u8 urls, I didn't pay attention to its real order since I was
# using recursive algorithm to get all the urls in a nested json object.


# find a way to optimize the search key when the search result is none.
# find a blur algorithm to search the name of the course to get the course
