import pymysql
import pandas as pd
import numpy as np
from operator import itemgetter
import time
import datetime

flunctuation_data=[] # DB에서 불러온 상위 10개 종목
stock_list = [] # 종목 담는 리스트

# DB연결 데이터 불러오기
def Connect_DB():
    connect = pymysql.connect(host='skuser39-instance.cpeexjfrdqsn.us-east-2.rds.amazonaws.com', user='admin', password='sky45741', db='mydb',charset='utf8mb4')
    cur = connect.cursor()

    query = "SELECT stock_code, stock_name, fluctuation_rate, trading_volume, max(created_at) from my6_stock_table GROUP BY stock_code"
    cur.execute(query)
    datas = cur.fetchall()

    return datas

# 상위 10개 종목 선정하기
def Choice_Stock(datas):

    for data in datas:
        data = list(data)
        flunctuation_data.append(data)

    for n in range(len(flunctuation_data)):
        flunctuation_data[n][3]=int(flunctuation_data[n][3])
        flunctuation_data[n][2]=float(flunctuation_data[n][2].replace("%",""))
        flunctuation_data[n][4]=datetime.datetime.fromtimestamp(int(flunctuation_data[n][4])).strftime('%Y-%m-%d %H:%M:%S')

    flunctuation_data.sort(key=itemgetter(2),reverse=True)

    for i in flunctuation_data[:10]:
        stock_list.append(i[0])

    return stock_list

# 선정된 종목을 재무제표에서 분석
def Analysis_Data(stocks):
    new_stock_list = [] # stock_list -> float 형변환
    stock_info = []

    data = pd.read_csv('./financial_statement.csv')
    data = pd.DataFrame(data)

    # stock:문자열 -> 실수형 바꿔주기
    for stock in stocks:
        new_stock_list.append(float(stock))

    # 데이터 전처리
    data = data.replace('-', 0)
    data = data.replace('(.*),(.*)',r'\1\2', regex=True)
    data = data.replace('(.*),(.*)',r'\1\2', regex=True)
    data = data.astype(float)

    data['Total ROE(지배주주)'] = data[['ROE(지배주주)-1', 'ROE(지배주주)-2', 'ROE(지배주주)-3']].mean(axis=1).round(3)
    data['Total PER(배)'] = data[['PER(배)-1', 'PER(배)-2', 'PER(배)-3']].mean(axis=1).round(3)
    data['Total PBR(배)'] = data[['PBR(배)-1', 'PBR(배)-2', 'PBR(배)-3']].mean(axis=1).round(3)
    data['평가'] = 'bad fit'

    for i, row in data.iterrows():
        if data.at[i, 'Total ROE(지배주주)'] >= 10 and data.at[i, 'Total PER(배)'] < 30 and data.at[i, 'Total PBR(배)'] < 5:
            data.at[i, '평가'] = 'good fit'

        else:
            pass

    # print(data)
    # data.to_csv("./analysis_data.csv")

    for stock in new_stock_list:
        result = data[(data['종목코드'] == stock) & (data['평가'] == 'good fit')]
        if not result.empty:
            stock_info.append(result.values.tolist()[0])
            # print(result.values.tolist()[0])

    return stock_info
    
### main 
datas = Connect_DB()
stocks = Choice_Stock(datas)
stock_info = Analysis_Data(stocks)

# 종목코드,매출액-1,매출액-2,매출액-3,영업이익-1,영업이익-2,영업이익-3,당기순이익-1,당기순이익-2,당기순이익-3,ROE(지배주주)-1,ROE(지배주주)-2,ROE(지배주주)-3,PER(배)-1,PER(배)-2,PER(배)-3,PBR(배)-1,PBR(배)-2,PBR(배)-3
for i in stock_info:
    print(i)


