from selenium import webdriver

from selenium.webdriver.common.keys import Keys

b = webdriver.Chrome(executable_path="./chromedriver")

b.get("https://google.com")

r = b.find_elements_by_link_text('gmail')
b.implicitly_wait(5)
r.click()