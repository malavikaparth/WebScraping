from bs4 import BeautifulSoup
import requests

html_status = requests.get('https://internshala.com/')
#print(html_status)
html_text = requests.get('https://internshala.com/').text
soup = BeautifulSoup(html_text, 'lxml')
'''
Two different ways of printing the title of a webpage
'''
jobs = soup.find('title').text
print(jobs)
title_elements = soup.find_all('title')
for title in title_elements:
    print(title.text)
