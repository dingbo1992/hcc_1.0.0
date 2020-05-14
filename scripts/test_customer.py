import os
import sys
from time import sleep
import allure
sys.path.append(os.getcwd())
from pages.customer_page import CustomerAction


class TestCustomer:
    cus_action = CustomerAction()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="点击进入客诉-曝光-曝光详情页，查看关联的是否为曝光平台")
    def test_exposure_in(self):
        assert self.cus_action.exposure_in()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="点击进入客诉-咨询列表-咨询详情页，查看关联的是否为咨询平台")
    def test_consult_in(self):
        assert self.cus_action.consult_in()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="点击进入客诉-投诉列表-投诉详情页，查看关联的是否为投诉平台")
    def test_complaint_in(self):
        assert self.cus_action.complaint_in()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="点击进入客诉-搜索-查看搜索列表并点击条目，判断详情页是否存在，依据是否有评论弹框")
    def test_search(self):
        self.cus_action.customer_search()

    def teardown(self):
        self.cus_action.teardown()

    def setup(self):
        self.cus_action.setup()

