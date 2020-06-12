from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class AddressListPage(BaseAction):

    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 地址的 收件人和电话组成的标题 的特征
    receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认 标记
    default_address_tag = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 删除 按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确认按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 点击 新增地址
    @allure.step(title='地址列表 点击 新增地址')
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取 地址的 收件人和电话组成的标题 的文字内容
    # 使用的是 find_element 的方法，第一个也就是默认的地址的信息
    def get_receipt_name_text(self):
        return self.get_feature_text(self.receipt_name_text_view)

    # 默认标记是否存在
    def is_default_address_tag_exist(self):
        return self.is_feature_exist(self.default_address_tag)

    # 点击 默认标记
    @allure.step(title='地址列表 点击 默认标记')
    def click_default_address(self):
        self.click(self.default_address_tag)

    # 点击 编辑 按钮
    @allure.step(title='地址列表 点击 编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 点击 删除 按钮
    @allure.step(title='地址列表 点击 删除')
    def click_delete(self):
        self.click(self.delete_button)

    # 点击 确认 按钮
    @allure.step(title='地址列表 点击 确认')
    def click_commit(self):
        self.click(self.commit_button)

    # 在列表界面 删除一个地址
    def delete_address(self):
        self.click_edit()
        self.click_delete()
        self.click_commit()

    @allure.step(title='地址列表 删除 十次地址')
    def delete_address_ten_times(self):
        for i in range(10):
            self.click_edit()
            try:
                self.click_delete()
            except Exception:
                return
            self.click_commit()
