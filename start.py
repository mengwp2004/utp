from  BeautifulReport import BeautifulReport as bf
import unittest
from conf.setting import CASE_PATH
from core import tools
import time
from core.tools import send_mail
import os

def run_case():
    suite = unittest.TestSuite() # 建测试集合
    print(CASE_PATH)
    cases = unittest.defaultTestLoader.discover(CASE_PATH,'test*.py')# 去某个目录下找测试用例

    for case in cases:
        suite.addTest(case)# 循环把每个文件里面的case加入到测试集合里面

    report = bf(suite)# 运行测试用例

    repoort_curday_dir = tools.make_today_dir()
    filename = "report_%s.html"%time.strftime("%H%M%S")
    report.report(filename=filename,description='抽奖接口测试',log_path= repoort_curday_dir) # 产生报告

    # 发邮件
    case_count = report.success_count+report.failure_count
    report_path = os.path.join(repoort_curday_dir,filename)
    content = '''
    各位好！
        本次测试结果：总共运行%s条用例，通过%s条，失败%s条，详细信息见附件。
         '''
    send_mail(content%(case_count,report.success_count,report.failure_count),report_path)

# 产生报告

run_case()