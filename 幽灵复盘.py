# -*- coding: utf-8 -*-
import urllib.request
from urllib.parse import quote
from urllib.request import urlopen  # 用于获取网页
from bs4 import BeautifulSoup  # 用于解析网页
import re
import requests
import json
from pyquery import PyQuery as Q
import os
import time
from selenium import webdriver
import requests
from pyquery import PyQuery as pq
import json
import os, struct
import re
import pandas as pd
import os.path
import codecs
from pymongo import MongoClient
import pymongo
import sys
import signal
import threading
from datetime import datetime
import os
from selenium import webdriver
import pandas as pd
from pandas.core.frame import DataFrame
import requests
import json
import urllib.request
import time
import re
import datetime
import datetime
from dateutil import parser
import json
#from aip import AipNlp
#import wencai as wc
import statsmodels.tsa.api
from statsmodels import datasets
import datetime as dt
import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
import numpy as np
#import itchat
import time
#from itchat.content import *

requests.packages.urllib3.disable_warnings()

chromedriver = "C:\ProgramData\Anaconda3\chromedriver.exe"
os.environ["webriver.chrome.driver"] = chromedriver
requests.packages.urllib3.disable_warnings()

options = webdriver.ChromeOptions()
# 关闭左上方 Chrome 正受到自动测试软件的控制的提示
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("--disable-extensions")
options.add_experimental_option("excludeSwitches", ['enable-automation'])


def parse_js1(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
    return obj
##每天更新一下ts sign user-agent
ts = "1526306310660"
sign = "17dfe18bda38772ed3c1009c75b8d90d"
device_token = "170976fa8aad0c9d30f"
page=1
page_count=100
device_id="Wh/eDBIrJoIDAIoj/hfJWopH"
appversion="andr-1.9.4.0"
div="ANDH010940"
open_uuid="Wh/eDBIrJoIDAIoj/hfJWopH"


headers_hsl1 = {
"user-agent":"iIzgx71/59dfmzWZePyInQ",
"appversion": "1.9.4.1",
"deviceId": "WtAUkk4MqxwDAC3kxDu+ossd",
"mobiledevice": "2",
"Host": "goserver.huanshoulv.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
}
headers_hsl2 ={
"user-agent": "93AgOpPmLntM+Qetbf1k3Q",
"appversion": "1.9.4.1",
"mobiledevice": "2",
"deviceId": "WtAUkk4MqxwDAC3kxDu+ossd",
"Accept-Encoding": "gzip",
"Host": "serverplus.huanshoulv.com",
"Connection": "Keep-Alive",
}
tdate =datetime.datetime.now().strftime('%Y-%m-%d')#今天
大盘信息表=[]
大盘信息表.append(str(tdate))
def 大盘温度趋势雷达(tdate):
    #大盘温度
    # #http://stock.jrj.com.cn/dapanwenduji/ 大盘温度
    # url = "http://stock.jrj.com.cn/action/stock-dynamic/dpwdj/getWdjInfo.jspa?vname=wdjData&_=1524834221000"
    url = "http://stock.jrj.com.cn/action/stock-dynamic/dpwdj/getWdjInfo.jspa?vname=wdjData&_=" + str(
        int(time.time() * 1000))
    stockDataResponse = urllib.request.urlopen(url)
    stockData = stockDataResponse.read()
    stockData = stockData.decode('gbk')
    stockData = stockData[12:-1]
    res = json.loads(stockData)
    # 涨跌情况
    # limitUpNum 涨停
    # scopeUpMoreFivePercentNum 涨幅>=5%
    # limitDownNum 跌停
    # scopeDownMoreFivePercentNum 跌幅<=-5%


    #昨天涨停连板数
    涨停数=res['data']['marketVO']['limitUpNum']
    涨幅5=res['data']['marketVO']['scopeUpMoreFivePercentNum']
    跌停数=res['data']['marketVO']['limitDownNum']
    跌幅5=res['data']['marketVO']['scopeDownMoreFivePercentNum']

    # 趋势雷达
    # raiseTrendStocksNum 上涨趋势
    # fallTrendStocksNum 下跌趋势
    # noTrendStocksNum 暂无趋势
    # shakeTrendStocksNum 震荡趋势
    上涨趋势=res['data']['trendVO']['raiseTrendStocksNum']
    下跌趋势=res['data']['trendVO']['fallTrendStocksNum']
    暂无趋势=res['data']['trendVO']['noTrendStocksNum']
    震荡趋势=res['data']['trendVO']['shakeTrendStocksNum']

    主力净流入=res['data']['fundFlowList'][0]['bruntNetInflow']

    累计净流入=res['data']['fundFlowList'][0]['todayNetInflow']
    中单净流入=res['data']['fundFlowList'][0]['middleNetInflow']
    散单净流入=res['data']['fundFlowList'][0]['retailNetInflow']
    建议仓位=res['data']['suggestPosition']
    大盘信息表.append("主力净流入:"+ str(主力净流入))
    大盘信息表.append("累计净流入:"+ str(累计净流入))
    大盘信息表.append("中单净流入:"+ str(中单净流入))
    大盘信息表.append("散单净流入:"+ str(散单净流入))
    大盘信息表.append("建议仓位:"+ str(建议仓位))
    大盘信息表.append("涨停数:"+ str(涨停数))
    大盘信息表.append("涨幅5:"+ str(涨幅5))
    大盘信息表.append("跌停数:"+ str(跌停数))
    大盘信息表.append("跌幅5:"+ str(跌幅5))
    大盘信息表.append("上涨趋势:"+ str(上涨趋势))
    大盘信息表.append("下跌趋势:"+ str(下跌趋势))
    大盘信息表.append("暂无趋势:"+ str(暂无趋势))
    大盘信息表.append("震荡趋势:"+ str(震荡趋势))
    #print(主力净流入,累计净流入,中单净流入,散单净流入,建议仓位)
    #print(涨停数,涨幅5,跌停数,跌幅5)
    #print(上涨趋势,下跌趋势,暂无趋势,震荡趋势)

#国内股票数据：个股
def getChinaStockIndividualInfo(stockCode, period):
    try:
        exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
        dataUrl = "http://hq.sinajs.cn/list=" + exchange + stockCode
        stdout = urllib.request.urlopen(dataUrl)
        stdoutInfo = stdout.read().decode('gb2312')
        tempData = re.search('''(")(.+)(")''', stdoutInfo).group(2)
        stockInfo = tempData.split(",")
        #stockCode = stockCode,
        stockName   = stockInfo[0]  #名称
        stockStart  = stockInfo[1]  #开盘
        stockLastEnd= stockInfo[2]  #昨收盘
        stockCur    = stockInfo[3]  #当前
        stockMax    = stockInfo[4]  #最高
        stockMin    = stockInfo[5]  #最低
        stockUp     = round(float(stockCur) - float(stockLastEnd), 2)
        stockRange  = round(float(stockUp) / float(stockLastEnd), 4) * 100
        stockVolume = round(float(stockInfo[8]) / (100 * 10000), 2)
        stockMoney  = round(float(stockInfo[9]) / (100000000), 2)
        stockTime   = stockInfo[31]

        content = "#" + stockName + "#(" + stockCode + ")" + " 开盘:" + stockStart \
        + ",最新:" + stockCur + ",最高:" + stockMax + ",最低:" + stockMin \
        + ",涨跌:" + str(stockUp) + ",幅度:" + str(stockRange) + "%" \
        + ",总手:" + str(stockVolume) + "万" + ",金额:" + str(stockMoney) \
        + "亿" + ",更新时间:" + stockTime + "  "

        imgUrl = "http://image.sinajs.cn/newchart/" + period + "/n/" + exchange + str(stockCode) + ".gif"
        twitter = {'exchange': exchange, 'stockRange': stockRange}

    except Exception as e:
        print(">>>>>> Exception: " + str(e))
    else:
        return twitter
    finally:
        None


codelist=[]
def 涨停强度_全部涨停板数据():
    涨停强度_全部涨停板 = "http://goserver.huanshoulv.com/aimapp/surgeLimit/surgeLimitList?page=1&page_count=100&sort_field_name=px_change_rate&sort_type=-1&type=1&stock_type=0&ts="+ts+"&device_id=Wh/eDBIrJoIDAIoj/hfJWopH&device_token=140fe1da9e860b91168&appversion=andr-1.9.4.0&div=ANDH010940&open_uuid=Wh/eDBIrJoIDAIoj/hfJWopH&channel=hsl-app&sdk_int=26&width=1080&sign="+sign
    content = requests.get(涨停强度_全部涨停板, headers=headers_hsl1).content
    text = parse_js1(content)
    # print(text)
    status = text["status"]
    timestamp = text["timestamp"]
    data = text["data"]
    # print(20*"-")
    # print(data)
    # for x in data:
    # print(x)
    # print(20 * "-")
    # print(data["fields"])
    # print(20 * "-")
    # print(data["page"])
    # print(20 * "-")
    # print(data["top"])
    # print(20 * "-")
    for x in data["surgeList"]:
        if int(x[34])==1:
            codelist.append([x[32], x[33], "一字板", x[35], x[3].replace("换手率App", "张雨杰NLP")])
            #print([x[32], x[33], "一字板", x[35], x[3].replace("换手率App", "张雨杰NLP")])
        else:
            codelist.append([x[32], x[33], "非一字板", x[35],x[3].replace("换手率App","张雨杰NLP")])
            #print([x[32], x[33], "非一字板", x[35],x[3].replace("换手率App","张雨杰NLP")])
    #print("全部涨停板数据")
    for x in codelist:
        print(x)

def 涨停强度_最强风口数据():
    涨停强度_最强风口 = "http://goserver.huanshoulv.com/aimapp/surgeLimit/surgeTopBlock?div=ANDH010940&device_id=Wh/eDBIrJoIDAIoj/hfJWopH&device_token=140fe1da9e860b91168&channel=hsl-app&width=1080&sign="+sign+"&appversion=andr-1.9.4.0&open_uuid=Wh/eDBIrJoIDAIoj/hfJWopH&sdk_int=26&ts="+ts
    content = requests.get(涨停强度_最强风口,headers = headers_hsl1).content
    text = parse_js1(content)
    #print(text)
    status = text["status"]
    timestamp = text["timestamp"]
    data = text["data"]
    # print(20*"-")
    #print(data)
    #for x in data:
        #print(x)
    #print(data["block"])
    #print(20 * "-")
    #print(data["block_name"])
    #print(20 * "-")
    #print(data["fields"])
    #print(20 * "-")
    #print(data["surgeList"])
    #print(20 * "-")
    hb_list  = []
    for x in data["block"]:
        #print(x.get("block_name"))
        hb_list.append(x.get("block_name"))
        大盘信息表.append("最强风口数据:" + x.get("block_name"))
        #print([x[28], x[29], x[25], x[1]])
    print( "最强风口数据:",hb_list)
    return hb_list

def httpsrt(string):
    string = str(string)
    start_string1 = 'w='
    end_string1 = 'target='

    start_string2 = 'target="_blank">'
    end_string2 = '</a>'
    # 先找第一个开始位置
    start = string.find(start_string1)
    start1 = string.find(start_string2)
    # 只要start不等于-1，说明找到了http

    # 找结束的位置
    end = string.find(end_string1, start)
    end1 =  string.find(end_string2, start1)
    # 截取字符串 结束位置=结束字符串的开始位置+结束字符串的长度
    sub_str = string[start:end][2:8]
    sub_str1 = string[start1:end1][16:]
    return sub_str,sub_str1
stocklist=[]
def 问财一字板():
    策略 = "一字板,涨停原因，最新涨停封单额，最新涨停封单量，涨停开板次数，涨停封成比，涨停封流比，连续涨停次数，首次涨停时间，最后涨停时间，流通盘，流通市值，上市天数，行业，首次封单量，占实际流通比，占成交量比，最高封单量，占实际流通比，占成交量比"
    url = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=" + 策略
    print(url)
    browser = webdriver.Chrome(chromedriver,chrome_options=options)

    browser.set_window_size(100, 1080)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    page_cnt = soup.find('span', attrs={'class': 'total'})
    NEXTPAGE=(page_cnt!=None)
    if NEXTPAGE == True:
        page_cnt = int(page_cnt.string[len("共"):-1])
    else:
        page_cnt=1
    page = 0

    while page < page_cnt:
        代码表 = []
        名称表 = []
        涨停属性表 = []
        现价表 = []
        涨跌幅表 = []
        涨停原因类别表 = []
        涨停封单额表 = []
        涨停封单量表 = []
        涨停开板次数表 = []
        涨停封成比表 = []
        涨停封流比表 = []
        连续涨停天数表 = []
        最终涨停时间表 = []
        a股流通市值表 = []
        上市天数表 = []
        # 行业表=[]
        page = page + 1
        bs = BeautifulSoup(html, "lxml")
        bs_con = bs.find_all('div', attrs={'class': 'em'})
        bs_name = bs.find_all('div', attrs={'class': 'em graph alignCenter graph'})
        i = 0
        for code in bs_con:
            try:
                #print(code)
                code = code.string.strip()
                if len(code) == len('300300') and int(code) > 0:
                    代码表.append(code)
                    #print("00000", code)
                    i=i+1
            except:
                pass
        i=0
        for name in bs_name:
            try:
                #print("2222",name)
                name = name.string.strip()
                名称表.append(name)
                #print("1111", name)
                i = i + 1
            except:
                pass
        '''
        bs_name = bs.find_all('a')  # qs=stockpick_ztyy&
        for hrefs in bs_name:
            #print("aaaa",hrefs)
            #print(hrefs.get('href'))
            if str(hrefs.get('href')).find("ztyy") != -1:
                涨停属性表.append(hrefs.string.strip())
                print("zzzz",hrefs.string.strip())
        #hrefs = [item.get('href') for item in bs_name if item.get('href')]
        #print("xxx",hrefs)
        '''
        '''
        现价(元)          2
        涨跌幅( %) 3
        涨停原因类别        4
        涨停封单额        5
        涨停封单量        6
        涨停开板次数        7
        涨停封成比        8
        涨停封流比        9
        连续涨停天数        10
        最终涨停时间        12
        a股流通市值        14
        上市天数        15
        #行业        16
        '''
        bs_tag = bs.find_all('td', attrs={'colnum': '2'})
        for hrefs in bs_tag:
            #print(hrefs)
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            现价表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '3'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em _x_ red alignRight alignRight'})[0].string.strip()
            涨跌幅表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '4'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em'})[0].string.strip()
            涨停原因类别表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '5'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em red alignRight alignRight'})[0].string.strip()
            涨停封单额表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '6'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em red alignRight alignRight'})[0].string.strip()
            涨停封单量表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '7'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            涨停开板次数表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '8'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            涨停封成比表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '9'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            涨停封流比表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '10'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            连续涨停天数表.append(text)

        bs_tag = bs.find_all('td', attrs={'colnum': '12'})
        for hrefs in bs_tag:
            timestr=""
            spans = hrefs.find_all('span')
            timelist=[]
            for x in spans:
                timelist.append(x.text)
                #print("112233",timestr,x.text)
            if len(timelist) == 6:
                timestr = timelist[0]+timelist[1]+":"+timelist[2]+timelist[3]+":"+timelist[4]+timelist[5]
            最终涨停时间表.append(timestr)

        bs_tag = bs.find_all('td', attrs={'colnum': '14'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            a股流通市值表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '15'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            上市天数表.append(text)
        for i in range(len(代码表)):
            stocklist.append([代码表[i],现价表[i], 涨跌幅表[i], 涨停原因类别表[i], 涨停封单额表[i], 涨停封单量表[i], 涨停开板次数表[i], 涨停封成比表[i],涨停封流比表[i], 连续涨停天数表[i], 最终涨停时间表[i], a股流通市值表[i], 上市天数表[i]])
        #print(stocklist)
        if  NEXTPAGE == True:
            # 模拟点击翻页
            browser.find_element_by_id("next").click()
            # time.sleep(2)
            current_page = 0
            while current_page < page_cnt:
                time.sleep(0.1)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                current_page = soup.find('a', attrs={'class': 'num current'})
                current_page = int(current_page.string)
                if current_page == page + 1:
                    # print(current_page)
                    time.sleep(0.5)
                    break
    #print("list1:",stocklist)
    browser.close()



def 问财非一字板():
    策略 = "非一字板,涨停原因，最新涨停封单额，最新涨停封单量，涨停开板次数，涨停封成比，涨停封流比，连续涨停次数，首次涨停时间，最后涨停时间，流通盘，流通市值，上市天数，行业，首次封单量，占实际流通比，占成交量比，最高封单量，占实际流通比，占成交量比"
    url = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=" + 策略
    browser = webdriver.Chrome(chromedriver,chrome_options=options)
    browser.set_window_size(100, 1080)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    page_cnt = soup.find('span', attrs={'class': 'total'})
    NEXTPAGE = (page_cnt != None)
    if NEXTPAGE == True:
        page_cnt = int(page_cnt.string[len("共"):-1])
    else:
        page_cnt = 1
    page = 0
    while page < page_cnt:
        代码表 = []
        名称表 = []
        涨停属性表 = []
        现价表 = []
        涨跌幅表 = []
        涨停原因类别表 = []
        涨停封单额表 = []
        涨停封单量表 = []
        涨停开板次数表 = []
        涨停封成比表 = []
        涨停封流比表 = []
        连续涨停天数表 = []
        最终涨停时间表 = []
        a股流通市值表 = []
        上市天数表 = []
        # 行业表=[]
        page = page + 1
        bs = BeautifulSoup(html, "lxml")
        bs_con = bs.find_all('div', attrs={'class': 'em'})
        bs_name = bs.find_all('div', attrs={'class': 'em graph alignCenter graph'})
        i = 0
        for code in bs_con:
            try:
                # print(code)
                code = code.string.strip()
                if len(code) == len('300300') and int(code) > 0:
                    代码表.append(code)
                    # print("00000", code)
                    i = i + 1
            except:
                pass
        i = 0
        for name in bs_name:
            try:
                # print("2222",name)
                name = name.string.strip()
                名称表.append(name)
                #print("1111", name)
                #pirnt("22222", 名称表)
                i = i + 1
            except:
                pass
        '''
        bs_name = bs.find_all('a')  # qs=stockpick_ztyy&
        for hrefs in bs_name:
            #print("aaaa",hrefs)
            #print(hrefs.get('href'))
            if str(hrefs.get('href')).find("ztyy") != -1:
                涨停属性表.append(hrefs.string.strip())
                print("zzzz",hrefs.string.strip())
        #hrefs = [item.get('href') for item in bs_name if item.get('href')]
        #print("xxx",hrefs)
        '''
        '''
        现价(元)          2
        涨跌幅( %) 3
        涨停原因类别        4
        涨停封单额        5
        涨停封单量        6
        涨停开板次数        7
        涨停封成比        8
        涨停封流比        9
        连续涨停天数        10
        最终涨停时间        12
        a股流通市值        14
        上市天数        15
        #行业        16
        '''
        bs_tag = bs.find_all('td', attrs={'colnum': '2'})
        for hrefs in bs_tag:
            #print(hrefs)
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            现价表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '3'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em _x_ red alignRight alignRight'})[0].string.strip()
            涨跌幅表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '4'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em'})[0].string.strip()
            涨停原因类别表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '5'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em red alignRight alignRight'})[0].string.strip()
            涨停封单额表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '6'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em red alignRight alignRight'})[0].string.strip()
            涨停封单量表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '7'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            涨停开板次数表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '8'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            涨停封成比表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '9'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            涨停封流比表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '10'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            连续涨停天数表.append(text)

        bs_tag = bs.find_all('td', attrs={'colnum': '12'})
        for hrefs in bs_tag:
            timestr = ""
            spans = hrefs.find_all('span')
            timelist = []
            for x in spans:
                timelist.append(x.text)
                # print("112233",timestr,x.text)
            if len(timelist) == 6:
                timestr = timelist[0] + timelist[1] + ":" + timelist[2] + timelist[3] + ":" + timelist[4] + timelist[5]
            最终涨停时间表.append(timestr)

        bs_tag = bs.find_all('td', attrs={'colnum': '14'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight alignRight'})[0].string.strip()
            a股流通市值表.append(text)
        bs_tag = bs.find_all('td', attrs={'colnum': '15'})
        for hrefs in bs_tag:
            text = hrefs.find_all('div', attrs={'class': 'em alignRight'})[0].string.strip()
            上市天数表.append(text)
        #print(名称表)
        #print(len(代码表),len(名称表),len( 现价表),len( 涨跌幅表),len( 涨停原因类别表),len( 涨停封单额表),len( 涨停封单量表),len( 涨停开板次数表),len( 涨停封成比表),len( 涨停封流比表),len(
                 #连续涨停天数表),len( 最终涨停时间表),len( a股流通市值表),len( 上市天数表))
        for i in range(len(代码表)):
            stocklist.append([ 代码表[i],现价表[i],涨跌幅表[i], 涨停原因类别表[i], 涨停封单额表[i], 涨停封单量表[i], 涨停开板次数表[i], 涨停封成比表[i], 涨停封流比表[i],
                 连续涨停天数表[i], 最终涨停时间表[i], a股流通市值表[i], 上市天数表[i]])

        if NEXTPAGE == True:
            # 模拟点击翻页
            browser.find_element_by_id("next").click()
            # time.sleep(2)
            current_page = 0
            while current_page < page_cnt:
                time.sleep(0.1)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                current_page = soup.find('a', attrs={'class': 'num current'})
                current_page = int(current_page.string)
                if current_page == page + 1:
                    # print(current_page)
                    time.sleep(0.5)
                    break
    #print("list2:",stocklist)
    browser.close()




#大盘温度趋势雷达(tdate)
#涨停强度_最强风口数据()
#涨停强度_全部涨停板数据()


问财一字板()
问财非一字板()
# raise
# #stocklist=[['002307', '北新路桥', '8.27', '9.97', '一带一路', '1.60亿', '1,930.18万', '0', '469.61', '2.16', '2', '09:30:00', '73.74亿', '3,417'], ['002950', '奥美医疗', '30.95', '9.99', '新股', '2.02亿', '654.03万', '0', '1,180.28', '13.63', '8', '09:30:00', '14.86亿', '10'], ['002951', '金时科技', '19.04', '9.99', '新股', '1.45亿', '761.78万', '0', '3.49万', '16.93', '4', '09:30:00', '8.57亿', '6'], ['300762', '上海瀚讯', '34.32', '10.00', '新股', '2.38亿', '692.25万', '0', '4.31万', '20.75', '5', '09:30:00', '11.45亿', '7'], ['300763', '锦浪科技', '42.20', '10.01', '新股', '1.24亿', '293.01万', '0', '10.85万', '14.65', '2', '09:30:00', '8.44亿', '2'], ['000503', '国新健康', '25.41', '10.00', '拟收购', '1.66亿', '653.31万', '0', '31.24', '0.73', '2', '09:30:00', '228.38亿', '9,607'], ['600072', '中船科技', '13.04', '10.04', '拟收购', '1.72亿', '1,322.81万', '0', '777.82', '2.20', '3', '09:30:00', '78.34亿', '7,961'], ['600345', '长江通信', '29.76', '10.02', '拟收购', '2.87亿', '965.49万', '0', '1,327.19', '4.88', '2', '09:30:00', '58.92亿', '6,663'], ['002109', '兴化股份', '4.72', '10.02', '甲醇汽车', '2.92亿', '6,182.75万', '0', '674.25', '11.34', '1', '09:30:00', '25.72亿', '4,437'], ['600722', '金牛化工', '6.42', '9.93', '甲醇汽车', '4.02亿', '6,267.76万', '0', '1,131.88', '9.21', '1', '09:30:00', '43.68亿', '8,303'], ['300536', '农尚环境', '14.67', '9.97', '高送转', '2.63亿', '1,792.00万', '0', '1,923.27', '29.34', '4', '09:30:00', '8.96亿', '912'], ['000993', '闽东电力', '9.47', '9.99', '电力', '2.73亿', '2,884.01万', '0', '296.84', '7.73', '4', '09:30:00', '35.32亿', '6,807']]
# #codelist=[['300152', '科融环境', '非一字板', '首板', '环保（神雾节能2连板带动）+创投（3月18日晚消息科创板受理名单或周五公布 保荐机构在接受最后培训）'], ['300337', '银邦股份', '非一字板', '首板', '科创板（今日10:11互动平台：公司正在探讨参股子公司飞而康科创板上市的可能性）'], ['600509', '天富能源', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路+油气改革+风电+甲醇'], ['600232', '金鹰股份', '非一字板', '首板', '工业大麻（浙江金鹰股份六安麻纺有限公司投资7350万元的六安大麻产业化项目）'], ['000682', '东方电子', '非一字板', '首板', '电力物联网（3月10日消息国家电网公司全面部署泛在电力物联网建设）'], ['000633', '合金投资', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路+创投'], ['000517', '荣安地产', '非一字板', '首板', '房地产（今日14:01消息财政部公布2019年立法工作安排 未提及房地产税）'], ['600156', '华升股份', '非一字板', '首板', '工业大麻（华升集团与汉麻集团达成全面战略合作意向）'], ['000563', '陕国投Ａ', '非一字板', '首板', '西安本地股（3月11日意大利“一带一路”展会城市推介会在西安举行）+创投'], ['600072', '中船科技', '一字板', '三连板', '一带一路+昨夜公告拟收购海鹰集团 加速打造中船集团多元化发展平台，复牌补涨'], ['300589', '江龙船艇', '非一字板', '首板', '一带一路（第二届“一带一路”国际合作高峰论坛将于4月下旬在北京举办）'], ['603829', '洛凯股份', '非一字板', '首板', '张雨杰NLP独家AI集合竞价提前看多+电力物联网（3月10日消息国家电网公司全面部署泛在电力物联网建设）+年报高送转预期'], ['000721', '西安饮食', '非一字板', '首板', '西安本地股（3月11日意大利“一带一路”展会城市推介会在西安举行）+一带一路+年报增长'], ['600800', '天津磁卡', '非一字板', '首板', '工业大麻（公司参股的云南省西双版纳云麻实业有限公司主营云麻的种植）'], ['002302', '西部建设', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['000788', '北大医药', '非一字板', '二连板', '创投+高校+医药（2月27日上交所理事长黄红元：科创板储备企业中生物医药等领域占比大）'], ['600798', '宁波海运', '非一字板', '首板', '港口航运（今日午间习近平：愿同意大利共建“一带一路” 深入挖掘在港口物流、船舶运输等领域合作）+一带一路'], ['600356', '恒丰纸业', '非一字板', '首板', '工业大麻（3月6日互动平台：恒元汉麻公司为集团公司汉麻产业实施主体 公司拥有全大麻手卷纸的生产方法专利）'], ['002565', '顺灏股份', '非一字板', '首板', '工业大麻（昨夜公告拟在美国设立子公司 拓展工业大麻相关业务）'], ['600088', '中视传媒', '非一字板', '三连板', '创投（3月18日晚消息科创板受理名单或周五公布 保荐机构在接受最后培训）+超高清视频'], ['600345', '长江通信', '一字板', '二连板', '3月18日晚公告拟发行股份收购烽火众智100%股权，复牌补涨'], ['300721', '怡达股份', '非一字板', '首板', '甲醇（3月19日盘后八部门发文鼓励在部分地区开展甲醇汽车应用）+年报高送转预期'], ['002109', '兴化股份', '一字板', '首板', '甲醇（3月19日盘后八部门发文鼓励在部分地区开展甲醇汽车应用）'], ['002787', '华源控股', '非一字板', '二连板', '科创板（3月7日互动平台：公司现持有润天智10%的股权，公司会积极关注科创板的相关政策及润天智的发展情况）'], ['000504', '南华生物', '非一字板', '首板', '张雨杰NLP独家AI集合竞价提前看多+医药（2月27日上交所理事长黄红元：科创板储备企业中生物医药等领域占比大）'], ['300380', '安硕信息', '非一字板', '首板', '创投（上海复之硕创业投资合伙企业）+国产软件+互联网金融'], ['002356', '赫美集团', '非一字板', '首板', '借壳（3月3日晚公告吸收合并英雄互娱 应书岭预计成为新实控人）+创投+电力物联网+互联网金融'], ['300663', '科蓝软件', '非一字板', '三连板', '今早公告与蚂蚁金融云展开业务合作+创投+国产软件'], ['002750', '龙津药业', '非一字板', '首板', '张雨杰NLP独家AI集合竞价提前看多+工业大麻（2月28日晚公告布局工业大麻领域）'], ['603881', '数据港', '非一字板', '首板', '3月18日晚公告近日公司与阿里巴巴签署关于ZH13等项目合作备忘录'], ['300763', '锦浪科技', '一字板', '二连板', '次新股一字连板'], ['603032', '德新交运', '非一字板', '首板', '西部开发+一带一路+年报增长（2月27日晚公告去年全年净利2.57亿 同比增长848.58%）'], ['600841', '上柴股份', '非一字板', '首板', '上海国资改革（3月15日早间消息上海谋划大手笔：打造国资改革示范区和国企改革尖兵）+氢能源'], ['000905', '厦门港务', '非一字板', '二连板', '福建板块（3月4日韩国瑜：将在3月22日至28日访问香港、澳门及深圳、厦门 进行城市交流）+一带一路'], ['000572', '海马汽车', '非一字板', '首板', '张雨杰NLP独家AI集合竞价提前看多+工业大麻（间接参股中麻立方科技有限公司）+新能源汽车（甲醇汽车带动）'], ['600888', '新疆众和', '非一字板', '首板', '张雨杰NLP独家AI集合竞价提前看多+西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['000159', '国际实业', '非一字板', '五连板', '创投+科创板基金（万家基金40%股权）+一带一路+油气改革+西部开发'], ['000610', '西安旅游', '非一字板', '首板', '西安本地股（3月11日意大利“一带一路”展会城市推介会在西安举行）+一带一路+创投'], ['603315', '福鞍股份', '非一字板', '首板', '疑似庄股'], ['600624', '复旦复华', '非一字板', '八连板', '创投+复旦张江概念（3月8日晚港股复旦张江：建议发行A股并于科创板上市 公司实控人持有复旦张江6%股权）+高校'], ['300762', '上海瀚讯', '一字板', '五连板', '次新股一字连板'], ['000503', '国新健康', '一字板', '二连板', '创投（3月18日晚消息科创板受理名单或周五公布 保荐机构在接受最后培训）'], ['000820', '神雾节能', '非一字板', '二连板', '超跌反弹+环保工程'], ['000796', '凯撒旅游', '非一字板', '首板', '一带一路（习近平主席将于3月21日至26日对意大利、摩纳哥、法国进行国事访问 公司主营出境游）'], ['300690', '双一科技', '非一字板', '首板', '风电（招标价回升成本下降 风电设备企业盈利今年将迎拐点）'], ['002017', '东信和平', '非一字板', '首板', '5G（3月17日工信部部长苗圩：要加快建设5G、工业互联网等新型智能基础设施）+前期妖股'], ['002950', '奥美医疗', '一字板', '八连板', '次新股一字连板'], ['600682', '南京新百', '非一字板', '首板', '医药（2月27日上交所理事长黄红元：科创板储备企业中生物医药等领域占比大）'], ['000993', '闽东电力', '一字板', '四连板', '核电（3月18日晚消息核电开闸！首批投资800亿 中长期规划投6000亿）+创投+风电'], ['002951', '金时科技', '一字板', '四连板', '次新股一字连板'], ['000990', '诚志股份', '非一字板', '二连板', '甲醇（3月19日盘后八部门发文鼓励在部分地区开展甲醇汽车应用）+工业大麻+氢能源+高校+创投（诚志科技园）'], ['002094', '青岛金王', '非一字板', '首板', '一带一路（第二届“一带一路”国际合作高峰论坛将于4月下旬在北京举办）'], ['000570', '苏常柴Ａ', '非一字板', '三连板', '创投+科创板（大股东参股新光光电）+氢能源'], ['600679', '上海凤凰', '非一字板', '四连板', '上海国资改革（3月15日早间消息上海谋划大手笔：打造国资改革示范区和国企改革尖兵）+创投'], ['600928', '西安银行', '非一字板', '首板', '西安本地股（3月11日意大利“一带一路”展会城市推介会在西安举行）+一带一路+次新银行'], ['300471', '厚普股份', '非一字板', '五连板', '氢能源（3月15日盘后国务院：《政府工作报告》新增“推动充电、加氢等设施建设”等内容）+油气改革'], ['002333', '罗普斯金', '非一字板', '首板', '苹果概念（苹果春季发布会将于北京时间3月26日凌晨1点在苹果总部举行）'], ['300171', '东富龙', '非一字板', '首板', '科创板（参股上海伯豪生物 2月27日上交所理事长黄红元：科创板储备企业中生物医药等领域占比大）'], ['002307', '北新路桥', '一字板', '二连板', '一带一路+西部开发+3月18日晚公告拟发行可转债及股份收购北新渝长，复牌补涨'], ['002473', '圣莱达', '非一字板', '二连板', 'ST摘帽（3月17日晚公告3月19日开市起撤销退市风险警示）'], ['601515', '东风股份', '非一字板', '首板', '工业大麻（2月19日晚公告参股公司绿馨电子与云南汉素拟设立合资公司 探索经营工业大麻花叶萃后基础材料应用的相关业务）'], ['600746', '江苏索普', '非一字板', '首板', '氢能源（3月15日盘后国务院：《政府工作报告》新增“推动充电、加氢等设施建设”等内容）'], ['300536', '农尚环境', '一字板', '四连板', '高送转（3月14日晚公告拟10转7.5派0.63元）'], ['300103', '达刚路机', '非一字板', '三连板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['603015', '弘讯科技', '非一字板', '首板', '一带一路（3月19日晚互动平台： 公司意大利子公司EEI主要从事驱动器、逆变器等工业设备高端解决方案等的研发）'], ['600831', '广电网络', '非一字板', '二连板', '5G（3月17日工信部部长苗圩：要加快建设5G、工业互联网等新型智能基础设施）+创投+超高清视频'], ['600695', '绿庭投资', '非一字板', '四连板', '创投（3月18日晚消息科创板受理名单或周五公布 保荐机构在接受最后培训）'], ['000877', '天山股份', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['600199', '金种子酒', '非一字板', '三连板', '白酒+年报预增（1月31日晚公告预计全年净利润同比增长1194%至1268%）'], ['600146', '商赢环球', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['603169', '兰石重装', '非一字板', '二连板', '核电（3月18日晚消息核电开闸！首批投资800亿 中长期规划投6000亿）+一带一路+西部开发'], ['300332', '天壕环境', '非一字板', '首板', '创投+科创板（公司参股威马汽车 控股股东参股上海聚辰半导体 公司董事长陈作涛为上海聚辰半导体董事长）+油气改革'], ['600540', '新赛股份', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['600722', '金牛化工', '一字板', '首板', '甲醇（3月19日盘后八部门发文鼓励在部分地区开展甲醇汽车应用）'], ['600075', '新疆天业', '非一字板', '首板', '西部开发（3月19日晚中央深改委：推进西部大开发形成新格局）+一带一路'], ['000683', '远兴能源', '非一字板', '首板', '甲醇（3月19日盘后八部门发文鼓励在部分地区开展甲醇汽车应用）+油气改革']]
# #print(stocklist)
# #print(codelist)
# rtnlist=[]
# print(大盘信息表)
# rtnlist.append(大盘信息表)
# for x in stocklist:
#     for y in codelist:
#         if y[0] == x[0]:
#             code1=int(y[0])
#             if code1 < 300000:
#                 code1 = str(code1)
#                 code1 = 'SZ' + code1.zfill(6)
#             elif code1 >= 300000 and code1 < 600000:
#                 code1 = 'SZ' + str(code1)
#             elif code1 >= 600000:
#                 code1 = 'SH' + str(code1)
#             z = [code1,y[1],y[2],y[3],y[4]]+ [x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]]
#             rtnlist.append(z)
# #print(codelist)
#
# list=rtnlist
# name=["代码","名称","板类别","连板","涨停原因","现价","涨跌幅","涨停属性","封单额","涨停封单量","涨停开板次数","涨停封成比","涨停封流比","连续涨停天数","最终涨停时间","a股流通市值","上市天数"]
# test=pd.DataFrame(columns=name,data=list)
# filenmae="复盘_"+str(tdate)+".csv"
# test.to_csv(filenmae,encoding='gbk')