from conf.setting import mysql_info,redis_info
import pymysql
import hashlib
import redis
import jsonpath
import time,datetime,yagmail
import os
from conf import setting
import mlplog
class MySQL:
    def __init__(self,host,user,password,db,port = 3306,charset = "utf8",autocommit = True):
        self.conn = pymysql.connect(host = host,user = user,password = password,db = db,port = port,charset = charset,autocommit = autocommit)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    def execute_many(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()  # [{},{},{}..]
        if res :
            return res

    def excute_one(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()   #{}  查询不到的话，返回的是空的元组（）
        if res:
            return res


    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("连接已关闭...")


def get_redis():
    return redis.Redis(**redis_info)

mysql = MySQL(**mysql_info)
r = get_redis()



def get_key_value(response,key):
        res = jsonpath.jsonpath(response,"$..%s"%key)
        # $..%s这个是jsonpath这个模块的用法   res 是一个list
        if res :
           return res[0]
        return '判断信息：找不到该key 【%s】'%key


def make_today_dir():
    # 创建当天的文件夹，返回绝对路径
    today = time.strftime("%Y-%m-%d")
    abs_path = os.path.join(setting.REPORT_PATH,today)
    if os.path.exists(abs_path):
        pass
    else:
        os.mkdir(abs_path)
    return abs_path



# 打印log

def write_log(conent):
    log_name =os.path.join(setting.LOG_PATH,'test_cj.log')   # 日志文件名
    logger = mlplog.MyLogger(log_name)
    logger.debug(conent)


#################################################################   发邮件
def send_mail(content,file_path=None):
    # 发邮件，传入邮件正文和附件
    m = yagmail.SMTP(** setting.MAIL_INFO)
    subject = '%s_接口测试报告'%str(datetime.datetime.today())
    m.send(subject= subject,to = setting.TO,contents=content,attachments=file_path)




def my_md5(s:str,salt = None):
    s = str(s)
    if salt:
        s = s+salt
    m = hashlib.md5(s.encode())
    return m.hexdigest()




# db = MySQL(host = "127.0.0.1",user ="root",password="root",db="tao")
# sql1 = "select * from meng where username = 'liutao';"
# print(db.excute_one(sql1))
# sql2 = "select * from usering;"
# print(db.execute_many(sql2))



