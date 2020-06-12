import time

from base.base_driver import init_driver
from page.page import Page
from selenium.webdriver.common.by import By

class TestShopCartCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_shop_cart(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 首页 点击 分类
        self.page.home.click_category()
        # 分类 随机点击 物品列表
        self.page.category.click_goods_list()
        # 物品列表 随机点击 物品详情
        self.page.goods_list.click_goods_detail()

        # 记录一下，当前商品的标题，后去作为断言的参考
        product_title = self.page.goods_detail.get_product_title_text()

        # 物品详情 点击 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 选择所有应该选择的规格
        self.page.goods_detail.choose_spec()

        # 断言 是否有 成功加入的 toast 提示
        assert self.page.goods_detail.is_toast_exist("成功加入购物车")
        # 断言 增加后这个购物车标记 是否有 +1 字样
        assert self.page.goods_detail.get_grand_total_text() == "+1"

        # 商品详情 点击 购物车
        self.page.goods_detail.click_shop_cart()

        # 断言 准备加入购物车的商品 是不是在 购物车里的标题内容之中
        assert self.page.goods_detail.is_product_title_exist(product_title)



