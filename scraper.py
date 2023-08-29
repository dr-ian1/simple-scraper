import requests 
import os
from bs4 import BeautifulSoup 
import urllib3
from urllib.parse import urljoin, urlparse, urlunparse
x = 0
y="""\n\n███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║██╔████╔██║██████╔╝██║     █████╗      ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\n
Created by Darian Sellars as a first outside of school project (29/08/23)\n """
print(y)

#exception shit bla bla bla
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def get_response(url): 
    return requests.get(url, verify=False) 


#getting urls from input
target=str(input("target: "))

parsed_url = urlparse(target)
base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, "", "", "", ""))

#getting images from url
response = get_response(target) 
soup = BeautifulSoup(response.text, 'html.parser') 


#setting save location
save_dir = input("Save location FORMAT MUST BE LIKE THIS: D:\ScrapedImages : ")

#grabbing all items with the "img" tag from the supplied page
 #adding the baseurl to the image url. EG: baseurl: https://www.w3schools imgurl:/images/x/y/z  result: https://www.w3schools/images/x/y/z
for item in soup.find_all('img'):
    img_url = item['src']
    absolute_img_url = urljoin(base_url, img_url)  

   #error handling
    try:
        img_response = get_response(absolute_img_url)
        img_response.raise_for_status()  

        image_filename = f'image{x}.png'

        #saving images
        image_path = os.path.join(save_dir, image_filename)
        
        with open(image_path, 'w+b') as fp:
            fp.write(img_response.content)
        
        print(f"Image {x} downloaded successfully.")
        x += 1
    except Exception as e:
        print(f"Error downloading image {x}: {e}")
