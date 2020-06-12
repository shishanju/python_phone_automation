import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def find_elements(self, feature, timeout=10, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature):
        self.find_element(feature).click()

    def clear(self, feature):
        self.find_element(feature).clear()

    def input(self, feature, value):
        self.clear(feature)
        self.find_element(feature).send_keys(value)

    def is_feature_exist(self, feature):
        """
        根据特征，判断这个特征是不是在当前屏幕上
        :param feature: 特征
        :return:
        """
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def get_feature_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self, message):
        """
        判断 界面上是否有 toast 的内容包含 message
        :param message: toast的部分信息
        :return:
        """
        toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % message
        try:
            self.find_element(toast_feature, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据 toast 的部分的 message 消息，获取所有的toast内容
        :param message: toast的部分信息
        :return:
        """
        if self.is_toast_exist(message):
            toast_feature = By.XPATH, "//*[contains(@text, '%s')]" % message
            return self.find_element(toast_feature, 5, 0.1).text
        else:
            raise Exception("没有找到 对应的toast")

    def scroll_page_one_time(self, direction='up'):
        """
        根据方向，滑动半个屏幕一次
        :param dir:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        top_x = center_x
        top_y = screen_height * 0.25
        bottom_x = center_x
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = center_y
        right_x = screen_width * 0.75
        right_y = center_y

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查 dir 参数，必须是 up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找执行的 feature 的元素
        :param feature: 元素的特征
        :return: 元素的内容
        """
        old_page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
                if self.driver.page_source == old_page_source:
                    raise Exception("没有找到这个特征对应的元素")
                old_page_source = self.driver.page_source

    def is_keyword_in_page_source(self, keyword, timeout=3, poll=0.1):

        start_time = time.time()
        end_time = start_time + timeout

        while True:

            if time.time() > end_time:
                print("最终 没有找到")
                return False

            if keyword in self.driver.page_source:
                print("找到")
                return True
            else:
                print("正在找，没有找到")

            time.sleep(poll)
