import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


d = webdriver.Chrome(executable_path='./chromedriver')
d.get("http://www.worldslongestwebsite.com/")
e = d.find_element_by_tag_name('html')
e.send_keys(Keys.END)
time.sleep(2)
e.send_keys(Keys.HOME)