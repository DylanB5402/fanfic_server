import sqlite3
from enum import Enum


class SQLiteFicQueue:

    def __init__(self) -> None:
        con = sqlite3.connect("fics.db", check_same_thread=False)
        self.cur = con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS fic_queue (priority INTEGER PRIMARY KEY, url TEXT, status TEXT);')

    def push(self, url):
        self.cur.execute('INSERT INTO fic_queue (url, status) VALUES (?, ?);', (url, str(FicQueueStatus.NOT_DOWNLOADED)))

    def pop(self):
        url = self.cur.execute('SELECT url FROM fic_queue WHERE status = (?) ORDER BY priority;', (str(FicQueueStatus.NOT_DOWNLOADED), )).fetchone()[0]
        self.cur.execute('UPDATE fic_queue SET status = (?) WHERE url = (?);', (str(FicQueueStatus.DOWNLOADED), url))
        return url

    def get_num_downloaded_fics(self):
        return len(self.cur.execute('SELECT * FROM fic_queue;').fetchall())

    def close(self):
        self.cur.close()
        self.con.close()

    def print_db(self):
        print(self.cur.execute('SELECT * FROM fic_queue;').fetchall())

class FicQueueStatus(Enum):
    NOT_DOWNLOADED = 1
    DOWNLOADED = 2

# queue = SQLiteFicQueue()
# queue.push('cheese')
# queue.push('taco')
# queue.push('bruh')
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# queue.print_db()

