import unittest
import mlplog
import os
from conf import setting
from core.my_requests import MyRequests
from core.tools import mysql,get_key_value
from core.tools import r as red
from core.tools import write_log
class CJ(unittest.TestCase):

    username = 'mengliping'
    passwd = '123456'
    def reg(self):
        '''注册接口'''
        url = "/regpost"
        url = setting.default_host +url
        data = {
            'username':self.username,
            'passwd':self.passwd,
            'cpwd':self.passwd
        }
        my_request = MyRequests(url,data)
        result = my_request.post() #{"status":1,"data":req.json()}
        self.assertEqual(1,result.get('status'),msg='注册接口调用失败，失败信息：%s'%result.get('data'))# 断言，如果不成功，直接停止运行程序。
        # 接口返回校验
        res = result.get('data')  #  {"error_code":0,"msg":"注册成功"}
        self.assertEqual(0,res.get('error_code'),msg = '没有注册成功！%s'%res)
        # 查看数据库
        sql = "select * from app_user where username = '%s';"%self.username
        res = mysql.excute_one(sql)
        self.assertIsNotNone(res,msg = "数据库没有查到用户名")
        write_log("reg--------------%s"%res)

    def login(self):
        '''登录接口'''
        url = "/loginpost"
        url = setting.default_host +url
        data = {
            'username':self.username,
            'passwd':self.passwd
        }
        my_request = MyRequests(url,data)
        result = my_request.post() #{"status":1,"data":req.json()}
        self.assertEqual(1,result.get('status'),msg='登录接口调用失败，失败信息：%s'%result.get('data'))
        # 接口返回校验
        res = result.get('data')
        # 接口校验成功后，拿到sign
        sign = get_key_value(res,'sign')
        self.assertIsNotNone(sign,msg = '登录失败 %s'%res)
        # 登录成功，拿到"userId":1,
        userId = get_key_value(res,'userId')
        write_log("login--------------%s"%res)
        return sign,userId

    def choujiang(self):
        '''抽奖接口'''
        url = "/choujiangget"
        url = setting.default_host +url
        sign,userid = self.login()

        data = {
            'userid':userid,
            'sign':sign
        }
        print("************************************************")
        my_request = MyRequests(url,data)
        print("************************************************")
        result = my_request.get() #{"status":1,"data":req.json()
        print(result)
        self.assertEqual(1,result.get('status'),msg='抽奖接口调用失败，失败信息：%s'%result.get('data'))

    # 接口返回校验
        res = result.get('data')
        self.assertEqual(0,res.get("error_code"),msg="抽奖返回json不对 %s"%res)

        # 1、redis校验
        redis_key = "choujiang:%s"%self.username
        count = red.get(redis_key)# 从redis中拿到的值都是字符串
        write_log("redis存的值count--------------%s"%count)
        self.assertEqual("1",count,msg= "抽奖次数错误 %s"%result)
        # 2、数据库校验
        sql = "select count(*) as cishu from app_record where userid =%s;"%userid
        cishu =mysql.excute_one(sql).get('cishu')
        self.assertEqual(1,cishu,msg="抽奖记录没有落到数据库里面！")

        write_log("choujiang--------------%s"%res)


    def test_choujiang(self):# 只执行test开头的函数
        '''抽奖流程'''
        self.reg()
        self.choujiang()

    # @classmethod
    # def tearDownClass(cls):
    #     ### 数据清除的工作
    #     sql = 'delete from app_user where username ="%s";'%cls.username
    #     mysql.excute_one(sql)
    #     key = 'choujiang:%s'%cls.username
    #     red.delete(key)
    #     print("测试数据清理完成。。")







































