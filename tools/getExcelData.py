#-*- coding: utf-8 -*-
#@File    : getExcelData.py
#@Time    : 2020/9/27 20:44
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
# xlrd  openpyxl
import xlrd  #pip  install xlrd
from xlutils.copy import copy
import json
#1- 打开excel表
def get_excelData(sheetName,startRow,endRow):
    resList = []
    #1-excel表路径
    excelDir = '../data/外卖系统接口测试用例.xls'
    #2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    # workSheetNames = workBook.sheet_names()#获取所有的表名
    # print(workSheetNames)
    #3- 获取某一个指定的表
    workSheet = workBook.sheet_by_name(sheetName)
    #4- 读取单元格---返回是字符串---cell(行号，列号)  从0开始
    for one in range(startRow-1,endRow):
        reqBodyData = workSheet.cell(one,9).value#请求body
        respData =  workSheet.cell(one,11).value#响应数据
        resList.append((reqBodyData,respData))#封装一个列表里嵌套元组
    return resList

#可以自动识别用例数
def get_excelData2(sheetName,caseName):
    '''
    :param sheetName: 表名
    :param caseName: 某一个接口的用例名称
    :return:
    '''
    resList = []
    #1-excel表路径
    excelDir = '../data/外卖系统接口测试用例.xls'
    #2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    # workSheetNames = workBook.sheet_names()#获取所有的表名
    # print(workSheetNames)
    #3- 获取某一个指定的表
    workSheet = workBook.sheet_by_name(sheetName)
    #4- 读取一列数据
    # print(workSheet.col_values(0))
    idx=0#开始的下标
    for one in workSheet.col_values(0):
        if caseName in one:
            reqBodyData = workSheet.cell(idx,9).value#请求body
            respData =  workSheet.cell(idx,11).value#响应数据
            resList.append((json.loads(reqBodyData),json.loads(respData)))#封装一个列表里嵌套元组
        idx += 1#
    return resList

    # for one in range(startRow-1,endRow):
    #     reqBodyData = workSheet.cell(one,9).value#请求body
    #     respData =  workSheet.cell(one,11).value#响应数据
    #     resList.append((reqBodyData,respData))#封装一个列表里嵌套元组
    # return resList


def set_excelData():
    #1-excel表路径
    excelDir = '../data/外卖系统接口测试用例.xls'
    #2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workBookNew = copy(workBook)#复制一个新excel文件对象
    workSheetNew = workBookNew.get_sheet(0)#取复制出来的新excel文件对象的第一个子表
    return workBookNew,workSheetNew#复制出来的excel对象，复制出来excel对象的第一个子表


if __name__ == '__main__':
    # print(get_excelData2('登录模块','Login'))
    for one in get_excelData2('登录模块','Login'):
        print(one)
