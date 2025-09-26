from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = 'xxxx'
passward = 'xxxx'

def edge_driver(username,passward):
    bili = webdriver.Edge()

    bili.get('https://www.bilibili.com/')
    bili.maximize_window()
    print('准备点击')
    bili.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span').click()
    time.sleep(3)
    print('点击完成')
    print('输入账号：'+username)
    bili.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input').send_keys(username)
    print('输入密码：'+passward)
    bili.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[3]/input').send_keys(passward)
    time.sleep(3)
    print('点击登录')
    bili.find_element(By.XPATH,'/html/body/div[4]/div/div[4]/div[2]/div[2]/div[2]').click()
    time.sleep(3)
    print('弹出登录验证弹窗，')
edge_driver(username,passward)

print('执行完成')