# 变量名字大写 代表 常量
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# atp目录
#BASE_PATH = os.path.dirname(os.getcwd()) # atp目录
LOG_PATH = os.path.join(BASE_PATH,"log")# log目录
CASE_PATH = os.path.join(BASE_PATH,"cases") # case目录
REPORT_PATH = os.path.join(BASE_PATH,"report") # report 目录
DATA_PATH = os.path.join(BASE_PATH,"data") # 存放参数化文件的目录
SQL_PATH = os.path.join(BASE_PATH,"sql_file")# sql_file

MAIL_INFO = {
    'user':"957732026@qq.com",
    'password':"rzqugjjkupghbddc",
    'host':'smtp.qq.com',
    'smtp_ssl':True  # 默认是False，非qq，是False
}
TO = ['1032016506@qq.com','13764172557@163.com']

HOST = {
    'QA':"http://192.168.124.6:9000",# 测试环境
    'DEV':'http://dev.nnzhp.cn',# 开发环境
    'PRE':'http://pre.nnzhp.cn'# 预生产环境
}

default_host = HOST.get('QA')

mysql_info = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"root",
    "db":"tao",
    "charset":"utf8",
    "autocommit":True
}

redis_info = {
    "host":"192.168.153.131",
    "port":6379,
    "password":"mlpwawj123",
    "db":1,
    "decode_responses":True
}

