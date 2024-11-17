import datetime as dt
from datetime import timedelta
import requests,smtplib

my_email = "abc@gamil.com" # from which you want to send msg
other_email = "xyz@gmail.com" # to you want to send msg
app_password = "my_pass" # not your email password but generated from google app 



api_key = "my_api_key"
api_stock = "my_api_stock"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


today_date = dt.datetime.now().date()
date_before_yesterday = (today_date - timedelta(days=2)).strftime('%Y-%m-%d')
yesterday_date = (today_date - timedelta(days = 1)).strftime('%Y-%m-%d')



url = ('https://newsapi.org/v2/everything?'
       'q=tesla&'
       f'from={yesterday_date}&'
       'sortBy=popularity&'
       f'apiKey={api_key}')
response = requests.get(url=url)
data_ = response.json()


link = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={api_stock}'
r = requests.get(link)
data = r.json()


open_price = float(data["Time Series (Daily)"][yesterday_date]["1. open"])
closing_price = float(data["Time Series (Daily)"][date_before_yesterday]["4. close"])

updation = ((open_price-closing_price)/closing_price)*100

if open_price < closing_price:
    symbol = "🔻" 
else:
    symbol = "🔺" 

news_list =[]
for i in range(3):
    news_list.append(data_["articles"][i]["title"])    
msg1 = f"stock is {COMPANY_NAME}"    
msg2 = str(updation)+"%"+f" {symbol}"
msg3 = f"it can be due to reasons\n1.{news_list[0]}\n2.{news_list[1]}\n3.{news_list[2]}"


connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=app_password)
connection.sendmail(from_addr=my_email, to_addrs=other_email, msg=f"{msg1}\n{msg2}\n{msg3}")
connection.close() 




