#-*- coding: utf-8 -*-
#@File    : getYamlData.py
#@Time    : 2020/10/11 9:15
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import yaml
# def get_yaml_data(fileDir):
#     #1-打开yaml文件
#     fo = open(fileDir,'r',encoding='utf-8')
#     #2- 使用第三方库去获取
#     res = yaml.load(fo,Loader=yaml.FullLoader)#处理警告
#     print(res)


# def get_yamls_data(fileDir):
#     '''
#     des：一个yaml文件内包含多个yaml数据
#     :param fileDir:
#     :return:
#     '''
#     #1-打开yaml文件
#     fo = open(fileDir,'r',encoding='utf-8')
#     #2- 使用第三方库去获取
#     res = yaml.load_all(fo,Loader=yaml.FullLoader)#处理警告
#     for one in res:
#         print(one)

def get_yaml_data(fileDir):
    '''
    思路：原则：尽量少动代码
        目标：函数的返回的结果与之前的excel方案数据一致
        1- 获取什么数据
            data
            resp
        2- 数据该如何组装返回
            分析：框架pytest需要什么格式数据
                1- 列表格式 [(),()]
                2- 要求是字典格式：
                    回顾：以前的读取excel的数据，记得在excel的函数里做了一步
                    操作：json---转化---字典
    :param fileDir:
    :return: [(字典1，字典2),(字典1，字典2)]
    '''
    #1-打开yaml文件
    resList = []
    fo = open(fileDir,'r',encoding='utf-8')
    #2- 使用第三方库去获取
    res = yaml.load(fo,Loader=yaml.FullLoader)#处理警告
    for one in res:
        resList.append((one['data'],one['resp']))
    return resList

if __name__ == '__main__':
    print(get_yaml_data('../data/data.yaml'))