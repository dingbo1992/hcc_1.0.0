from time import sleep

import uiautomator2 as u2

d = u2.connect()
# d.app_start('com.bailun.huichacha', stop=True)
# print(d.current_app())
# msg = d.app_info("com.taobao.idlefish")
# print(msg)
# img = d.app_icon("com.taobao.idlefish")
# img.save("icon.png")
# run_list = d.app_list_running()
# print(run_list)
# sess = d.session('com.taobao.idlefish', attach=True)
# print(d.info)
# print(d.wlan_ip)
# d.screen_on()
print(d.info.get('screenOn'))
# xml = d.dump_hierarchy() # 打印页面xml
# print(xml)
# d.open_notification()
# d.open_quick_settings()
# im = d(text='xxx').screenshot()
# im.save('settings.jpg')
# 等到UI对象出现
d(text='设置').wait(timeout=3.0)  # 返回布尔
# 等待直到UI对象不见了
d(text='设置').wait_gone(timeout=1.0)


