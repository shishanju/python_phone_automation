from base.base_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_update(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 关于百年奥莱
        self.page.setting.click_about()
        # 关于 点击 版本更新
        self.page.about.click_update()

        # 断言 "当前已是最新版本" 的 toast 是不是出现在屏幕上
        assert self.page.about.is_toast_exist("当前已是最新版本")