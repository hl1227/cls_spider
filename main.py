import requests,hashlib,time,random
from requests.adapters import HTTPAdapter
headers = {
    'Referer': 'https://www.cls.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
}
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
def encrypts(text):
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    sha1 = hashlib.sha1(text).hexdigest()
    md5 = hashlib.md5(sha1.encode()).hexdigest()
    return md5
#------提取板块名及链接---------
def plate_parse(s_url):
    l=[]
    res_json = s.get(s_url + '&sign=' + encrypts(s_url),headers=headers,timeout=10).json()
    for data in res_json['data']['plate_data']:
        d={}
        d['bk_name']=data['secu_name']
        d['bk_link']=data['secu_code']
        l.append(d)
    return l
#-----提取股票名及链接---------
def stock_parse(plate):
    s_url='https://x-quote.cls.cn/web_quote/plate/stocks?app=CailianpressWeb&os=web&rever=1&secu_code={}&sv=7.5.5&way=last_px'.format(plate['bk_link'])
    res_json=s.get(s_url + '&sign=' + encrypts(s_url),headers=headers,timeout=10).json()
    l = []
    for data in res_json['data']['stocks']:
        d = {}
        d['stock_name']=  data['secu_name']
        d['stock_code'] = data['secu_code']
        l.append(d)
    return l
#-----提取股票数据--------(最终结果在此返回)
def stock_data(stock):
    s_url = 'https://x-quote.cls.cn/quote/stock/basic?secu_code={}&fields=open_px,av_px,high_px,low_px,change,change_px,down_price,change_3,change_5,qrr,entrust_rate,tr,amp,TotalShares,mc,NetAssetPS,NonRestrictedShares,cmc,business_amount,business_balance,pe,ttm_pe,pb,secu_name,secu_code,trade_status,secu_type,time,preclose_px,up_price,last_px&app=CailianpressWeb&os=web'.format(stock['stock_code'])
    res_json = s.get(s_url + '&sign=' + encrypts(s_url),headers=headers,timeout=10).json()
    print('--------------------',time.strftime('%Y.%m.%d-%H:%M:%S'),res_json['data']['secu_name'],'获取成功','--------------------')
    return res_json['data']
def run(s_url):
    plate_list=plate_parse(s_url)
    for plate in plate_list:
        try:
            print('---------------', time.strftime('%Y.%m.%d-%H:%M:%S'),'开始获取板块:',plate['bk_name'],'---------------')
            stock_list=stock_parse(plate)
        except Exception as e:
            print('***error:{},股票名及链接请求失败:{}'.format(e,plate['bk_name']))
            continue
        for stock in stock_list:
            try:
                result=stock_data(stock)
                print(result)   #####最终结果
            except Exception as e:print('***error:{},股票数据请求失败:{}'.format(e,stock['stock_name']))
            time.sleep(random.random())




if __name__ == '__main__':
    three_plate_link=[
                      'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=1&rever=1&sv=7.5.5&type=industry&way=change', #行业板块接口
                      'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=13&rever=1&sv=7.5.5&type=concept&way=change', #概念板块接口
                      'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=2&rever=1&sv=7.5.5&type=area&way=change',     #地域板块接口
                      ]
    for s_url in three_plate_link:
        run(s_url)


