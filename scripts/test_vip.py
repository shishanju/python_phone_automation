import time
import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
from selenium.webdriver.support.ui import WebDriverWait


class TestVip:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("vip_data", "test_vip"))
    def test_vip(self, args):

        keyword = args["keyword"]
        toast = args["toast"]

        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_vip()
        print(self.driver.contexts)
        # 切换到对应的 webview
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite_code(keyword)
        # vip 点击 成为vip
        self.page.vip.click_be_vip()

        assert self.page.vip.is_can_not_be_vip(toast)

        # 切换到原生的环境
        self.driver.switch_to.context("NATIVE_APP")



