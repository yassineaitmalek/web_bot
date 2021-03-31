from selenium import webdriver
import re
import time

d = webdriver.Chrome(executable_path="./chromedriver")
d.get("https://www.tripsavvy.com/telephone-numbers-for-top-airlines-54594")

doc=d.page_source
time.sleep(4)
d.quit()

phones = re.findall(r'[\d]{3}-[\d]{3}-[\d]{4}',doc)
for phone in phones:
    print(phone)
