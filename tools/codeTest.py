#-*- coding: utf-8 -*-
#@File    : codeTest.py
#@Time    : 2020/10/14 20:20
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
import sys
#工具设置的编码
# print(sys.getdefaultencoding())

# #字符串---unicode
# str1 = '大家好'
# res = str1.encode('utf-8')#  编码：字符串--变成---字节码
# print(res)
# res2 = res.decode('utf-8')#解码 字节码--变成---字符串
# print(res2)


#---------------------装饰器------------------------
'''
需求：领导想知道，该测试用例执行foo，服务器的响应时间是多少，我们怎么实现该代码？
'''
import time
# def foo():
#     print('--测试用例执行---')
#     time.sleep(1)
#方案一：
'''
开始计时
foo()
结束计时
'''
# def show_time(func):
#     start_time = time.time()
#     func()# foo()函数运行
#     end_time = time.time()
#     print('该服务器响应时间: ',end_time-start_time)
#
# show_time(foo)#函数名本身就是一个对象

'''
方案一复盘：
    1- 逻辑简单，需求可以完成
    2- 缺点：直接修改了代码原有的执行方法
优化：是否有一种办法。不改变foo()方式，能不能使show_time()函数有一个返回值
'''
# def show_time(func):
#     def inner():
#         start_time = time.time()
#         func()# foo()函数运行
#         end_time = time.time()
#         print('该服务器响应时间: ',end_time-start_time)
#     return inner #函数对象
#
# foo=show_time(foo) # foo = inner  变量= 函数对象
# foo() #函数调用，以前其他模板调用这个方法，不需要修改任何代码！

'''
方案二：复盘
    foo=show_time(foo)  每一次都得重新赋值，麻烦
    @  语法糖--方案三
'''
# def show_time(func):
#     def inner():
#         start_time = time.time()
#         func()# foo()函数运行
#         end_time = time.time()
#         print('该服务器响应时间: ',end_time-start_time)
#     return inner #函数对象
#
#
# @show_time  #foo=show_time(foo) # foo = inner  变量= 函数对象
# def foo():
#     print('--测试用例执行---')
#     time.sleep(1)
#
# @show_time
# def fo2():
#     print('--测试用例执行2---')
#     time.sleep(1)
# # foo=show_time(foo) # foo = inner  变量= 函数对象
# foo() #函数调用，以前其他模板调用这个方法，不需要修改任何代码！
# fo2()

#扩展知识点---带参数装饰器
#需要知道是谁运行了这个测试用例的，怎么办
def some_body_run(name):
    def show_time(func):
        def inner():
            start_time = time.time()
            func()# foo()函数运行
            end_time = time.time()
            print('该服务器响应时间: ',end_time-start_time)
            print('该测试用例地执行是--->',name)
        return inner #函数对象
    return show_time


@some_body_run('tom')  #foo=some_body_run('tom') # foo = inner  变量= 函数对象
def foo():
    print('--测试用例执行---')
    time.sleep(1)


# foo=show_time(foo) # foo = inner  变量= 函数对象
foo() #函数调用，以前其他模板调用这个方法，不需要修改任何代码！

