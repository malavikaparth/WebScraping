'''
In this program i am automating simple form filling using selenium to automate entering
value to a form using send_keys. Here ia ma also learning when two keys have the same name,
different ways to access it like using CSS selector or XML path. I am also learnt that to include keys
like clt, shift, alt i can use 'Keys' in selenium and about Keys.NUMPAD1,Keys.NUMPAD5)
ALL CSS SELECTORS : https://www.w3schools.com/cssref/css_selectors.php
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #for importing cntrl, alt,shift keys ect for automating copy, paste etc...
'''
Here a main problem i am facing is that my page is not loading for a long time. it is just poping up and going 
Thus to solve this i am using explicit wait
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

os.environ['PATH'] += r"C:/Users/Malavika/PycharmProjects/Selenium"

driver = webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
'''
In case some selenium pop up came

try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping ....')
THINGS TO NOTE ON THIS PROGRAM:
Both the buttons are having thr same name "btn-primary". Thus there is some problem in displaying the 
answer correctly. One way of solving this is by using the css option.
'''
message_input = driver.find_element(By.ID, 'user-message')
message_input.send_keys("This is halloween")
#show_message = driver.find_element(By.CSS_SELECTOR, 'button[onclick="showInput()"]')
show_message = driver.find_element(By.XPATH, '//button[contains(@onclick, "showInput()")]')
show_message.click()

time.sleep(2)
text_input_a = driver.find_element(By.ID, 'value1')
text_input_a.send_keys(Keys.NUMPAD1,Keys.NUMPAD5) #equal to 15
text_input_b = driver.find_element(By.ID, 'value2')
text_input_b.send_keys("5")
#when button name is like "btn btn-primary" we take only the last part
#download_file = driver.find_element(By.ID, 'btn-primary')
#download_file = driver.find_element(By.CLASS_NAME, 'button[onclick="return total()"]') This method is not working for me
#So i am using the down method
download_file = driver.find_element(By.XPATH, '//button[contains(@onclick, "return total()")]')

time.sleep(2)
download_file.click()




