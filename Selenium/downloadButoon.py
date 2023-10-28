'''
Here ia m clicking on download button.
I am also checking if the download is complated by checking if the text displayed in the screen is 'completed!'
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Users\Malavika\PycharmProjects\Selenium"

driver = webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(30)
start_downoad = driver.find_element(By.ID, 'downloadButton')
start_downoad.click()
'''
cancel_dnwld = driver.find_element(By.CLASS_NAME, 'ui-dialog-buttonset')
cancel_dnwld.click()
'''
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label') , # Element filtration
        'Complete!'# The expected text
    )
)

