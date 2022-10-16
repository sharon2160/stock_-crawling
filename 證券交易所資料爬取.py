#!/usr/bin/env python
# coding: utf-8

# ### 證券交易所資料爬取
# 
# 爬取111年8-10月0050日成交價格，匯出CSV

# In[85]:


#瀏覽器自動操作套件
from webdriver_manager.chrome import ChromeDriverManager 

#瀏覽器自動操作：尋找網頁元素
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#瀏覽器自動操作：設定停止秒數
import time

# 轉換成html
# import requests 
#網頁解析
from bs4 import BeautifulSoup 

import pandas as pd

url = 'https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html'
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

date_list = []
price_list = []

code = '0050' #股票代碼
sotck_code = browser.find_element(By.CLASS_NAME, 'stock-code-autocomplete').send_keys(code)


year = Select(browser.find_element(By.NAME, 'yy'))
year.select_by_index(2)

month = Select(browser.find_element(By.NAME, 'mm'))
month.select_by_index(2)

button = browser.find_element(By.CLASS_NAME, 'button.search').click()



sp = BeautifulSoup (browser.page_source, 'lxml')
stock = sp.find('div', class_='data-table') #ok
date_price = stock.find_all('td')

for i in range(0,len(date_price),2):
    date_list.append(date_price[i].text)

for i in range(1,len(date_price),2):
    price_list.append(date_price[i].text)
    

print(date_list)
print(price_list)

stock_price_dict = {'日期':date_list,
                    '收盤價':price_list}

df = pd.DataFrame(stock_price_dict)
df.to_csv('stocks_march_price', index = False)

# for i in stock:
#     print(date_price[i].text) #看不出哪裡錯


# In[91]:


#瀏覽器自動操作套件
from webdriver_manager.chrome import ChromeDriverManager 

#瀏覽器自動操作：尋找網頁元素
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#瀏覽器自動操作：設定停止秒數
import time
 
#網頁解析
from bs4 import BeautifulSoup 

#匯入pandas
import pandas as pd

url = 'https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html'
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

#建立空的清單，用來之後爬完資料之後裝資料
date_list = []
price_list = []

#輸入要查詢的股票代碼
code = '0050' #股票代碼
sotck_code = browser.find_element(By.CLASS_NAME, 'stock-code-autocomplete').send_keys(code)


for i in range(1,4):
    year = Select(browser.find_element(By.NAME, 'yy'))
    year.select_by_index(i)
    time.sleep(2)
    
    
    for i in (0,11):
        month = Select(browser.find_element(By.NAME, 'mm'))
        month.select_by_index(i)
        time.sleep(2)
        button = browser.find_element(By.CLASS_NAME, 'button.search').click()
        time.sleep(2)
        
        sp = BeautifulSoup (browser.page_source, 'lxml')
        stock = sp.find('div', class_='data-table') #ok
        date_price = stock.find_all('td')

        for i in range(0,len(date_price),2):
            date_list.append(date_price[i].text)
        for i in range(1,len(date_price),2):
            price_list.append(date_price[i].text)
        # for i in stock:
            # print(date_price[i].text) #看不出哪裡錯
    

stock_price_dict = {'日期':date_list,
                    '收盤價':price_list}




df = pd.DataFrame(stock_price_dict)
df.to_csv('stocks_march_price', index = False)



# In[90]:


df = pd.DataFrame(stock_price_dict)
df.to_csv('stocks_march_price', index = False)

