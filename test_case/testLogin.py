#-*- coding: utf-8 -*-
#@File    : testLogin.py
#@Time    : 2020/9/27 21:32
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import json
#1- 读取数据
from tools.getExcelData import get_excelData,set_excelData
workBookNew,workSheetNew = set_excelData()#元组
#2- 关联请求
dataList = get_excelData('登录模块',2,7)#[(请求body，响应数据),(),()]
from lib.apiLib.login import Login
for one in range(0,len(dataList)):#one---元组--(请求body，响应数据)
    res=Login().login(dataList[one][0],False)#实际响应结果
    #预期与实际的响应数据进行比较
    if res['msg'] == json.loads(dataList[one][1])['msg']:
        print('---pass---')
        #列表.index(元素)---求出该元素的下标
        workSheetNew.write(one+1,12,'pass')#(行号，列号，字符串内容)
    else:
        print('---fail---')
        workSheetNew.write(one + 1, 12, 'fail')
workBookNew.save('../data/res.xls')
#3- 写结果

