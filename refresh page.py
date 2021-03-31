import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


d = webdriver.Chrome(executable_path='./chromedriver')
d.get("https://google.com")


time.sleep(3)
d.refresh()
time.sleep(2)
d.close()
