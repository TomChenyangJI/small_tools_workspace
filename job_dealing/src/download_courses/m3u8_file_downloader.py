def download_m3u8_file(uri, output_path="test2_m3u8.m3u8"):
    from web_spider_test.image_downloader.src import configs
    cfg = configs.__dict__
    for key, val in cfg.items():
        if key.startswith("config"):
            response = cfg.get('request_get')(
                uri, val)
            if response.status_code == 200:
                with open(output_path, "wb") as fi:
                    fi.write(response.content)
                print(f"{uri} has been downloaded!")
                break
            else:
                print(response.status_code, " is the status code.")
