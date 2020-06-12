import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class EditAddressPage(BaseAction):

    # 收件人 输入框
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"

    # 手机号 输入框
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"

    # 详细地址 输入框
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"

    # 邮编 输入框
    postal_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"

    # 设为默认地址 按钮
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"

    # 所在地区 按钮
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 省市区的 特征
    area_title_feature = By.ID, "com.yunmall.lc:id/area_title"

    # 保存 按钮
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    # 输入 收件人
    @allure.step(title='编辑地址 输入 收件人')
    def input_name(self, value):
        self.input(self.name_edit_text, value)

    # 输入 手机号
    @allure.step(title='编辑地址 输入 手机号')
    def input_phone(self, value):
        self.input(self.phone_edit_text, value)

    # 输入 详细地址
    @allure.step(title='编辑地址 输入 详细地址')
    def input_info(self, value):
        self.input(self.info_edit_text, value)

    # 输入 邮编
    @allure.step(title='编辑地址 输入 邮编')
    def input_postal_code(self, value):
        self.input(self.postal_code_edit_text, value)

    # 点击 设为默认地址
    @allure.step(title='编辑地址 点击 设为默认地址')
    def click_default_address(self):
        self.click(self.default_address_button)

    # 点击 所在区域
    @allure.step(title='编辑地址 点击 所在区域')
    def click_region(self):
        self.click(self.region_button)

    # 选择 所在区域
    @allure.step(title='编辑地址 选择 所在区域')
    def choose_region(self):
        self.click_region()
        region_text = ""
        while True:
            # 判断 当前页面是不是 省市区选择的页面
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return region_text
            # 找到所有的地区
            areas = self.find_elements(self.area_title_feature)
            # 根据当前所有地区的数量，创建一个随机的下标
            area_index = random.randint(0, len(areas) - 1)
            # 获取点击的元素的文字
            region_text += areas[area_index].text
            # 根据下标获取随机的地区，进行点击
            areas[area_index].click()

            time.sleep(1)

    # 点击 保存
    @allure.step(title='编辑地址 点击 保存')
    def click_save(self):
        self.click(self.save_button)

    # 获取 收件人 文字
    def get_name_text(self):
        return self.get_feature_text(self.name_edit_text)

    # 获取 手机号 文字
    def get_phone_text(self):
        return self.get_feature_text(self.phone_edit_text)

    # 获取 详细地址 文字
    def get_info_text(self):
        return self.get_feature_text(self.info_edit_text)

    # 获取 邮编 文字
    def get_postal_code_text(self):
        return self.get_feature_text(self.postal_code_edit_text)

    # 获取 所在地区 文字
    def get_region_text(self):
        return self.get_feature_text(self.region_button)

