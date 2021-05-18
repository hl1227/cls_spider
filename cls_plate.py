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
    md5  = hashlib.md5(sha1.encode()).hexdigest()
    return md5
#------提取板块名及链接---------
def plate_parse(s_url):
    res_json = s.get(s_url + '&sign=' + encrypts(s_url),headers=headers,timeout=10).json()
    return res_json

def run(s_url):
    res_json=plate_parse(s_url)
    for result in res_json['data']['plate_data']:
        print(result)     #板块数据最终结果

if __name__ == '__main__':
    three_plate_link=[
                      'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=13&rever=1&sv=7.5.5&type=concept&way=change',# 概念板块接口
                      'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=1&rever=1&sv=7.5.5&type=industry&way=change', #行业板块接口
                     #'https://x-quote.cls.cn/web_quote/plate/plate_list?app=CailianpressWeb&os=web&page=2&rever=1&sv=7.5.5&type=area&way=change',     #地域板块接口
                      ]
    for s_url in three_plate_link:
        run(s_url)


