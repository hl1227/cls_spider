import requests,hashlib
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

#-----提取股票数据--------(最终结果在此返回)
def stock_data(stock_code):
    s_url = 'https://x-quote.cls.cn/quote/stock/basic?secu_code={}&fields=open_px,av_px,high_px,low_px,change,change_px,down_price,change_3,change_5,qrr,entrust_rate,tr,amp,TotalShares,mc,NetAssetPS,NonRestrictedShares,cmc,business_amount,business_balance,pe,ttm_pe,pb,secu_name,secu_code,trade_status,secu_type,time,preclose_px,up_price,last_px&app=CailianpressWeb&os=web'.format(stock_code)
    res_json = s.get(s_url + '&sign=' + encrypts(s_url),headers=headers,timeout=10).json()
    return res_json['data']


if __name__ == '__main__':
    ######stock参数为股票code码  如:sh600036##########################
    result=stock_data(stock_code='')
    print(result)

