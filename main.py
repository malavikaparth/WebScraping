'''
To parse html files to python objects we use lxml. lxml is used as it is the
best library inside beautiful soup and can work with even broken html code.
'''
from bs4 import BeautifulSoup
'''
reading the contents of the html file "scraping1.html
TO FIND : How to read a file when the file is not in the same directory

How to scrape a webpage to find some specific information
----------------------------------------------------------
Scraping the html file using beautifulsoup. 
lxml is the parser method to convert the html file to python objects

To find any perticular tags "soup.find(tag name)". This will find only one tag with this name
To fins all the tags use "soup.find_all(tag name)".the output will be a list of tags. 
The output of all this will be the full tags.

In a webpage to find tag of a perticular sentance or heading or content or button, we can right click on the thing and 
press inspect
'''
with open('scraping1.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tag = soup.find('script')
    heading = soup.find_all('h2')
    #print(heading)
    #To print just the headings alone:
    for title in heading:
        print(title.text)
    #to enumerate
    for title, i  in enumerate(heading):
        print(title, i.text)

