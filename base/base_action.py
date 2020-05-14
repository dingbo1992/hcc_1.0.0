from time import sleep

import uiautomator2 as u2
import random


class BaseAction:

    def __init__(self):
        self.d = u2.connect()  # 一个设备时
        self.d.app_start('com.bailun.huichacha', stop=True)

    def click(self, loc=None, timeout=10000, **args):
        """
        找到元素后，直接点击
        :param loc: 元素定位
        :param timeout:
        :return:
        """
        if isinstance(loc, str):
            location = self.d.xpath(loc)
        else:
            location = self.d(**args)
        sleep(1)
        location.click_exists(timeout)

    def click_with_group(self):
        self.d(resourceId="com.bailun.huichacha:id/tv_title", text="交易商").click()

    #  点击发送文字
    def send_text(self, loc, text='外汇'):
        location = self.d.xpath(loc)
        sleep(0.5)
        location.set_text(text)

    def select_from_more(self, location, num=1, index=-1):
        """
        :param location: 定位的一组元素
        :param num: 选择列表中的元素个数
        :param index: 选择列表中元素的索引
        :return:返回选择的元素（一个或多个）
        """
        sleep(2)
        els = []
        for el in self.d.xpath(location).all():
            els.append(el)
        print(len(els))
        if els is not None:
            if num <= len(els):
                albums = random.sample(els, num)
                if num == 1:
                    if index == -1 or index < 0:
                        loc = random.randint(0, len(els) - 1)
                        print(loc)
                        return els[loc]
                    else:
                        return els[index]
                if num > 1:
                    sel_elements = []
                    for album in albums:
                        sel_elements.append(album)
                    return sel_elements

    #  上滑屏幕
    def swipe_up(self, duration=1):
        screen_x = 0
        screen_y = 1
        size_x = self.d.window_size()[screen_x]
        size_y = self.d.window_size()[screen_y]
        fx = 0.5 * size_x
        fy = 0.9 * size_y
        tx = 0.5 * size_x
        ty = 0.2 * size_y
        self.d.swipe(fx, fy, tx, ty, duration)

    #  下滑/下拉屏幕
    def swipe_down(self, duration=1):
        screen_x = 0
        screen_y = 1
        size_x = self.d.window_size()[screen_x]
        size_y = self.d.window_size()[screen_y]
        fx = 0.5 * size_x
        fy = 0.2 * size_y
        tx = 0.5 * size_x
        ty = 0.9 * size_y
        self.d.swipe(fx, fy, tx, ty, duration)

    def teardown(self, package_name='com.bailun.huichacha'):
        sleep(2)
        self.d.app_stop(package_name)

    def setup(self, package_name='com.bailun.huichacha'):
        sleep(2)
        self.d.app_start(package_name)

    def text_judge_equal(self, expect_msg, loc):
        """
        通过text属性值断言
        :param expect_msg: 预期结果
        :param loc: 实际结果的元素定位
        :return: 断言返回
        """
        try:
            el = self.d.xpath(loc)
            message = el.text
            print('实际结果', message)
            print('预期结果', expect_msg)
            if message == expect_msg:
                return True
            else:
                return False
        except Exception:
            return False

    def text_judge_contain(self, expect_msg, loc):
        """
        通过text属性值断言
        :param expect_msg: 预期结果
        :param loc: 实际结果的元素定位
        :return: 断言返回
        """
        try:
            el = self.d.xpath(loc)
            message = el.text
            print('实际结果', message)
            print('预期结果', expect_msg)
            if message in expect_msg:
                return True
            else:
                return False
        except Exception:
            return False
