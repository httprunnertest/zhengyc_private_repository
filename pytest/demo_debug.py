import json

from selenium import webdriver
import os
import datetime
import logging
from config import LogConfig
import allure


logging.basicConfig(filename=LogConfig.FileName, level=logging.DEBUG, format=LogConfig.LOG_FORMAT,
                    datefmt=LogConfig.DATE_FORMAT)
# logging.basicConfig(filename=LogConfig.FileName, level=logging.DEBUG, format=LogConfig.LOG_FORMAT,
# datefmt=LogConfig.DATE_FORMAT) logging.debug("This is a debug log.") logging.info("This is a info log.")
# logging.warning("This is a warning log.") logging.error("This is a error log.") logging.critical("This is a
# critical log.")
# os.system('allure generate ./allure/xml -o ./allure/html --clean')


# driver = webdriver.Firefox()
# driver.get('http://10.1.28.186:6002/')
# driver.find_element_by_xpath('//input[@placeholder=" 用户名/手机号 "]').send_keys('zhengyc')
# driver.find_element_by_xpath('//input[@type="password"]').send_keys('Jgjt@2020')
# driver.find_element_by_xpath('//span[text()="登录"]').click()
# driver.maximize_window()
# picture = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# picture =datetime.datetime.strptime(picture,'%d/%b/%Y:%H:%M:%S')
# driver.save_screenshot(rf'./reports/{picture}.png')
# driver.get_screenshot_as_file(rf'../reports/{picture}.png')
# driver.quit()
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//input[@placeholder="搜索菜单"]').send_keys('投标立项')
# driver.find_element_by_xpath('//div[@class="menu-side-search-autocomplete"]/li[@title="综合管理/投标管理/商机管理/投标立项"]').click()
# driver.implicitly_wait(10)
# ele1 = driver.find_elements_by_xpath(
#     '//span[text()="工作桌面"]/ancestor::div[@class="ivu-tabs-nav"]/div[contains(@class,"ivu-tabs-tab")]')
# try:
#     driver.find_element_by_xpath('//span[@class="JGToolbarItem"]').click()
#     sleep(5)
#     ele2 = driver.find_elements_by_xpath(
#         '//span[text()="工作桌面"]/ancestor::div[@class="ivu-tabs-nav"]/div[contains(@class,"ivu-tabs-tab")]')
#     if len(ele2) == len(ele1):
#         raise Exception
# except Exception:
#     driver.find_element_by_xpath('//span[@class="JGToolbarItem"]').click()
# driver.implicitly_wait(10)
#
# class Rerun_time:
#     def __init__(self, time):
#         self.time = time + 1
#
#     def operate(self):
#         self.time = self.time - 1
#
#     def renew(self, t):
#         self.time = t
#
#
# def rerun_times(t):
#     rtime = Rerun_time(t)
#
#     def rerun_mistake(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 print(func.__name__)
#                 print('try', *args[1:])
#                 func(*args, **kwargs)
#             except Exception as e:
#                 rtime.operate()
#                 print(rtime.time)
#                 if rtime.time != 0:
#                     wrapper(*args, **kwargs)
#                 else:
#                     print('截图')
#                     rtime.renew(t)
#
#         return wrapper
#
#     return rerun_mistake
#
#
# class obh:
#     @rerun_times(3)
#     def test(self, i):
#         raise TypeError
#
#     @rerun_times(3)
#     def test23(self):
#         print(2)
#
#     def test3(self):
#         a = 'l'
#         print(3 + a)
#

# kk = obh()
# kk.test(1)
# kk.test(23)

# kk.test(23)

# def __getattribute__(self, item):
#     try:
#         print('未报错')
#         self.
#         return k
#     except Exception:
#         print('已报错')
#         return object.__getattribute__(self, item)
#
#
# def auto_screenshot(func):
#     def wrapper(self, *args, **kwargs):
#         func(self, *args, **kwargs)
#         self.sreenshot()
#
#     return wrapper
#
#
# class Tbase:
#     def __init__(self):
#         subclasses = Tbase.__subclasses__()
#         import re
#         patt = re.compile(r'__.*?__')
#         for i in subclasses:
#             for j in i.__dict__.keys():
#                 if not patt.match(j):
#                     setattr(i, j, auto_screenshot(getattr(i, j)))
#
#     def open(self):
#         print('打开浏览器')
#
#     def get(self):
#         print('获取元素')
#
#     def click(self):
#         print('点击')
#
#     def send(self):
#         print('传值')
#
#     def sreenshot(self):
#         print('截图')
#
#     def __new__(cls, *args, **kwargs):
#         # if cls.__name__ != 'Tbase':
#         #     import re
#         #     patt = re.compile(r'__.*?__')
#         #     for i in cls.__dict__.keys():
#         #         if not patt.match(i):
#         #             setattr(cls, i, auto_screenshot(getattr(cls, i)))
#         return object.__new__(cls)
#
#
# class Tpage(Tbase):
#
#     def send_text(self):
#         self.get()
#         self.send()
#
#     def click_ele(self):
#         self.get()
#         self.click()
#
#     def k(self):
#         self.open()
#         self.get()
#         self.send()
#
#
# class Test(Tpage):
#     def login(self):
#         self.open()
#         self.send_text()
#         self.click_ele()
#
#     def add_item(self):
#         self.click_ele()
#         self.send_text()
#         self.send_text()
#         self.click_ele()
#


def big_dec(co):
    def decorater(func):
        def wrapper(*args, **kwargs):
            print(co)
            func(*args, **kwargs)
            print(co)

        return wrapper

    return decorater


def cl_dec(cname):
    @allure.feature(cname)
    class CK:
        pass

    return CK

#
# CCB = cl_dec('投标立项')
# print(CCB)
'''
def de_ttt(bb):
    @big_dec(bb)
    def ttt(self, action1, strategy1, locator1, value1):
        self.relexf(action1, strategy1, locator1, value1)

    return ttt


# C.test_fun = de_ttt(1)
# k = C()
# k.test_fun(1, 2, 3, 4)


def custom(story, step_list):
    def test_fun(self):
        print(story)
        for i in step_list:
            print(*tuple(i.values()))

    return test_fun


story_num = 1


def ert(a, b, c, d, e=None):
    print(a, b, c, d, e)


C.m = ert

for i in data.DataDict:
    for l in data.DataDict[i]:
        ert(*tuple(l.values()))
    tf = custom(i, data.DataDict[i])
    setattr(C, f'fun{story_num}', tf)
    story_num = story_num + 1
'''
# logging.info("this is info\r")
# logging.debug("this is debug")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")
a={
    '1':'a1',
    '2':'b1'
}
b= ['a2','b2']

from common.mutil_read import MutilRead
c=MutilRead('./data')

dic_json = json.dumps(c.result,ensure_ascii=False,indent=4) #字典转化成json，字典转化成字符串。其中，d，字典；ensure_ascii=False处理中文，去掉的话中文会乱码，indent=4，json格式缩进字节数
print(dic_json)