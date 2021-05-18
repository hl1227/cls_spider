#财联社看盘实时监控

import requests,hashlib,time
#请求库requests需要使用pip安装,命令行:pip3 install requests

class monitoring():
    def __init__(self):
        self.headers = {
                        'Referer': 'https://www.cls.cn/telegraph',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                       }
    def encrypts(self,text):
        if not isinstance(text, bytes):
            text = bytes(text, 'utf-8')
        sha1 = hashlib.sha1(text).hexdigest()
        md5 = hashlib.md5(sha1.encode()).hexdigest()
        return md5

    def sign(self,content):
        # 根据文本内容判定好坏
        if '涨' in content or '资金流入'in content or'强势'in content or'拉升'in content:
            sign='好'
        elif '跌'in content or'天地板'in content or'资金流出'in content or'弱'in content:
            sign='坏'
        else:
            sign=None
        return sign
    def parse_date(self,url):
        try:
            json_res=requests.get(url,headers=self.headers).json()
        except Exception:
            raise Exception('接口请求错误,请联系技术人员')
        res_json=[]
        try:
            for data_dict in json_res['data']['roll_data']:
                res_dict={}
                subject_list = []
                content=data_dict['content']
                sign=self.sign(content=content)
                ctime = time.strftime("%Y.%m.%d-%H:%M", time.localtime(int(data_dict['ctime'])))
                image_url=data_dict['images']
                for subject_dict in data_dict['subjects']:
                    subject_list.append(subject_dict['subject_name'])
                res_dict['ctime']=ctime
                res_dict['content'] =content
                res_dict['image_url'] =image_url
                res_dict['subject_list'] =subject_list
                res_dict['sign'] =sign
                res_json.append(res_dict)
        except Exception:
            raise Exception('数据清洗错误,请联系技术人员')
        return res_json

    def run(self,s_url):
        sign=self.encrypts(text=s_url)
        url = 'https://www.cls.cn/v1/roll/get_roll_list?' + s_url + '&sign=' + sign
        return self.parse_date(url=url)


if  __name__ == '__main__':
    monitoring = monitoring()
    #死循环
    while True:
        s_url = 'app=CailianpressWeb&category=watch&last_time={}&os=web&refresh_type=1&rn=20&sv=7.5.5'.format(int(time.time()))
        try:
            res_json=monitoring.run(s_url=s_url) #res_json为最终结果 json类型
            print(res_json)
        except Exception as e:
            print('error:',e)
        time.sleep(60)#设置每隔多少秒请求一次!

