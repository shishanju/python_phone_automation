from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class HomePage(BaseAction):

    # 我 按钮
    me_button = By.XPATH, "//*[@text='我' and @resource-id='com.yunmall.lc:id/tab_me']"

    # 分类 按钮
    category_button = By.XPATH, "//*[@text='分类' and @resource-id='com.yunmall.lc:id/tab_category']"

    # 点击 我
    @allure.step(title='首页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    # 点击 分类
    @allure.step(title='首页 点击 分类')
    def click_category(self):
        self.click(self.category_button)

    # 如果没有登录，则登录
    @allure.step(title='如果没有登录，则登录')
    def login_if_not(self, page):
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":  # 已经登录
            return
        # 登录操作
        page.register.click_login()
        page.login.input_username("itheima_test")
        page.login.input_password("itheima")
        page.login.click_login()

