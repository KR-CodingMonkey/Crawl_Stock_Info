import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup


def getDataOfParam(param):
    sub_tbody = sub_soup.find("table", attrs={"class": "tb_type1 tb_num tb_type1_ifrs"}).find("tbody")
    sub_title = sub_tbody.find("th", attrs={"class": param}).get_text().strip()
    dataOfParam = sub_tbody.find("th", attrs = {"class":param}).parent.find_all("td")
    value_param = [i.get_text().strip() for i in dataOfParam] # 실질적으로 불러오는 값
    # print(sub_title, " : ",value_param[0:3])

    for idx in range(0, 3):
        if value_param[idx] == '' or value_param[idx] == '-':
            value_param[idx] = '-'

    return value_param[0:3]

# csv 파일 종목 가젹오기
def Read_csv_stock():
    f = open('stock_code_200.csv', 'r')
    write_csv = csv.reader(f)
    csv_stocks = list(write_csv)[0]
    f.close()

    return csv_stocks

# main 시작
csv_stocks = Read_csv_stock()
all_stock_info = {}

# csv_stocks = [005930, 000660,051910,035420,005380,207940,006400 .... ]
for stock in csv_stocks:
    link = 'https://finance.naver.com//item/main.nhn?code=' + stock
    # print(link)
    sub_res = requests.get(link)
    sub_soup = BeautifulSoup(sub_res.text, 'lxml')

    print()
    print('stock Num :', stock)
    stock_info = [] 
    ParamList = ['매출액', '영업이익', '당기순이익', 'ROE(지배주주)', 'PER(배)', 'PBR(배)']
    for idx, pText in enumerate(ParamList):

        try:
            param = " ".join(sub_soup.find('strong', text=pText).parent['class'])
            values = getDataOfParam(param)
            stock_info += values

        except:
            stock_info += ['-', '-', '-']
    
    print(stock_info)
    all_stock_info[stock] = stock_info

data = pd.DataFrame(all_stock_info, index = ['매출액-1', '매출액-2', '매출액-3', '영업이익-1', '영업이익-2', '영업이익-3', '당기순이익-1', '당기순이익-2', '당기순이익-3', 'ROE(지배주주)-1', 'ROE(지배주주)-2', 'ROE(지배주주)-3', 'PER(배)-1', 'PER(배)-2', 'PER(배)-3', 'PBR(배)-1', 'PBR(배)-2', 'PBR(배)-3'])
data=data.T

data.to_csv("./financial_statement.csv")
print(data)