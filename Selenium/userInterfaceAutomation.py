'''
To automatically open up a web browser.
For each browser there will be different way to open a browser. here we are doing chrome
To know chrome version : "chrome://version" : We can get the required version from here. save it in a place.
Now if needed we need to add this to the environment variable and for that we can use import os.
Check the commented code for this.
https://chromedriver.storage.googleapis.com/index.html
'''
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
#import os

#os.environ['PATH'] += r"C:/Users/Malavika/PycharmProjects/WebScraping/Selenium"
driver = webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/generate-file-to-download-demo.html')
driver.implicitly_wait(8)
'''
Here i am trying to enter data into a text box,
generate a file for it
and downloading it
'''
text_input = driver.find_element(By.ID, 'textbox')
# Enter data into the text box
text_input.send_keys("Your text goes here")
generate_file = driver.find_element(By.ID, 'create')
generate_file.click()

download_file = driver.find_element(By.ID, 'link-to-download')
download_file.click()