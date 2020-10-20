import requests
from configs.config import HOST
import json
#md5加密
import hashlib
def get_md5(psw):
    '''
    :param psw: 需要加密的字符串数据
    :return: 加密结果
    '''
    md5 = hashlib.md5()#实例化对象
    md5.update(psw.encode('utf-8'))#加密操作
    return md5.hexdigest()#调用hexdigest方法,获取加密结果


class Login:#登录类
    def login(self,inData,getToken = True):#实例方法---可以直接接收json字符串
        '''
        :param inData: data参数
        :param getToken: 工作模式切换mode
        :return:
                getToken = True：sessionid
                getToken = False:响应数据
        '''
        url = f'{HOST}/account/sLogin'#路径

        # inData = json.loads(inData)#字符串---转化---字典
        inData['password'] = get_md5(inData['password'])  # 参数
        payload = inData

        resp = requests.post(url, data=payload)
        # print('修改前的编码--->', resp.encoding)
        # resp.encoding = 'gbk'
        # print('修改后的编码--->',resp.encoding)#修改后，中文出现乱码，英文不影响，按照接口响应的要求，设置编码
        if getToken:#获取token模式
            return resp.json()['data']['token']
        else:#获取响应数据--返回值是---字典格式
            return resp.json()


if __name__ == '__main__':
    print(Login().login({"username":"sq0777","password":"xintian"},getToken =False))
    #注意事项：inData='''{"username":"sq0001","password":"123456"}'''  必须是json格式，不然不能使用
    #json.loads(inData)会报错