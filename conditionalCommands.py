import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("https://www.atg.party/")
driver.implicitly_wait(25)

user_ele = driver.find_element_by_name("first_name")
pass_ele = driver.find_element_by_name("password")

user_ele.send_keys("wiz_saurabh@rediffmail.com")
pass_ele.send_keys("Pass@123")


print(user_ele.is_displayed());
print(user_ele.is_enabled())

