from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest

class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("address_data", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        postal_code = args["postal_code"]
        toast = args["toast"]

        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址列表 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 收件人
        self.page.edit_address.input_name(name)
        # 新增地址 输入 手机号
        self.page.edit_address.input_phone(phone)
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info(info)
        # 新增地址 输入 邮编
        self.page.edit_address.input_postal_code(postal_code)
        # 新增地址 点击 设为默认地址
        self.page.edit_address.click_default_address()
        # 新增地址 选择区域
        self.page.edit_address.choose_region()
        # 新增地址 点击 保存
        self.page.edit_address.click_save()

        if toast is None:
            # 格式：姓名 + 2个空格 + 电话
            assert self.page.address_list.get_receipt_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)

    def test_edit_address(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 根据 默认标记 判断是否有地址
        if not self.page.address_list.is_default_address_tag_exist():
            # 默认不在，也就是没有任何地址，增加地址
            # 地址列表 点击 新增地址
            self.page.address_list.click_add_address()
            # 新增地址 输入 收件人
            self.page.edit_address.input_name("李四")
            # 新增地址 输入 手机号
            self.page.edit_address.input_phone("16666666666")
            # 新增地址 输入 详细地址
            self.page.edit_address.input_info("三单元 402")
            # 新增地址 输入 邮编
            self.page.edit_address.input_postal_code("200000")
            # 新增地址 点击 设为默认地址
            self.page.edit_address.click_default_address()
            # 新增地址 选择区域
            self.page.edit_address.choose_region()
            # 新增地址 点击 保存
            self.page.edit_address.click_save()

        # 地址列表 点击 默认标记
        self.page.address_list.click_default_address()
        # 编辑地址 输入 收件人
        self.page.edit_address.input_name("李四123")
        # 编辑地址 输入 手机号
        self.page.edit_address.input_phone("16666666666")
        # 编辑地址 输入 详细地址
        self.page.edit_address.input_info("三单元 402")
        # 编辑地址 输入 邮编
        self.page.edit_address.input_postal_code("200000")
        # 编辑地址 选择区域
        region_text = self.page.edit_address.choose_region()
        # 编辑地址 点击 保存
        self.page.edit_address.click_save()

        # 断言 toast 是否弹出
        assert self.page.address_list.is_toast_exist("保存成功")
        # 断言 保存后的 收件人和手机号的信息 是否和之前 输入的一致
        assert self.page.address_list.get_receipt_name_text() == "%s  %s" % ("李四123", "16666666666")

        # 进入默认地址，准备重新判断里面所有的内容
        self.page.address_list.click_default_address()
        # 断言 修改后的文字信息，是不是和输入的一致
        assert self.page.edit_address.get_name_text() == "李四123"
        assert self.page.edit_address.get_info_text() == "三单元 402"
        assert self.page.edit_address.get_phone_text() == "16666666666"
        assert self.page.edit_address.get_postal_code_text() == "200000"
        assert self.page.edit_address.get_region_text() == region_text

    def test_delete_address(self):
        # 在首页判断登录状态，如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()

        # 保证有地址可以删除，然后才能测试删除功能，如果没有，直接报错
        assert self.page.address_list.is_default_address_tag_exist()

        # 保证有地址可以删除，然后才能测试删除功能，如果没有则添加
        # if not self.page.address_list.is_default_address_tag_exist():
        #     # 添加地址
        #     pass

        # 地址管理 删除10次 地址
        self.page.address_list.delete_address_ten_times()

        assert not self.page.address_list.is_default_address_tag_exist()


