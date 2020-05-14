import os
import sys
from time import sleep

import allure
sys.path.append(os.getcwd())
from pages.home_scan_page import HomeScan


class TestScan:
    home_scan = HomeScan()

    def teardown(self):
        self.home_scan.teardown()

    def setup(self):
        self.home_scan.setup()

    #  通过相册扫描交易商
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="通过相册扫描交易商")
    def test_scan_by_album(self):
        allure.attach('相册扫描', '点击进入相册，随机选择一张图片扫一扫，'
                              '验证扫描结果是否正常')
        is_true = self.home_scan.scan_by_album()
        allure.attach(open('./screen/ab_img.jpg', 'rb').read(), '图片', allure.attachment_type.JPG)
        assert is_true

    #  拍摄照片扫描交易商
    @allure.severity(allure.severity_level.MINOR)
    @allure.step(title="通过相机拍摄扫描交易商")
    def test_scan_by_camera(self):
        allure.attach('拍照扫描', '点击扫一扫，相机拍摄图片，'
                              '验证扫描结果是否正常')
        assert self.home_scan.scan_by_camera()


