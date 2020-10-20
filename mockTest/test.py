#-*- coding: utf-8 -*-
#@File    : test.py
#@Time    : 2020/10/12 20:36
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
# import requests
# url = 'http://127.0.0.1:9999/demo2'
# payload = {'key1':'abc','key2':'123'}
# resp = requests.get(url,params=payload)
# print(resp.text)

# import requests
# from configs.config import HOST
# import json
# #md5加密
# import hashlib
# def get_md5(psw):
#     '''
#     :param psw: 需要加密的字符串数据
#     :return: 加密结果
#     '''
#     md5 = hashlib.md5()#实例化对象
#     md5.update(psw.encode('utf-8'))#加密操作
#     print(md5.hexdigest())
#     return md5.hexdigest()#调用hexdigest方法,获取加密结果
#
#
# class Login:#登录类
#     def login(self,inData,getToken = True):#实例方法---可以直接接收json字符串
#         '''
#         :param inData: data参数
#         :param getToken: 工作模式切换mode
#         :return:
#                 getToken = True：sessionid
#                 getToken = False:响应数据
#         '''
#         url = 'http://127.0.0.1:9999/account/sLogin'#路径
#
#         # inData = json.loads(inData)#字符串---转化---字典
#         inData['password'] = get_md5(inData['password'])  # 参数
#         payload = inData
#         resp = requests.post(url, data=payload)
#         if getToken:#获取token模式
#             return resp.json()['data']['token']
#         else:#获取响应数据--返回值是---字典格式
#             # return resp.json()
#             return resp.text
#
#
# if __name__ == '__main__':
#     print(Login().login({"username":"sq0777","password":"xintian"},getToken =False))
#     #注意事项：inData='''{"username":"sq0001","password":"123456"}'''  必须是json格式，不然不能使用
#     #json.loads(inData)会报错

#-------------------------------------------------------------------------------
import requests
HOST = 'http://127.0.0.1:9999'
#1- 编写提交申请接口函数
def create_order():
    url = f'{HOST}/api/order/create/'
    payload = {
                "user_id": "sq001",
                "goods_id": "20201012",
                "num": 2,
                "amount": 100.8
    }
    resp = requests.post(url,json=payload)
    return resp.json()['order_id']# 返回是字典数据
#2- 编写查询结果函数---有点难度----什么时候处理好，你得自己查询，要考虑一个超时的机制
#机制：查询的频率（隔多久查询一次）：多少时间超时
import time
def get_order_result(orderId,interval = 5,time_out=30):#time_out= 30s
    '''
    :param orderId: id
    :param interval: 查询频率 5s查询频率
    :param time_out: 查询的超时时间
    :return:
    '''
    payload = {'order_id':orderId}#封装数据
    url = f'{HOST}/api/order/get_result01/'

    #1- 开始查询时间--记录下
    start_time = time.time()
    #2- 结束的时间--要不设定下---超时多少不在查询-----开始时间+你设定的超时时间
    end_time = start_time+time_out
    #3- 在一定时间内进行循环查询
    cnt =0#计数变量
    while time.time() < end_time:
        resp = requests.get(url,params=payload)#
        cnt += 1#计数变量
        print(f'第{cnt}次查询','结果是:--->',resp.text)
        #5- 如果接口响应比较快--很短时间就响应数据了
        if resp.text:
            break
        #4- 设置查询的频率
        time.sleep(interval)
    return resp.text

if __name__ == '__main__':
    print(get_order_result(create_order()))




















