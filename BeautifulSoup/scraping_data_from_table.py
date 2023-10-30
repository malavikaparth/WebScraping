'''
The task is to download images from a website
'''
from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

'''
To extract the url of all images from the website
'''
url = 'https://www.amazon.in/ref=nav_logo'
html_status = requests.get('https://www.amazon.in/ref=nav_logo')
print(html_status)
html_text = requests.get('https://www.amazon.in/ref=nav_logo').text
soup = BeautifulSoup(html_text, 'lxml')
images = soup.find_all('img')
for img in images:
    img_src = img['src']
    print(img_src)

'''
To save the images to a directory
'''
if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')
# Download and save each image
for img in images:
    img_src = img.get('src')
    if img_src:
        # Construct a full image URL in case it's a relative URL
        img_url = urljoin(url, img_src)
        # Extract the image filename from the URL
        img_filename = os.path.join('downloaded_images', os.path.basename(img_url))

        # Send an HTTP GET request to download the image
        img_response = requests.get(img_url)

        # Save the image to the "downloaded_images" directory
        with open(img_filename, 'wb') as img_file:
            img_file.write(img_response.content)

        print(f'Downloaded: {img_filename}')


