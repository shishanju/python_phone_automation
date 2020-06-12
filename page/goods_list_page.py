import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class GoodsListPage(BaseAction):

    # 分类中的进入物品列表的特征
    goods_detail_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    # 随机点击一个物品，进入物品的详情
    @allure.step(title='商品列表 随机点击一个物品，进入物品的详情')
    def click_goods_detail(self):
        buttons = self.find_elements(self.goods_detail_button)
        button_index = random.randint(0, len(buttons) - 1)
        buttons[button_index].click()