import time
import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):

        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 首页 点击 我
        self.page.home.click_me()
        # 注册 点击 已有账号去登陆
        self.page.register.click_login()
        # 登录 输入 用户名
        self.page.login.input_username(username)
        # 登录 输入 密码
        self.page.login.input_password(password)
        # 登录 点击 登录
        self.page.login.click_login()

        if toast is None:  # 如果 toast 为 none，表示 登录成功的断言
            assert self.page.me.get_username_text() == "itheima_test"
            assert self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity"
        else: # 如果 toast 有值，表示 预期失败，通过toast的内容断言
            assert self.page.login.is_toast_exist(toast)
