
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockscraperPipeline:

    def __init__(self):
        self.setup_DB_Connect()
        self.Create_Table()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item:dict):
        # 각 아이템을 Table에 저장
        stock_num = item.get('stock_num', '').strip()
        max_price = item.get('max_price', '').strip()
        min_price = item.get('min_price', '').strip()
        current_price = item.get('current_price', '').strip()
        trading_volume = item.get('trading_volume').strip()
        created_at = item.get('created_at').strip()

        insert_sql = '''
        INSERT INTO stock_table(stock_num, max_price, min_price, current_price, trading_volume, created_at) VALUES(%s, %s, %s, %s, %s, %s)
        '''

        values = (stock_num, max_price, min_price, current_price, trading_volume, created_at)
        # print('---------------------------------------')

        self.cur.execute(insert_sql, values)
        print('Data stored in DB')
        self.conn.commit()

    def setup_DB_Connect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='', port=13306, db='stock_db', charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")

    def Create_Table(self):

        # 테이블이 없을 경우 새로 생성
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_table(
            id INT AUTO_INCREMENT PRIMARY KEY,
            stock_num VARCHAR(10),
            max_price VARCHAR(10),
            min_price VARCHAR(10),
            current_price VARCHAR(10),
            trading_volume VARCHAR(20),
            created_at VARCHAR(30))
        ''')