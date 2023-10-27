from bs4 import BeautifulSoup
import requests

base_url  = "https://internshala.com/jobs/python-jobs/page-/"
html_status = requests.get('https://internshala.com/jobs/python-jobs/')
print(html_status)
html_text = requests.get('https://internshala.com/jobs/python-jobs/').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
page_start = int(soup.find('span' , id= 'pageNumber').text)
page_end = int(soup.find('span' , id= 'total_pages').text)
print(page_start, page_end)
with open('posts/index.txt', 'w') as f:
    for page in range(page_start,page_end+1):
        html_status = requests.get(f'https://internshala.com/jobs/python-jobs/page-{page}')
        print(html_status)
        html_text = requests.get(f'https://internshala.com/jobs/python-jobs/page-{page}').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
        for job in jobs:
            company_name = job.find('a', class_ = 'link_display_like_text view_detail_button').text.replace(' ','')
            experiance = job.find('div', class_ = 'item_body mobile-text').text
            published_date = job.find('div', class_=['status status-small status-success',
                                                     'status status-small status-info',
                                                     'status status-small status-inactive']).text

            f.write(f'page:{page}, company_name: {company_name}, experiance: {experiance},published_date: {published_date}')
