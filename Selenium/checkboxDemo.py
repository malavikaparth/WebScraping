'''
This code we are learning what to do when elements have the same name in check box.
Here we need to understand that there were three options with the same name "cb1-element"
and to select option 2 for this case we need to do indexing by "driver.find_elements"
instead of driver.find_element.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/basic-checkbox-demo.html')
driver.implicitly_wait(30)
select_checkbox = driver.find_element(By.ID, 'isAgeSelected')
select_checkbox.click()
time.sleep(2)
check_all = driver.find_element(By.ID, 'check1')
check_all.click()
time.sleep(2)
check_all = driver.find_element(By.ID, 'check1')
check_all.click()
time.sleep(2)
check_all = driver.find_element(By.ID, 'check1')
check_all.click()
time.sleep(2)
'''
Here we need to understand that there were three options with the same name "cb1-element"
and to select option 2 for this case we need to do indexing by "driver.find_elements"
instead of driver.find_element
'''
checkbox_elements = driver.find_elements(By.CLASS_NAME, 'cb1-element')
# To interact with "option 2" (index 1, as it's 0-based):
checkbox_elements[1].click()