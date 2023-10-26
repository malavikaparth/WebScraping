'''
Scraping a real website.
Scraping a real job advertisement website. Scraping all jobs from the website which had python
as their main skill. In this i am only scraping jobs that were posted "2 Days Age to Few Hours Age".

'''
'''
For scraping a real website we can use the "request" library
pip install urllib3==1.26.6. In case of problems with this library

'''
import requests
from bs4 import BeautifulSoup
#requests.get('')
html_status = requests.get('https://internshala.com/jobs/python-jobs/')
print(html_status)
html_text = requests.get('https://internshala.com/jobs/python-jobs/').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'container-fluid individual_internship visibilityTrackerItem')
#For each job in each page
for job in jobs:
    '''
    When we have more than one type of class name we can use this
    '''
    published_date = job.find('div', class_=['status status-small status-success', 'status status-small status-info', 'status status-small status-inactive'])
    if published_date is not None:   #To know the jobs posted very recently coz other have different class name
      #if 'Few' in published_date.text:  # To print the jobs posted in "Few hours ago"
        company_name = job.find('a', class_ = 'link_display_like_text view_detail_button').text.replace(' ', '')
        experiance = job.find('div', class_ = 'item_body desktop-text').text
        #print(published_date)
        '''
        if this was like <div class = xyz> 
        <div> experiance </div>
        </div>
        we do "experiance = job.find('div', class_ = 'item_body desktop-text').div.text
        '''

        print(f'The comapny name is {company_name}, the experiance required is {experiance}, the published date is  {published_date.text}')
    #else:
        #print('nothing')