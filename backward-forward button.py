import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


d = webdriver.Chrome(executable_path='./chromedriver')
d.get("https://google.com")

time.sleep(2)

d.get("http://youtube.com")
time.sleep(2)
d.back()
time.sleep(2)
d.forward()
time.sleep(2)

d.close()
