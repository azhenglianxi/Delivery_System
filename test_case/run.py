#-*- coding: utf-8 -*-
#@File    : run.py.py
#@Time    : 2020/10/11 7:49
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import pytest
import allure
import os
if __name__ == '__main__':
    for one in os.listdir('../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../report/tmp/{one}')
    # pytest.main(['test_myShop.py', '-s', '--alluredir', '../report/tmp'])
    print(__file__)
    print(os.getcwd())#当前路径
    pytest.main(['test_login.py','test_myShop.py','-s', '-v', '--alluredir', '../report/tmp'])
    os.system('allure serve ../report/tmp')