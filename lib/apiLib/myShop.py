#-*- coding: utf-8 -*-
#@File    : myShop.py
#@Time    : 2020/9/28 21:07
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
from configs.config import HOST
import requests
from lib.apiLib.login import Login
import pprint
class MyShop:
    #1- 需要操作商铺--需要token
    def __init__(self,inToken):
        self.header = {'Authorization':inToken}#请求头

    #2- 列出商铺
    def shop_list(self,inData):
        payload = inData
        url = f'{HOST}/shopping/myShop'
        resp = requests.get(url,headers = self.header,params=payload)
        return resp.json()#响应数据

    #3-文件上传接口
    def file_upload(self,fileName,fileDir):
        '''
        :param fileName: 文件名
        :param fileDir: 文件路径
        :return:
        '''
        #组装文件对象  (文件名，文件对象open(路径，打开方式)，文件类型)
        user_file = {'file':(fileName,open(fileDir,'rb'),'image/png')}
        #多个文件接口：{"文件名1":(),"文件名2":(),"文件名3":()}
        resp = requests.post(f'{HOST}/file',files=user_file,headers=self.header)
        return resp.json()['data']['realFileName']#图片信息

    #4- 编辑商铺
    #需要2个数据：  商铺的id   ,图形信息---实时数据
    def shop_update(self,inData,shopId,imageInfo):
        '''
        :param inData:用例数据
        :param shopId:商铺的id
        :param imageInfo:图形信息
        :return:
        '''
        inData['id'] = shopId#更新店铺id
        inData['image_path'] = imageInfo  # 更新图片信息
        inData['image'] = f"{HOST}/file/getImgStream?fileName={imageInfo}"  # 更新图片信息
        payload = inData
        url = f'{HOST}/shopping/updatemyshop'
        resp = requests.post(url,headers = self.header,data=payload)
        return resp.json()#响应数据

if __name__ == '__main__':
    #1- 登录成功
    token = Login().login({"username":"sq0001","password":"123456"},getToken=True)
    #2- 列出商铺--id
    res=MyShop(token).shop_list({'page':1,'limit':20})
    id=res['data']['records'][0]['id']
    #3-文件上传
    res = MyShop(token).file_upload('123.png','../../data/123.png')
    #4- 编辑商铺
    pprint.pprint(res)
