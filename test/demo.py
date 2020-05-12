from time import sleep

import uiautomator2 as u2

d = u2.connect()
d.app_start('com.bailun.huichacha', stop=True)
sleep(2)
print(d.window_size())
sleep(1)


