#-*- coding: utf-8 -*-
#@File    : logBasic.py
#@Time    : 2020/10/14 21:30
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import logging

#对日志设置
'''
1- 存放路径
2- 日志文件名
3- 内容格式：format
    2020_10_14.21.34.24 - logBasic.py [代码错误的行号] 级别：具体内容
    执行时间 文件名 【报错行号】 等级 msg(具体信息)

'''
import datetime
def logger():
    '''
    logging.basicConfig函数各参数：
    filename：指定日志文件名；
    filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
    format：指定输出的格式和内容，format可以输出很多有用的信息，
    level logging.INFO,#
    '''
    #调用配置函数
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s',
                        filename= f'../logs/{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.txt',
                        level='INFO',#
                        filemode='a'
    )
    return logging

if __name__ == '__main__':
    log = logger()
    log.error('---hello---')

'''
debug：最细微的信息记录到debug中，这个级别就是用来debug的，看程序在哪一次迭代中发生了错误，比如每次循环都输出一些东西用debug级别
info：级别用于routines，也就是输出start finish 状态改变等信息
warn：输出一些相对重要，但是不是程序bug的信息，比如输入了错误的密码，或者连接较慢
error：输出程序bug，打印异常信息
critical：用于处理一些非常糟糕的事情，比如内存溢出、磁盘已满，这个一般较少使用
'''