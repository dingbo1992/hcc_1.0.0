import uiautomator2 as u2
import random


class BaseAction:

    def __init__(self):
        self.d = u2.connect()  # 一个设备时
        self.d.app_start('com.bailun.huichacha', stop=True)

    def click(self, loc, timeout=None):
        """
        找到元素后，直接点击
        :param loc: 元素定位
        :param timeout:
        :return:
        """
        self.d.xpath(loc).click_exists(timeout)

    #  点击发送文字
    def send_text(self, loc, text=''):
        self.d.xpath(loc).set_text(text)

    def select_from_more(self, location, num=1, index=-1):
        """
        :param location: 定位的一组元素
        :param num: 选择列表中的元素个数
        :param index: 选择列表中元素的索引
        :return:返回选择的元素（一个或多个）
        """
        els = []
        for el in self.d.xpath(location).all():
            print(el)
            els.append(el)
        print(len(els))
        if els is not None:
            print(len(els))
            if num <= len(els):
                albums = random.sample(els, num)
                print(len(els))
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

    def teardown(self, package_name):
        self.d.app_stop(package_name)

    def setup(self, package_name):
        self.d.app_start(package_name)
