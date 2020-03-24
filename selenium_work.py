import time
import logging
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
#############################################################
driver = webdriver.Chrome(executable_path='./chromedriver')

#############################################################
logging.basicConfig(filename='logs.txt',
                    format='%(asctime)s : %(levelname)s: %(message)s',
                    datefmt='%m/ %d/ %y %I: %M: %S %p',
                    level=logging.DEBUG)
logging.warning("This is warning")

#############################################################

driver.get("https://www.atg.party/")
driver.maximize_window()
print('Title is : ')
print(driver.title)         #  Title of the page
print(driver.current_url)   #current url of the page

#############################################################
# Response time
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
print('HTTP RESPONSE TIME (Page load of the web page): ')
print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)


#############################################################
''' Code to check the HTTP RESPONSE CODE CONDITION  '''

js = '''
let callback = arguments[0];
let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://www.atg.party/', true);
xhr.onload = function () {
    if (this.readyState === 4) {
        callback(this.status);
    }
};
xhr.onerror = function () {
    callback('error');
};
xhr.send(null);
'''

status_code = driver.execute_async_script(js)
print("HTTP RESPONSE CODE == ")
print(status_code)                    # 200
#############################################################
# Response time


""" After opening the url need to wait for some time to display all  the details in the browser . Otherwise immediatly it will start to
executing the code.
"""

driver.implicitly_wait(10)   # Implicit wait will applicable for all the elements present in the page.

login = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/ul/li[2]/a')
login.click()
#############################################################
                           # Login
user_name = driver.find_element_by_xpath('//*[@id="email"]')

user_pass = driver.find_element_by_xpath('//*[@id="password"]')
user_name.send_keys("wiz_saurabh@rediffmail.com ")
user_pass.send_keys("Pass@123")

# Go Button
login = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button')
login.click()   # Successfully logged iin
driver.implicitly_wait(10)
#############################################################
nav_close = driver.find_element_by_xpath('/html/body/div[1]/div/button')
nav_close.click()

""" Working with Button drop down - select option ( Article in this case ) """

drpDown = driver.find_element_by_id('dropdownMenuButton')
hover = ActionChains(driver).move_to_element(drpDown)
hover.perform()
article = driver.find_element_by_link_text('Article')
aHover = ActionChains(driver).move_to_element(article)
aHover.perform()
driver.get('https://www.atg.party/article')
#############################################################
# After swich to the form or frame


#############################################################
# For adding the image/ file you need to take the path of the image and also add name of the img.

driver.find_element_by_name('profile_pic').send_keys('/home/vidhya/PycharmProjects/SeleniumProject/image/img2.jpg')

# Textbox
title = driver.find_element_by_name('title')
title.send_keys('Title For The Project')

content = driver.find_element_by_xpath('//*[@id="form_post_article"]/div[2]/div[1]/div[3]/div')
content.send_keys('Content of  the title')
#############################################################
# Publish
publish = driver.find_element_by_id('featurebutton')
publish.click()
print('Current URL :')
print(driver.current_url)
driver.execute_script("window.scrollBy(0,1000)","")


# LOG FILE : Every event will be logged into the file called log file. By seeing the log file we can identify what an all the actions perfomed
# in the website.