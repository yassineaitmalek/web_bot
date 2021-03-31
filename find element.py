from selenium import webdriver
import time

d = webdriver.Chrome(executable_path="./chromedriver")
d.get("https://www.youtube.com")


try :
    #d.find_element_by_id("button") 
    #d.find_element_by_name("")
    d.find_element_by_tag_name("form")
    #d.find_elements_by_link_text("")
    print("found")
except Exception as e:
    print("not found")


d.close()
