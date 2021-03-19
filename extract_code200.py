import urllib.request
import re
import csv
import pandas as pd

stock_list = []

for i in range(21):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page={}".format(i+1)
    html = urllib.request.urlopen(url)
    html_contents = str(html.read().decode("ms949")) # 디코딩


    # print(html_contents)
    stock_results = re.findall("(\<td class=\"ctg\"\>)([\s\S]+?)(\<\/td\>)", html_contents)

    # print(stock_results)
   
    for i in range(len(stock_results)):
        my_stock = stock_results[i][1]
        # print(my_stock)

        stock_number = re.findall("(code\=)([\s\S]+?)(\")", my_stock)
        stock_list.append(stock_number[0][1])
    
new_list = []
for i in stock_list:
    new_list.append(i)

# print(new_list)
f = open('stock_code_200.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(new_list)
f.close()