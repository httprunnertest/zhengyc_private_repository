from selenium import webdriver
import datetime


class LogConfig:
    datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    FileName = f"./log/{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"


"""
自动截图设置，默认错误时截图
1.错误时截图
2.每一步截图，点击，提交
"""


class ScreenConfig:
    Screen_When_Rerun = 2
    Screen_With_Mistake = False
    Screen_With_Step = False


class RerunMistakes:

    def __init__(self, RerunTimes):
        self.RerunTimes = RerunTimes + 1

    def operate(self):
        self.RerunTimes = self.RerunTimes - 1

    def renew(self, init_time):
        self.RerunTimes = init_time + 1


class BY:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG = "tag name"
    CLASS = "class name"
    CSS = "css selector"


class Browser:
    def __init__(self, driver_type):
        if not driver_type:
            self.driver = webdriver.Chrome()
        else:
            self.switch_to_driver_type(driver_type)

    def switch_to_driver_type(self, driver_type):
        if driver_type == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver_type == 'firefox':
            self.driver = webdriver.Firefox()
        elif driver_type == 'ie':
            self.driver = webdriver.Ie()
