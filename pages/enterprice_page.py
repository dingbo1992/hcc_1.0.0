from base.base_action import BaseAction


class EnterPrice(BaseAction):

    enter_price_id = "com.bailun.huichacha:id/tv_title"  # id属性
    enter_price_text = "交易商"                            # text属性

    # 点击进入交易商tab
    def enter_price_in(self):
        self.click(resourceId=self.enter_price_id, text=self.enter_price_text)


EnterPrice().enter_price_in()