import time
import os

try:
    from fanficserver.fanfic_database import FanFicDatabase
    from fanficserver.downloader import *
except:
    from fanfic_database import FanFicDatabase
    from downloader import *

fdb = FanFicDatabase()
if __name__ == '__main__':
    while (True):
        download_data = fdb.get_fics_to_download()
        print(download_data)
        if (len(download_data) > 0):
            key1 = list(download_data.keys())[0]
            fic_url = download_data[key1]['url']
            my_email = "dylanb5402@gmail.com"
            # kindle_email = "dylanb5402@kindle.com"
            kindle_email = "d.barva5402@gmail.com"
            my_password = ""
            try:
                my_password = os.environ['KINDLE_PASSWORD']
            except:
                import password
                my_password = password.password
            send_fic(fic_url, my_email, my_password, kindle_email)
            fdb.delete_fic_from_downloads(key1)
        print('---------------')
        time.sleep(5)

    
    
