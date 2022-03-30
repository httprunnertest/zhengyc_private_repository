import os

import pytest
import logging
from common.zjg import ZjgPage
from common.mutil_read import MutilRead
import allure


def custom_fun(story, title, step_list):
    @allure.story(story)
    @allure.title(title)
    def test_fun(self):
        for i in step_list:
            self.reflex(i.get('操作步骤'), i.get('操作'), i.get('定位方式'), i.get('定位内容'), i.get('输入值/定位'))

    return test_fun


def cl_dec(cname):
    @allure.feature(cname)
    class TXlsx:
        browser = ZjgPage()

    TXlsx.reflex = reflex

    return TXlsx


def setup_module():
    logging.info('删除旧文件')
    os.system('clear.bat')


def teardown_module():
    logging.info('测试完成')


def reflex(self, step, action, strategy=None, locator=None, value=None):
    if action == '初始化':
        self.browser.get_url(value)
        self.browser.max_window()
    if action == '输入':
        self.browser.input_text_with_allure(step, value, strategy, locator)
    if action == '点击':
        self.browser.click_ele_with_allure(step, strategy, locator)
    if action == '下拉选择':
        self.browser.select_ele_with_allure(step, value, strategy, locator)
    if action == '关闭':
        self.browser.close()


story_num = 1
feature_num = 1

data = MutilRead('./data')
createTestCls = locals()
for filename in data.filename:
    createTestCls['TestXlsx' + str(feature_num)] = cl_dec(filename)
    for sheetname, sheetcontent in data.result[filename].items():
        for bigstepName, bigstepList in sheetcontent.items():
            setattr(createTestCls['TestXlsx' + str(feature_num)], f'test_story_{story_num}',
                    custom_fun(sheetname, bigstepName, bigstepList))
            story_num = story_num + 1
    feature_num = feature_num + 1

if __name__ == '__main__':
    pytest.main()
