import time

try:
    from fanficserver.fanfic_database import FanFicDatabase
except:
    from fanfic_database import FanFicDatabase

fdb = FanFicDatabase()
if __name__ == '__main__':
    while (True):
        download_data = fdb.get_fics_to_download()
        print(download_data)
        if (len(download_data) > 0):
            key1 = list(download_data.keys())[0]
            print(key1)
            fdb.delete_fic_from_downloads(key1)
        print('---------------')
        time.sleep(5)

    
    
