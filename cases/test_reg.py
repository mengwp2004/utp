import unittest
from core.parse_param_file import textFileToList,excelToList
from core.my_requests import MyRequests
from conf.setting import default_host
from core.tools import get_key_value

from parameterized import parameterized
class RegTest(unittest.TestCase):
    # @parameterized.expand(textFileToList("reg_data.txt",seq = ','))
    @parameterized.expand(excelToList("excel_data.xls"))
    def test_login(self,username,password,key,check):
        '''参数化登录啊啊啊啊啊啊'''
        url = default_host +"/loginpost"
        data = {
            "username":username,
            "passwd":password
        }

        r = MyRequests(url,data)
        result = r.post()
        self.assertEqual(1,result["status"],msg="请求数据调用post接口失败！%s"%result)
        reponse = result["data"]
        real_res = get_key_value(reponse,key)
        self.assertEqual(check,str(real_res),msg="登录失败！%s"%reponse)



