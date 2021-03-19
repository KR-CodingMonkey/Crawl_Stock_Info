import scrapy
import csv
from stockscraper.items import StockscraperItem
# from datetime import datetime
import re
import time

# 문자열 공백 제거
def Remove_space(descs):
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0 :
            result.append(descs[i].strip())
            
    return result

class StockBotsSpider(scrapy.Spider):
    name = 'stock_bots'

    allowed_domains = ['finance.naver.com']
    start_urls = []

    # csv 파일 읽기
    def Read_csv_stock(self):
        f = open('stock_code_200.csv', 'r')
        write_csv = csv.reader(f)
        self.csv_stocks = list(write_csv)[0]
        f.close()

    def start_requests(self):
        self.Read_csv_stock()
        
        base_url = 'https://finance.naver.com/item/sise.nhn?code='
        for csv_stock_code in self.csv_stocks:
            self.start_urls = base_url + csv_stock_code
            yield scrapy.Request(url=self.start_urls, callback=self.parse)

    def parse(self, response):

        stock_name = response.xpath('//*[@id="middle"]/div[1]/div[1]/h2/a/text()').extract()
        stock_code = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        current_price = response.xpath('//*[@id="_nowVal"]/text()').extract()
        trading_volume = response.xpath('//*[@id="_quant"]/text()').extract()

        fluctuation_rate = response.xpath('//*[@id="_rate"]/span/text()').extract()
        fluctuation_rate = Remove_space(fluctuation_rate)
        foreigner_investor = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[13]/td[1]/span/span/text()').extract()

        # now = datetime.now()
        # created_at = now.strftime('%Y-%m-%d %H:%M:%S')
        created_at = str(int(time.time()))

        items = []
        for idx in range(len(stock_name)):
            item = StockscraperItem()
            item['stock_name'] = stock_name[idx]
            item['stock_code'] = stock_code[idx]
            item['current_price'] = current_price[idx]
            item['fluctuation_rate'] = fluctuation_rate[idx]
            item['trading_volume'] = trading_volume[idx]
            item['foreigner_investor'] = foreigner_investor[idx]
            item['created_at'] = created_at

            items.append(item)

        print(items)
        return items

