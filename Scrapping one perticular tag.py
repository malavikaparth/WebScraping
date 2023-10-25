'''
In this program i am going to scrape all the images and tip para from the webpage
'''
from bs4 import BeautifulSoup
with open('scraping1.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    #To find all the div tabls that are only tip tabs.
    #the filtering is done using "class_".
    tip_paras = soup.find_all('div' , class_ = 'tip tab')
    img_paras = soup.find_all('img')
    #To see what is there in this tip_paras:
    '''
        printing only para tabs and only printing the text inside the tabs
        print(tip.p.text)
        print(tip)
        printing only tabs with hyperreference in the tip tabs
        print(tip.a)
    '''
    for tip in tip_paras:
        #moving all hyperreference to a variable
        hyperef = tip.a
        if hyperef is not None:
            print(f'The hyperref in tip tabs are {hyperef.text}')
    '''
    <img> tag does not contain text like other HTML elements such as paragraphs or headings. 
    Therefore, trying to print image.text will result in an empty string or None. 
    If you want to extract information from the <img> tags, you should access their attributes, 
    such as the src attribute, which contains the image URL.
    '''
    for image in img_paras:
        #Split is used to print only the last part of url
        src = image.get('src').split('/')[-1]
        alt = image.get('alt')
        if src or alt:
            print(f'The source is {src} and alt is {alt}')






