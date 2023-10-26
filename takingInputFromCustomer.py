'''
Scraping a real website.
In this program i am first asking the user to input the skill they want then
i am printing the link to the webpage for jobs for that link. Then i am taking
that link and sending a get request to get the company name, experiance and published_date
'''
'''
For scraping a real website we can use the "request" library
pip install urllib3==1.26.6. In case of problems with this library

'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin #For making relative url to absalute url
#requests.get('') The main syntax
print("Ente the skill you want")
familiar_skill  = input('>')
print(f"The jobs for {familiar_skill} is")

html_status = requests.get('https://internshala.com/jobs-by-skill/')
html_text = requests.get('https://internshala.com/jobs-by-skill/').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'directory_content')
'''
"a_tag = jobs.find_all('a')"
The issue with your code is that you are using the .find_all() method on a ResultSet (the jobs variable), 
which is returned by soup.find_all('div', class_='directory_content'). 
The .find_all() method returns a list of Tag objects, and you are trying to call 
.find_all('a') directly on this list, which is not supported.

To extract all the <a> tags within the <div class="directory_content"> elements, 
you should loop through the list of Tag objects and then use .find_all('a') for each individual Tag. 

'''
for job in jobs:
    a_tags = job.find_all('a')
    for a_tag in a_tags:
        a_text = a_tag.text
        if familiar_skill in a_text:
            a_href = a_tag['href']
            html_status2 = requests.get(a_href)
            html_text2 = requests.get(a_href).text
            # print(html_text)
            soup2 = BeautifulSoup(html_text2, 'lxml')
            jobs2 = soup2.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
            for job in jobs2:
                '''
                When we have more than one type of class name we can use this
                '''
                published_date = job.find('div', class_=['status status-small status-success',
                                                         'status status-small status-info',
                                                         'status status-small status-inactive'])
                if published_date is not None:  # To know the jobs posted very recently coz other have different class name
                    # if 'Few' in published_date.text:  # To print the jobs posted in "Few hours ago"
                    company_name = job.find('a', class_='link_display_like_text view_detail_button').text.replace(' ',
                                                                                                                  '')
                    experiance = job.find('div', class_='item_body desktop-text').text
                    job_link1 = job.find('a', class_='view_detail_button')
                    '''
                    In my current webpage the url is a relative URL. This is possible in a lot of website. 
                    But when we print 'job_link2', the link that will come is the relative url. This is not clickable.
                    To make this clickable we need to join it with the base url. The base_url in web scraping typically refers
                     to the main or root URL of the website you are scraping.
                    '''
                    job_link2 = job.div.h3.a['href']
                    absolute_job_link = urljoin('https://internshala.com/jobs/python-jobs/', job_link2)
                    # print(job_link1)
                    # print(published_date)
                    '''
                    if this was like <div class = xyz> 
                    <div> experiance </div>
                    </div>
                    we do "experiance = job.find('div', class_ = 'item_body desktop-text').div.text
                    '''

                    print(
                        f'The comapny name is {company_name}, the experiance required is {experiance}, the published date is  {published_date.text}, the job link is {absolute_job_link}')

