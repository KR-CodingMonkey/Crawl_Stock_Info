import scrapy


class StockscraperItem(scrapy.Item):

    stock_code = scrapy.Field() # 종목코드
    stock_name = scrapy.Field()
    # max_price = scrapy.Field() # 최고가
    # min_price = scrapy.Field() # 최저가
    current_price = scrapy.Field() # 현재가
    fluctuation_rate = scrapy.Field() # 시가대비 상승률
    trading_volume = scrapy.Field() # 거래량
    foreigner_investor=scrapy.Field()
    created_at = scrapy.Field() # 데이터를 읽어온 시간
    foreigner_investor = scrapy.Field()

