import sqlite3
from itemadapter import ItemAdapter

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('admissions.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS jbcrc_notices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT,
                date TEXT,
                category TEXT,
                year TEXT,
                source TEXT,
                crawl_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cur.execute('''
            INSERT INTO jbcrc_notices (title, url, date, category, year, source)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            adapter['title'],
            adapter['url'],
            adapter['date'],
            adapter['category'],
            adapter['year'],
            adapter['source']
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
