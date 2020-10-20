#-*- coding: utf-8 -*-
#@File    : test_login.py
#@Time    : 2020/9/28 20:23
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import pytest
from lib.apiLib.login import Login
from tools.getExcelData import get_excelData2
from tools.getYamlData import get_yaml_data
import allure
import json,os
from tools.logBasic import logger
log = logger()#调用自定义封装的log函数
#1- 封装测试类
@allure.epic('外卖系统---史诗级别epic')
@allure.feature('登录模块')
class TestLogin:
    #[({},{}),({},{})]
    #@pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    @pytest.mark.parametrize('inData,respData',get_excelData2('登录模块','Login'))  # parametrize('变量'，值)
    def test_login(self,inData,respData):
        #1- 调用--封装模块
        res=Login().login(inData,getToken=False)
        print(res)
        log.info('------##############------------')
        #2- 断言  实际结果与预期的结果进行比较
        try:
            assert res['msg'] == respData['msg']
        except Exception as err:
            log.error(err)#
            raise err#抛出异常


if __name__ == '__main__':
    for one in os.listdir('../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../report/tmp/{one}')
    #-s:输出打印信息； -q  简化输出
    #--alluredir =../report/tmp---生成allure报告需要的源数据
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    #allure generate---生成报告
    #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
    os.system('allure serve ../report/tmp')
    #生成报告