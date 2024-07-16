home_cookies = {
    
}

track_cookies = {
    
}

article_cookies = {
}


def compare_cookies(c1, c2):
    c1_keys = c1.keys()
    c2_keys = c2.keys()
    for key in c1_keys:
        if key in c2_keys:
            if c1.get(key) == c2.get(key):
                pass
            else:
                print(f"same key: {key}, different value: 1 >>> ", c1.get(key), "    <><><><><> 2 >>>", c2.get(key))
        else:
            print("key in c1 but not in c2, ", key, ":", c1.get(key))
    for key in c2_keys:
        if key not in c1_keys:
            print("key in c2 but not in c1, ", key, ":", c2.get(key))


compare_cookies(home_cookies, article_cookies)
