from base.base_action import BaseAction
from time import sleep

scan_id = 'com.bailun.huichacha:id/iv_scan_popup_window'  # 首页-扫一扫
scan_take_id = 'com.bailun.huichacha:id/iv_camera_scan_take_photo'  # 识别按钮
scan_album_id = 'com.bailun.huichacha:id/v_camera_scan_title_bar_album'  # 相册按钮
scan_help_id = 'com.bailun.huichacha:id/v_camera_scan_title_bar_help'  # 帮助按钮
scan_cancel_id = 'com.bailun.huichacha:id/v_camera_scan_title_bar_cancel'  # 取消按钮
# 相册页面
scan_picture_id = 'com.bailun.huichacha:id/iv_album_picture'  # 相册图片id
scan_camera_id = 'com.bailun.huichacha:id/iv_animation_icon'  # 相机按钮
picture_cancel_id = 'com.bailun.huichacha:id/tv_cancel'  # 相册页面取消按钮
picture_back_id = 'com.bailun.huichacha:id/iv_back'  # 相册页面返回按钮
picture_confirm_id = 'com.bailun.huichacha:id/iv_ucrop_confirm'  # 确定选择按钮
meizu_camera_take_id = 'com.meizu.media.camera:id/shutter_button'  # 相机拍摄按钮
xioami_camera_take = 'com.android.camera:id/v9_shutter_button_internal'
xiaomi_camera_done = 'com.android.camera:id/intent_done_apply'
xiaomi_camera_done_confirm = 'com.bailun.huichacha:id/iv_ucrop_confirm'
meizu_camera_done_id = 'com.meizu.media.camera:id/done_button'  # 照片完成按钮
meizu_camera_confirm_id = 'com.bailun.huichacha:id/iv_ucrop_confirm'  # 相机拍摄确按钮
result_text = 'com.bailun.huichacha:id/tv_custom_toolbar_title'


class HomeScan(BaseAction):

    def scan_sure(self):
        try:
            expect_message = '智能识别结果'
            el = self.d.xpath(result_text)
            message = el.text
            print(message)
            if message == expect_message:
                print(message)
                return True
        except Exception:
            return False  # 获取扫描结果

    # 进入扫一扫
    def scan(self):
        self.click(scan_id)

    def scan_by_camera(self):
        self.scan()
        self.click(scan_take_id)
        return self.scan_sure()

    # 进入相册页面
    def album_in(self):
        self.scan()
        self.click(scan_album_id)

    # 通过相册识别
    def scan_by_album(self):
        self.album_in()
        ele = self.select_from_more(scan_picture_id)
        ele.click()
        self.click(picture_confirm_id)
        self.d.screenshot('./screen/ab_img.jpg')
        return self.scan_sure()

    # 通过相机拍摄识别
    def scan_by_album_camera(self):
        self.album_in()
        self.click(scan_camera_id)  # 点击相册相机
        self.click(xioami_camera_take)  # 点击拍摄
        self.click(xiaomi_camera_done)  # 点击完成拍摄
        self.click(xiaomi_camera_done_confirm)  # 点击确认选择
        return self.scan_sure()


# if __name__ == '__main__':
#
#     home_scan = HomeScan()
#     home_scan.scan_by_album()
