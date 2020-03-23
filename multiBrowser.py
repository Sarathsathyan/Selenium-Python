import requests
import time
from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path='./chromedriver')

# Get url (open application)

driver.get("https://www.atg.party/")                               # Navigation starts
print('Title is : ')
print(driver.title); #  Title of the page
print(driver.current_url)  #current url of the page
time.sleep(5)

driver.get("https://christuniversity.in/")
print(driver.title)
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()                                              # Navigation ends



# r = requests.get(driver.current_url)
# print(r.status_code)
#driver.close()