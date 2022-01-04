import os
import selenium
from selenium import webdriver

# Web Driver Setup 
driver  = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(2)
url = "https://www.amazon.com/"
driver.get(url)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys("books")
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
print(driver.find_element_by_xpath('//*[@id="p13n-asin-index-0"]/div/span/div').text)
