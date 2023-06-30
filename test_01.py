# 导入selenium库
from selenium import webdriver
# 导入时间
import time
# 引入By方法
from selenium.webdriver.common.by import By

# 加载驱动，驱动下载后放Microsoft\Edge\Application目录
# 驱动器更名【MicrosoftWebDriver.exe】
edge = webdriver.Edge()

# 载入网址
url = 'https://www.baidu.com/'
edge.get(url)

# 窗口最大化
edge.maximize_window()

edge.find_element(By.ID,'kw').send_keys("python菜鸟学习")

edge.find_element(By.XPATH,'//*[@id="su"]').click()
edge.implicitly_wait(3)
edge.find_element(By.LINK_TEXT,'Python 基础语法 | 菜鸟教程').click()
time.sleep(1.5)
# 定位页面
windows = edge.window_handles
edge.switch_to.window(windows[-1])

edge.find_element(By.LINK_TEXT,'Python 基础教程').click()
# 定位内容获取文本信息输出
a = edge.find_element(By.XPATH,'//*[@id="content"]/p[4]').text
print(a)
# 定时5s
time.sleep(5)

print('--------------（test_01）执行完毕--------------')