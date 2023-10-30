import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html_status = requests.get('https://internshala.com/jobs/python-jobs/')
print(html_status)
html_text = requests.get('https://internshala.com/jobs/python-jobs/').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'container-fluid individual_internship visibilityTrackerItem')
for job in jobs:
    position_name = job.find('a',class_ = 'view_detail_button').text
    company_name = job.find('a', class_ = 'link_display_like_text view_detail_button').text.replace(' ','')
    money = job.find('span', class_ = 'mobile').text.replace(' ','')
    print(f"The company name is:{company_name}, The position is:{position_name}, The money is{money}\n")

