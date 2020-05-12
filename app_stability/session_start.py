from time import sleep

import uiautomator2 as u2

d = u2.connect()
# d.app_start('com.ba
sess = d.session('com.taobao.idlefish')  # 开始网易云音乐
sess.close()  # 停止网易云音乐
sess.restart()  # 冷启动网易云音乐
# 启动应用程序（如果未运行），如果已运行(跳过启动)
sess = d.session('com.taobao.idlefish', attach=True)  # 则跳过启动
# 如果应用崩溃或退出
sess(text='Music').click()  # 引发SessionBrokenError
# 会话下的其他函数调用也会引发SessionBrokenError
