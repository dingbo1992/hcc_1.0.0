from time import sleep
from base.base_action import BaseAction


class CustomerAction(BaseAction):

    customer_id = "com.bailun.huichacha:id/rl_bottom_menu_customer"  # 客诉中心
    exposure_xpath = "//*[contains(@text, '曝光')]"  # 曝光tab
    consult_xpath = "//*[contains(@text, '咨询')]"  # 咨询tab
    complaint_xpath = "//*[contains(@text, '投诉')]"  # 投诉tab
    search_id = 'com.bailun.huichacha:id/iv_right_center'  # 搜索按钮
    search_box_id = 'com.bailun.huichacha:id/et_search'  # 搜索框
    publish_id = 'com.bailun.huichacha:id/iv_right'  # 发布按钮

    def search(self):
        self.customer_in()
        self.click(self.search_id)  # 点击搜索
        sleep(1)
        self.click(self.search_box_id)
        self.send_text(self.search_box_id, '汇')
        sleep(1)
        self.d.set_fastinput_ime(False)
        sleep(2)
        self.d.send_action("search")
        sleep(3)

    #  进入客诉中心
    def customer_in(self):
        self.click(self.customer_id)

    # 点击曝光
    def exposure_in(self):
        self.customer_in()
        self.click(self.exposure_xpath)

    # 点击曝光
    def consult_in(self):
        self.customer_in()
        self.click(self.consult_xpath)

    # 点击投诉
    def complaint_in(self):
        self.customer_in()
        self.click(self.complaint_xpath)


cs = CustomerAction()
cs.search()
