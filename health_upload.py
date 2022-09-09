from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime, time

url = "https://workflow.ecust.edu.cn/default/work/uust/zxxsmryb/mrybtb.jsp"
options = webdriver.ChromeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# 实现规避检测
fp = open("info.txt", 'r')
fp1 = open("log.txt", 'a+')
for i in fp.readlines():
    username = i.split(' ')[0]
    password = i.split(' ')[1]
    password = password.replace('\n', '')
    try:
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
        chrome.get(url)
        wait = WebDriverWait(chrome, 10)
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        chrome.find_element(By.ID, "username").send_keys(username)
        chrome.find_element(By.ID, "password").send_keys(password)
        chrome.find_element(By.TAG_NAME, "button").click()
        wait.until(EC.presence_of_element_located((By.ID, "radio_swjkzk20")))
        chrome.find_element(By.ID, "radio_swjkzk20").click()
        chrome.find_element(By.ID, "radio_xrywz34").click()
        chrome.find_element(By.ID, "radio_xcm5").click()
        chrome.find_element(By.ID, "radio_sfycxxwc44").click()
        chrome.find_element(By.ID, "post").click()
        # wait.until(EC.presence_of_element_located((By.ID, "layui-layer-btn0")))
        chrome.find_element(By.CLASS_NAME, "layui-layer-btn0").click()
        # chrome.close()
        fp1.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')+username+" 填写成功\n")
    except Exception as e:
        fp1.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')+username+" 填写失败\n")
        fp1.write("失败原因："+str(e))




