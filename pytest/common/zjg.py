import allure

from common.base import Base


class ZjgPage(Base):
    # 文本输入。参数name属性和输入值
    def zjg_input_text(self, name, value):
        self.input_text(value, 'xpath', f'//input[@name="{name}"]')
        self.input_text(value, 'xpath', f'//input[@name="{name}"]')

    # 下拉框选择，有部分下拉框需要点击两次。参数定位的name属性和下拉值
    def zjg_select_ele_twice(self, name, value):
        self.click_ele('xpath', f'//input[@name="{name}"]/parent::td/following-sibling::td')
        self.click_ele('xpath', f'//input[@name="{name}"]/parent::td/following-sibling::td')
        self.click_ele('xpath', f'//tr[@role="option"]/td/div[text()="{value}"]')

    # 下拉框选择。参数定位的name属性和下拉值
    def zjg_select_ele(self, name, value):
        self.click_ele('xpath', f'//input[@name="{name}"]/parent::td/following-sibling::td')
        self.click_ele('xpath', f'//tr[@role="option"]/td/div[text()="{value}"]')

    # 长文本输入。参数name属性和输入值
    def zjg_input_textarea(self, name, value):
        self.input_text(value, 'xpath', f'//textarea[@name="{name}"]')

    # 点击按钮。参数按钮名称
    def zjg_click_button(self, btname):
        self.click_ele('xpath', f'//td[text()="{btname}"]')
        self.sleep(5)

    def zjg_try_except_click(self, *locator):
        # 查看当前页签，和按钮点击之后做对比，如果按钮点击没有生成新的页签则抛出错误
        ele1 = self.find_elements('xpath', '//span[text()="工作桌面"]/ancestor::div[@class="ivu-tabs-nav"]/div['
                                           'contains(@class,"ivu-tabs-tab")]'
                                  )
        try:
            self.click_ele(*locator)
            ele2 = self.find_elements('xpath', '//span[text()="工作桌面"]/ancestor::div[@class="ivu-tabs-nav"]/div['
                                               'contains(@class,"ivu-tabs-tab")]'
                                      )
            if len(ele2) == len(ele1):
                raise Exception
        except Exception as e:
            self.click_ele(*locator)

    def select_ele_twice_with_allure(self, step, value, *args):
        @allure.step(step)
        def cetwa():
            self.click_ele(*args)
            self.click_ele(*args)
            self.click_ele(args[0], value)
        return cetwa()
