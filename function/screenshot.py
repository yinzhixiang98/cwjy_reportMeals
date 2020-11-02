from time import sleep
import os
from selenium import webdriver     #从selenium库导入webdirver

def screenshot(save_path):
    global driver
    chrome_path = "C:/Users/zhengtianrui/Desktop/chromedriver_win32/chromedriver.exe"
    os.environ['webdriver.chrome.driver'] = chrome_path
    driver = webdriver.Chrome(chrome_path)
    sleep(1)
    driver.get("file:///C:/Program Files (x86)/Jenkins\workspace/Auto_Test_Api/Test_Ecs_Interface/reports/SummaryReport.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.save_screenshot(save_path)
    driver.close()

if __name__ == "__main__":
    screenshot("E:\screenshot.png")