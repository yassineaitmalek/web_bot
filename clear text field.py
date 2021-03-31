import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="./chromedriver")

browser.get("https://facebook.com")

search = browser.find_element_by_id('email')
search.send_keys('username')
search = browser.find_element_by_id('pass')
search.send_keys('password')
search.send_keys(Keys.RETURN)
time.sleep(4)
search.clear()
time.sleep(2)
browser.close()