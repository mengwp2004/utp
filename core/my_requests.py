import requests
import mlplog
import os
from conf import setting
class MyRequests:
    log_name =os.path.join(setting.LOG_PATH,'MyRequests.log')   # 日志文件名

    time_out = 10 #请求超时时间
    def __init__(self,url,data = None,headers = None,file = None):
        self.url = url
        self.data = data
        self.headers = headers
        self.file = file
    # post方法
    def post(self):
        try:
            req = requests.post(url=self.url,data=self.data,headers =self.headers,files = self.file,timeout = self.time_out)
        except Exception as e:  # e 是对象  e.args是字符串
            res = {"status":0,"data":e.args}  # 0 代表请求失败
        else:
            try:
                res ={"status":1,"data":req.json()} # 1 代表返回json
            except Exception as e:
                res= {"status":2,"data":req.text} # 2 代表返回不是json
        log_str = 'url:%s 请求方式：post data：%s ，返回数据：%s'%(self.url,self.data,res)
        self.write_log(log_str)
        return res
    # get方法
    def get(self):
        try:
            req = requests.get(url=self.url,params =self.data,headers =self.headers,timeout = self.time_out)
        except Exception as e:  # e 是对象  e.args是字符串
            res = {"status":0,"data":e.args}  # 0 代表请求失败
        else:
            try:
                res ={"status":1,"data":req.json()} # 1 代表返回json  J
            except Exception as e:
                res= {"status":2,"data":req.text} # 2 代表返回不是json
        log_str = 'url:%s 请求方式：get data：%s ，返回数据：%s'%(self.url,self.data,res)

        self.write_log(log_str)
        return res
    # 打印log
    @classmethod
    def write_log(cls,conent):
        logger = mlplog.MyLogger(cls.log_name)
        logger.debug(conent)

if __name__ == "__main__":

    url1 = "http://192.168.124.6:9000/orderget"
    url2 ="http://192.168.124.6:9000/orderpost"
    data ={'username':"mlp","password":"123456"}
    # f = MyRequests(url1,data)
    # f.get()
    f = MyRequests(url2,data)
    f.post()
