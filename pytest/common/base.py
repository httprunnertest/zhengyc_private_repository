from time import sleep
from config import BY, Browser, RerunMistakes, ScreenConfig, LogConfig
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import allure
import logging

logging.basicConfig(filename=LogConfig.FileName, level=logging.INFO, format=LogConfig.LOG_FORMAT,
                    datefmt=LogConfig.DATE_FORMAT)


# 报错则重新执行,默认两次
def rerun_times(t=ScreenConfig.Screen_When_Rerun):
    rtime = RerunMistakes(t)

    def rerun_mistake(func):

        def wrapper(self, *args, **kwargs):
            method = func.__name__
            argument = args[1:]
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                rtime.operate()
                logging.warning(f'发送错误{e};尝试执行方法 {method},参数是 {argument}，第{rtime.RerunTimes}次')
                if rtime.RerunTimes != 0:
                    wrapper(self, *args, **kwargs)
                else:
                    rtime.renew(t)
                    if ScreenConfig.Screen_With_Mistake:
                        self.screenshot()
            else:
                rtime.renew(t)

        return wrapper

    return rerun_mistake


# 自动截图
def auto_screenshot(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.screenshot()

    return wrapper


class Base:
    def __init__(self, driver_type=None):
        self.driver = Browser(driver_type).driver

    def __new__(cls, *args, **kwargs):
        if ScreenConfig.Screen_With_Step:
            patt = re.compile(r'__.*?__')
            if ScreenConfig.Screen_With_Step:
                for j in Base.__dict__.keys():
                    if not patt.match(j):
                        setattr(Base, j, auto_screenshot(getattr(Base, j)))
        return object.__new__(cls)

    @auto_screenshot
    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, *args):
        strategy, locator = args
        logging.info(f'     对{strategy}方式定位元素的{locator}进行定位')
        return self.driver.find_element(getattr(BY, strategy.upper()), locator)

    def find_elements(self, *args):
        strategy, locator = args
        return self.driver.find_elements(getattr(BY, strategy.upper()), locator)

    @auto_screenshot
    @rerun_times()
    def input_text(self, text, *args):
        logging.info('尝试进行文本输入')
        ele = self.find_element(*args)
        ele.clear()
        logging.info(f'     对{args[0]}方式定位元素的{args[1]}输入值{text}')
        ele.send_keys(text)

    @auto_screenshot
    @rerun_times()
    def click_ele(self, *args):
        logging.info('尝试进行元素点击')
        ele = self.find_element(*args)
        logging.info(f'     对{args[0]}方式定位元素的{args[1]}进行点击')
        ele.click()
        self.wait_ele(10)
        self.sleep(1)

    def max_window(self):
        self.driver.maximize_window()

    def wait_ele(self, time):
        logging.info(f'隐式等待{time}秒')
        self.driver.implicitly_wait(time)

    def screenshot(self):
        # 截图名称格式调整，不支持冒号
        picture_name = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.png'
        self.driver.get_screenshot_as_file(rf'./reports/{picture_name}')
        with open(rf'./reports/{picture_name}', 'rb')as f:
            file = f.read()
            allure.attach(file, '截图说明', allure.attachment_type.PNG)

    def select_ele(self, value, *args):
        logging.info('尝试进行下拉选择')
        self.click_ele(*args)
        self.click_ele(args[0], value)

    def close(self):
        self.driver.quit()

    def wait_until_ele_visible(self, sec, *args):
        WebDriverWait(self.driver, sec,ignored_exceptions=None).until(EC.presence_of_element_located(args))

    def sleep(self, second):
        logging.info(f'显示等待{second}秒')
        sleep(second)

    def input_text_with_allure(self, step, text, *args):
        logging.info(f'正在进行{step}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        @allure.step(step)
        def itwa():
            self.input_text(text, *args)

        return itwa()

    def select_ele_with_allure(self, step, value, *args):
        logging.info(f'正在进行{step}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        @allure.step(step)
        def sewa():
            self.select_ele(value, *args)

        return sewa()

    def click_ele_with_allure(self, step, *args):
        logging.info(f'正在进行{step}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        try:
            self.wait_until_ele_visible(10, *args)
        except Exception as e:
            logging.error(f'未找到元素{args}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.screenshot()
            raise e
            
        @allure.step(step)
        def cewa():
            self.click_ele(*args)

        return cewa()
