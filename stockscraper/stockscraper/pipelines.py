from kafka import KafkaProducer
from json import dumps
import time

class StockscraperPipeline(object):

    def __init__(self):
        self.producer = KafkaProducer(acks=0,
                                      compression_type='gzip',
                                      bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))

    def process_item(self, item, spider):
        item = dict(item)
        
        item["current_price"] = item["current_price"].replace(",", "")
        item["foreigner_investor"] = item["foreigner_investor"].replace(",", "")
        item["trading_volume"] = item["trading_volume"].replace(",", "") 

        if len(item["trading_volume"]) <= 10:
            add_zero_count = 10 - len(item["trading_volume"])
            add_zero_str = '0' * add_zero_count
            item["trading_volume"] = add_zero_str + item["trading_volume"]

        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":False,"field":"id"},{"type":"string","optional":True,"field":"stock_code"},{"type":"string","optional":True,"field":"stock_name"},{"type":"string","optional":True,"field":"current_price"},{"type":"string","optional":True,"field":"fluctuation_rate"},{"type":"string","optional":True,"field":"created_at"},{"type":"string","optional":True,"field":"foreigner_investor"},{"type":"string","optional":True,"field":"trading_volume"}],"optional":False,"name":"my_stock_table"}, "payload":{"id":2,"stock_code":item['stock_code'],"stock_name":item['stock_name'],"current_price":item['current_price'],"fluctuation_rate":item['fluctuation_rate'],"created_at":item['created_at'],"foreigner_investor":item['foreigner_investor'],"trading_volume":item['trading_volume']}}

        self.producer.send("my6_stock_table", value=data)
        # time.sleep(0.3)
        self.producer.flush()