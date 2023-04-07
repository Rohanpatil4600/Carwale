from selenium import  webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("/Users/rohan/Downloads/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= options, service = s)
driver.get('https://www.carwale.com/used/cars-for-sale/#sc=-1&so=-1&city=176&pc=176')
time.sleep(1)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    if new_height== old_height:
        break
    old_height=new_height

html = driver.page_source
with open('carwale9.html', 'w', encoding = 'utf-8')as f:
    f.write(html)