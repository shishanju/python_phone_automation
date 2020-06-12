import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class VipPage(BaseAction):

    # 邀请码 输入框
    invite_code_edit_text = By.XPATH, "//input[@type='tel']"

    # 成为会员 按钮
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    # 输入 邀请码
    @allure.step(title='vip 输入 邀请码')
    def input_invite_code(self, value):
        self.input(self.invite_code_edit_text, value)

    # 点击 成为会员
    @allure.step(title='vip 点击 成为会员')
    def click_be_vip(self):
        self.click(self.be_vip_button)


    def is_can_not_be_vip(self, cond, timeout=3, poll=0.1):
        """
        判断 网页的 div 是不是包含 cond 内容
        :param cond:
        :param timeout:
        :param poll:
        :return:
        """
        return self.is_keyword_in_page_source(cond, timeout, poll)

