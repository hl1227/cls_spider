#财联社看盘历史记录
import requests,hashlib,time
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

def parse_date(c_time):
    s_url = 'app=CailianpressWeb&category=watch&last_time={}&os=web&refresh_type=1&rn=20&sv=7.5.5'.format(c_time)
    url = 'https://www.cls.cn/v1/roll/get_roll_list?' + s_url + '&sign=' + encrypts(s_url)
    try:
        json_res = requests.get(url, headers=headers).json()
    except Exception as e:
        print('接口请求错误:{},等待5秒后重试!!!'.format(e))
        json_res={}
        time.sleep(5)
        parse_date(c_time=c_time)
    try:
        for data_dict in json_res['data']['roll_data']:
            print(data_dict)     #############最终结果##############



        next_ctime = str(data_dict['ctime'])
    except Exception as e:
        raise Exception('数据清洗错误:{},请联系技术人员'.format(e))
    print('◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆开始获取时间戳:{}◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆'.format(next_ctime))
    time.sleep(1)
    parse_date(c_time=next_ctime)

def run():
    parse_date(c_time=int(time.time()))   ######如果报错,将 'c_time' 的值更改为: '开始获取时间戳'的值(在控制台打印),再重新运行

if __name__ == '__main__':
    run()

