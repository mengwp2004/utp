import unittest
#import nose_parameterized 改名字了parameterized
from conf.setting import DATA_PATH
import os
from core.parse_param_file import textFileToList
from parameterized import parameterized
def login(username,password):
    print(username,password)
    print("========================")
    return 1

# data_file_path = os.path.join(DATA_PATH,"abc_data.txt")
# with open(data_file_path,"r",encoding='utf-8')as fr:
#     res = fr.read()
#     print(res)



class MyTest(unittest.TestCase):
    # 第三个参数是 检查点
    # @parameterized.expand(
    # [
    #     ['mengliping','123','success'],
    #     ['liutao','345','2'],
    #     ['geda','789',1]
    # ])
    # def test_login(self,username,password,check):
    #     login(username,password)
    #     self.assertEqual(1,check,msg="不对")

    @parameterized.expand(textFileToList("abc_data.txt"))
    def test_login(self,username,password,check):
        '''参数化用户名和密码登陆'''
        login(username,password)
        self.assertEqual('1',check,msg="不对")


#不能写unittest.main()，否则只执行这里的，不会执行start