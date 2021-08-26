import requests as r
import json
import pandas as pd
from datetime import datetime, date 
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

url = "https://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?response=json&date=20210826"

# 下載一日大盤走勢
def get_stock_daily(year,month,day):
    stock_date = str(date(year,month,day).strftime("%Y%m%d"))
    df = pd.DataFrame()
    url = "https://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?response=json&date="+ stock_date
    res = r.get(url)
    stock_json = res.json()
    stock_df = pd.DataFrame.from_dict(stock_json['data'])
    df = df.append(stock_df, ignore_index=True)
    df.columns = stock_json['fields']
    return df

# 畫出一日大盤K線圖
def daily_k_plot(day):
    # day format: '2021/08/26'
    d = list(map(int,day.split('/')))
    try:
        daily_stock = get_stock_daily(d[0],d[1],d[2])
        for row in range(daily_stock.shape[0]):
            daily_stock.iloc[row,1] = float(daily_stock.iloc[row,1].replace(',',''))
        daily_stock = daily_stock[['時間','發行量加權股價指數']]
        high_price = max(daily_stock['發行量加權股價指數'])
        low_price = min(daily_stock['發行量加權股價指數'])
        open_price = daily_stock['發行量加權股價指數'].iloc[1]
        close_price = daily_stock['發行量加權股價指數'].iloc[-1]
        data = {
            'Date': [day],
            'Open': open_price,
            'High': [high_price],
            'Low' : [low_price],
            'Close': [close_price]
        }

        df = pd.DataFrame(data)

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
        open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'],
        increasing_line_color='red', decreasing_line_color='green' )])
        fig.update_layout(xaxis_rangeslider_visible=False)
        return df,fig,daily_stock
    except:
        print("請輸入一個開盤日,你目前輸入的日期並沒有交易")
        return None

# 下載多日大盤走勢資料
# 資料來源: 證卷交易所 發行量加權股價指數歷史資料 https://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html
def get_stock_base_data(start_year, start_month, end_year, end_month):
    start_date = str(date(start_year,start_month,1))
    end_date = str(date(end_year,end_month,1))
    month_list = pd.date_range(start_date,end_date,freq='MS').strftime('%Y%m%d').tolist()
    print(month_list)
    df = pd.DataFrame()
    for month in month_list:
        try:
            url = "https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=" + month 
            res = r.get(url)
            stock_json = res.json()
            stock_df = pd.DataFrame.from_dict(stock_json['data'])
            df = df.append(stock_df, ignore_index=True)
        except:
            print(f"抓取 {month} 資料有錯!!")
    df.columns = ['Date','Open','High','Low','Close']
    return df

def month_k_plot(start_year, start_month, end_year, end_month):
    stock = get_stock_base_data(start_year= start_year, start_month= start_month, end_year=end_year, end_month= end_month)
    for col in range(1,5):
        for row in range(stock.shape[0]):
            stock.iloc[row,col] = float(stock.iloc[row,col].replace(',',''))
    fig = go.Figure(data=[go.Candlestick(x=stock['Date'],
    open=stock['Open'],high=stock['High'],low=stock['Low'],close=stock['Close'],
    increasing_line_color='red', decreasing_line_color='green')])
    return fig


def run():
    # 畫出當日大盤的走勢,作為K線圖的參考
    daily_stock = get_stock_daily(2021,8,26)    
    #print(daily_stock)
    # 時間  發行量加權股價指數  未含金融保險股指數    未含電子股指數  未含金融電子股指數   水泥類指數     食品類指數  ... 建材營造類指數   航運
    # 類指數   觀光類指數   金融保險類指數 貿易百貨類指數 油電燃氣類指數   其他類指數
    daily_stock = daily_stock[['時間','發行量加權股價指數']]
    for row in range(daily_stock.shape[0]):
        daily_stock.iloc[row,1] = float(daily_stock.iloc[row,1].replace(',',''))
    #print(daily_stock.head())
    fig = plt.figure(figsize=(20,5))
    plt.plot(daily_stock["發行量加權股價指數"], color='red')
    plt.title("2021-08-26 Daily Stock")
    plt.show()

def run2():
    # 畫出當日大盤的走勢,作為K線圖的參考
    daily_stock = get_stock_daily(2021,8,26)       
    daily_stock = daily_stock[['時間','發行量加權股價指數']]
    for row in range(daily_stock.shape[0]):
        daily_stock.iloc[row,1] = float(daily_stock.iloc[row,1].replace(',',''))
    # 計算出畫K線圖需要的開盤價|收盤價|最高價|最低價
    high_price = max(daily_stock['發行量加權股價指數'])
    low_price = min(daily_stock['發行量加權股價指數'])
    open_price = daily_stock['發行量加權股價指數'].iloc[1]
    close_price = daily_stock['發行量加權股價指數'].iloc[-1]
    data = {
        'Date': ['2021/08/26'],
        'Open': open_price,
        'High': [high_price],
        'Low' : [low_price],
        'Close': [close_price]
    }
    daily_k = pd.DataFrame(data)
    #print(daily_k)
    df = daily_k

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
    open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'],
    increasing_line_color='red', decreasing_line_color='green' )])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()


def run3():
    data = daily_k_plot('2021/08/26')
    if data != None:
        print(data[0])
        fig = go.Figure(data=data[1])
        fig.update_layout(xaxis_rangeslider_visible=False)
        fig.show()
        #print(data[1])

def run4():
    data = daily_k_plot('2021/08/26')
    #data = daily_k_plot('2020/12/19')
    if data != None:
        df = data[2]
        fig = plt.figure(figsize=(18,5))
        plt.plot(df["發行量加權股價指數"], color='red')
        plt.title("2021-08-26 Daily Stock")
        plt.show()

def run5():
    #stock = get_stock_base_data(start_year=2020,start_month=1,end_year=2021,end_month=8)
    stock = get_stock_base_data(start_year=2021,start_month=1,end_year=2021,end_month=8)
    for col in range(1,5):
        for row in range(stock.shape[0]):
            stock.iloc[row,col] = float(stock.iloc[row,col].replace(',',''))
    #print(stock.head())
    fig = go.Figure(data=[go.Candlestick(x=stock['Date'],
    open=stock['Open'],high=stock['High'],low=stock['Low'],close=stock['Close'],
    increasing_line_color='red', decreasing_line_color='green')])
    fig.show()

def run6():
    figdata = month_k_plot(start_year=2020,start_month=1,end_year=2021,end_month=8)
    if figdata != None:
        fig = go.Figure(data=figdata)
        fig.update_layout(xaxis_rangeslider_visible=False)
        fig.show()

if __name__ == '__main__':
    run6()
