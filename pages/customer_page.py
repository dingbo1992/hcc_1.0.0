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
    customer_detail = 'com.bailun.huichacha:id/tv_plate_name'  # 客诉详情页曝光/咨询/投诉平台字样
    search_list_id = 'com.bailun.huichacha:id/rl_item'  # 搜索后的客诉列表
    detail_commen_id = 'com.bailun.huichacha:id/tv_send_comment'  # 详情页评论框

    def customer_search(self):
        self.customer_in()
        self.click(self.search_id)  # 点击搜索
        self.click(self.search_box_id)
        self.send_text(self.search_box_id)
        self.d.set_fastinput_ime(False)
        sleep(2)
        self.d.send_action("search")
        self.select_from_more(self.search_list_id).click()
        return self.text_judge_equal('发表你的评论吧…', self.detail_commen_id)

    #  进入客诉中心
    def customer_in(self):
        self.click(self.customer_id)

    # 点击曝光
    def exposure_in(self):
        self.customer_in()
        self.click(self.exposure_xpath)
        self.select_from_more('com.bailun.huichacha:id/rl_top').click()
        return self.text_judge_equal('曝光平台：', self.customer_detail)

    # 点击咨询
    def consult_in(self):
        self.customer_in()
        self.click(self.consult_xpath)
        self.select_from_more('com.bailun.huichacha:id/rl_top').click()
        return self.text_judge_equal('咨询平台：', self.customer_detail)

    # 点击投诉
    def complaint_in(self):
        self.customer_in()
        self.click(self.complaint_xpath)
        self.select_from_more('com.bailun.huichacha:id/rl_top').click()
        return self.text_judge_equal('投诉平台：', self.customer_detail)


