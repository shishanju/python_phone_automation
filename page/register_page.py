from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class RegisterPage(BaseAction):

    # 跳转到登录页面 按钮
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    # 点击 跳转到登录页面
    @allure.step(title='注册 点击 跳转到登录页面')
    def click_login(self):
        self.click(self.login_button)