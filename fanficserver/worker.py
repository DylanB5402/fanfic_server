import time

try:
    from fanficserver.fanfic_database import FanFicDatabase
except:
    from fanfic_database import FanFicDatabase

fdb = FanFicDatabase()
if __name__ == '__main__':
    while (True):
        print(fdb.get_all_fics())
        print('---------------')
        time.sleep(2)

    
    
