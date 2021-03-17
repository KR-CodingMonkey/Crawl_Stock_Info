import schedule
import time
import os

def job():
    # path = "C:\\Users\\ahipp\\work\\my_scraping\\stockscraper\\stockscraper"
    path = "C:\\Users\\ahipp\\OneDrive\\바탕 화면\\GitHub\\Module_Team_Project\\Module_Team_Project\\stockscraper\\stockscraper\\"
    os.system('cd {}'.format(path))
    os.system('scrapy crawl stock_bots')

# schedule.every(30).seconds.do(job)
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
