from selenium import webdriver

d = webdriver.Chrome(executable_path="./chromedriver")
d.get('http://google.com')

ids = d.find_elements_by_xpath('//*[@id]')




for i in ids :
    print(i.get_attribute('id'))
print('\n')


d.close()