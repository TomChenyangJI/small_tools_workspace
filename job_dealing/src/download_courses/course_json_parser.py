from configs import PROJECT_BASE_DIRECTORY


def course_json_file_parser(json_file_path='./jsons/course_info.json'):
    import json

    with open(json_file_path, "r") as fi:
        obj = json.load(fi)
    video_file_urls = []
    chapters = obj.get('data').get('children')
    for chapter in chapters:
        # definitions = chapter.get("definitions")
        # videoUrl = definitions.get("videoUrl")
        # print(videoUrl)
        children_inner_children = chapter.get("children")  # this is a list obj
        for child in children_inner_children:  # maybe I should write a recursive function to get the nested urls
            child_children = child.get("children")  # this is also a list obj
            for child_inner_child in child_children:
                definitions = child_inner_child.get("definitions")
                videoUrl = definitions.get("videoUrl")
                or_url = definitions.get('url')  # this is the same as videoUrl
                m3u8_url = videoUrl or or_url
                if m3u8_url:
                    if m3u8_url.startswith("http"):
                        video_file_urls.append(m3u8_url)
                # print(m3u8_url)
    return video_file_urls


def get_all_children(obj, all_children):
    if type(obj) is dict:
        for key, val in obj.items():
            if key == "definitions":
                if type(val) is dict:
                    temp_url = val.get("videoUrl") or val.get('url')
                    if temp_url and type(temp_url) is str and temp_url.startswith("http"):
                        all_children.append(temp_url.strip())
            elif key == "children" or type(val) in [dict, list]:
                get_all_children(val, all_children)
    elif type(obj) is list:
        for ele in obj:
            get_all_children(ele, all_children)


def get_all_video_urls(obj, all_urls):
    if type(obj) is dict:
        for key, val in obj.items():
            if ((key == "high_url" and type(val) is str and "m3u8" in val) or
                    (key == "videoUrl" and type(val) is str and "m3u8" in val)):
                if val not in all_urls:
                    all_urls.append(val)
            elif type(val) in [dict, list]:
                get_all_video_urls(val, all_urls)

    elif type(obj) is list:
        for ele in obj:
            get_all_video_urls(ele, all_urls)


def course_full_json_file_parser(
        json_file_path=f"{PROJECT_BASE_DIRECTORY}/test_script/jsons/course_info3.json"):
    import json
    with open(json_file_path, "r") as fi:
        obj = json.load(fi)
    urls = []
    get_all_children(obj, urls)
    if len(urls) == 0:
        get_all_video_urls(obj, urls)
    print("the len of urls is ", len(urls), urls)
    return urls

# course_full_json_file_parser()
