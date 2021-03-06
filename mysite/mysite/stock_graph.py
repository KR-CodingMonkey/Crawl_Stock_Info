import pymysql
from operator import itemgetter
import time
import datetime 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Connect_DB(stock_code):
    connect = pymysql.connect(host='skuser39-instance.cpeexjfrdqsn.us-east-2.rds.amazonaws.com', user='admin', password='sky45741', db='mydb',charset='utf8mb4')
    cur = connect.cursor()

    query1 = "SELECT stock_code, stock_name, trading_volume, created_at, current_price from my6_stock_table where stock_code = %s"
    cur.execute(query1, (stock_code,))
    datas = cur.fetchall()

    cur.close()
    connect.close()

    return datas

def Draw_Graph(datas, mode:int):

    flunctuation_data=[]

    for data in datas:
        data = list(data)
        flunctuation_data.append(data)
    
    if mode == 1: # 특정 종목 그래프 보기   
        stock_code = flunctuation_data[0][0]
        plot1_volume=[] 
        plot1_price=[]
        plot1_date=[]
        
        for n in range(len(flunctuation_data)):
            plot1_volume.append(int(flunctuation_data[n][2]))
            plot1_price.append(flunctuation_data[n][4])
            str_time = datetime.datetime.fromtimestamp(int(flunctuation_data[n][3]))
            str_time = str(str_time.hour) + ':' + str(str_time.minute)
            plot1_date.append(str_time)

        # print(plot1_volume)
        x_tick = np.arange(0, 100, 4)

        fig = plt.figure(figsize=(10,8))

        # graph 1
        ax1 = fig.add_subplot(2,1,1)
        ax1.plot(plot1_date, plot1_volume, color='red', label= 'volume')
        plt.xticks(x_tick, rotation = 45, fontsize = 'small')
        plt.yticks(fontsize = 'small') # y축 폰트 사이즈 설정
        plt.ylabel('Volume')
        plt.grid(True, alpha = 0.5, linestyle='--') # grid
        plt.title(stock_code, loc='right')

        # graph 2
        ax2 = fig.add_subplot(2,1,2)
        ax2.plot(plot1_date, plot1_price, color='darkblue',label= 'Price')
        plt.xticks(x_tick, rotation = 45, fontsize = 'small')
        plt.yticks(fontsize = 'small')
        plt.grid(True, alpha = 0.5, linestyle='--') # grid
        plt.xlabel('Date Time')
        plt.ylabel('price')

        plt.subplots_adjust(hspace=0.35)
        plt.show()
        # plt.savefig('{}.png'.format(stock_code))
        graph_name = stock_code + '.png'

        return graph_name

def Trade_Rank():
    flunctuation_data=[] # DB에서 불러온 상위 10개 종목

    # DB연결 데이터 불러오기
    # def Connect_DB():
    connect = pymysql.connect(host='skuser39-instance.cpeexjfrdqsn.us-east-2.rds.amazonaws.com', user='admin', password='sky45741', db='mydb',charset='utf8mb4')
    cur = connect.cursor()

    query = "SELECT stock_code, stock_name, fluctuation_rate, max(trading_volume), created_at from my_stock_table GROUP BY stock_code"
    cur.execute(query)
    datas = cur.fetchall()

    for data in datas:
        data = list(data)
        flunctuation_data.append(data)

    for n in range(len(flunctuation_data)):
        flunctuation_data[n][3]=int(flunctuation_data[n][3])

    flunctuation_data.sort(key=itemgetter(3),reverse=True)

    stocks = []
    volumes = []
    for stock in flunctuation_data[:5]:
        stocks.append(stock[0])
        volumes.append(stock[3])

    fig = plt.figure()
    # graph 1
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(stocks, volumes, color='darkblue', label= 'volume', align = 'center')
    # plt.xticks(x_tick, rotation = 45, fontsize = 'small')
    plt.yticks(fontsize = 'small') # y축 폰트 사이즈 설정
    plt.xticks(fontsize = 'small') # y축 폰트 사이즈 설정
    plt.ylabel('Volume')
    plt.xlabel('Stock Code')
    plt.grid(True, alpha = 0.5, linestyle='--') # grid
    plt.title('Rank', loc='right')

    # plt.show()
    plt.savefig('trade_rank.png')
    graph_name = 'trade_rank.png'

    return graph_name
    # return stocks, volumes

## main
def My_Graph(stock_code):
    datas = Connect_DB(stock_code)
    graph_name = Draw_Graph(datas, 1)
    return graph_name
# My_Graph('352820')