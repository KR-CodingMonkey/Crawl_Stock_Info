import schedule
import time
import os

def job():
    path = "C:\\Users\\ahipp\\work\\my_scraping\\stockscraper\\stockscraper"
    os.system('cd {}'.format(path))
    os.system('scrapy crawl stock_bots')

schedule.every(20).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
