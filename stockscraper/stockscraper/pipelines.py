# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class StockscraperPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDB(item)
        print('----')
        return item

    def storeInDB(self, item):
        title = item.get('title','').strip()
        Quantity = item.get('Quantity','').strip()
        Price = item.get('Price','').strip()
        Low_High_Price = item.get('Low_High_Price','').strip()


        sql = "INSERT INTO my_stock(id,title,Quantity,Price,l_h_Price,create_at) VALUES (null,%s,%s,%s,%s,NOW())"

        self.cur.execute(sql, (title,Quantity,Price,Low_High_Price))
        print('Data stored in DB')

        self.conn.commit()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='mydb',charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")

    def createTable(self):
        # self.cur.execute("DROP TABLE IF EXISTS my_stock")

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS my_stock(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            price VARCHAR(100),
            l_h_price varchar(100),
            Quantity VARCHAR(100),
            create_at VARCHAR(100))
        ''')
