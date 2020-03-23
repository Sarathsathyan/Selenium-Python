import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path='./chromedriver')

# Get URL
driver.get("https://www.atg.party/")
# After opening the url need to wait for some time to display all  the details in the browser . Otherwise immediatly it will start to
# executing the code.

driver.implicitly_wait(10)  #IMplicit wait will applicable for all the elements present in the page.

login = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/ul/li[2]/a')
login.click()
# Login
user_name = driver.find_element_by_xpath('//*[@id="email"]')

user_pass = driver.find_element_by_xpath('//*[@id="password"]')
user_name.send_keys("wiz_saurabh@rediffmail.com ")
user_pass.send_keys("Pass@123")

# Go Button
login = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button')
login.click()   # Successfully logged iin
driver.implicitly_wait(10)
nav_close = driver.find_element_by_xpath('/html/body/div[1]/div/button')
nav_close.click()

# Working with Button drop down - select option ( Article in this case )

drpDown = driver.find_element_by_id('dropdownMenuButton')
hover = ActionChains(driver).move_to_element(drpDown)
hover.perform()
article = driver.find_element_by_link_text('Article')
aHover = ActionChains(driver).move_to_element(article)
aHover.perform()
driver.get('https://www.atg.party/article')
