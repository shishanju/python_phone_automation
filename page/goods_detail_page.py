import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class GoodsDetailPage(BaseAction):

    # 加入购物车 按钮
    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    # 确认 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 加入完成之后的+1提示
    grand_total_text_view = By.ID, "com.yunmall.lc:id/tv_grand_total"

    # 商品标题的特征
    product_title_feature = By.ID, "com.yunmall.lc:id/tv_product_title"

    # 购物车图标
    shop_cart_button = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

    # 点击 加入购物车
    @allure.step(title='商品详情 点击 加入购物车')
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    # 点击 确认
    @allure.step(title='商品详情 点击 确认')
    def click_commit(self):
        self.click(self.commit_button)

    # 点击 购物车图标
    @allure.step(title='商品详情 点击 购物车图标')
    def click_shop_cart(self):
        self.click(self.shop_cart_button)

    def get_spec_name(self):
        return self.get_toast_text("请选择").split(" ")[1]

    def get_grand_total_text(self):
        return self.get_feature_text(self.grand_total_text_view)

    # 获取商品标题的所有文字
    def get_product_title_text(self):
        return self.get_feature_text(self.product_title_feature)

    @allure.step(title='商品详情 选择 所有的规格')
    def choose_spec(self):
        while True:
            # 点击 确认
            self.click_commit()
            if self.is_toast_exist("购物车"):
                break

            # 有没有 "请选择" 的 toast ，如果有，应该选择对应的规格，如果没有，加入成功
            self.click_commit()
            if self.is_toast_exist("请选择"):
                feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % self.get_spec_name()
                self.click(feature)
                time.sleep(2)


    # @allure.step(title='商品详情 选择 所有的规格')
    # def choose_spec(self):
    #     while True:
    #         # 点击 确认
    #         self.click_commit()
    #
    #         # 有没有 "请选择" 的 toast ，如果有，应该选择对应的规格，如果没有，加入成功
    #         if self.is_toast_exist("请选择"):
    #             feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % self.get_spec_name()
    #             self.click(feature)
    #
    #         else:
    #             break
    #
    #         time.sleep(2)



    def is_product_title_exist(self, product_title):
        # 加入的商品的 xpath 的特征
        product_title_feature = By.XPATH, "//*[@text='%s']" % product_title
        return self.is_feature_exist(product_title_feature)
