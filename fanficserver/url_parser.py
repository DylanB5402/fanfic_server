import random

def get_id_str(url : str) -> str:
    if ("fanfiction.net" in url):
        # print('ffn')
        id = url[-8:]
        id = id.replace('/', '')
        return 'ffn_' + id
    elif("archive" in url):
        # print('ao3')
        if ("chapters" in url):
            id = url[34:42]
            return 'ao3_' + id
        else:
            return 'ao3_' + url[34:]
    else:
        return str(random.randint(1, 100000))

# print(get_id_str("https://www.fanfiction.net/s/11824953/"))
# print(get_id_str("https://archiveofourown.org/works/21809323/chapters/52043659"))