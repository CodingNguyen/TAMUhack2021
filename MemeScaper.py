from PIL import Image
import requests
import bs4
import os
import time

not_broken = True
counter = 1
while counter < 20:
    time.sleep(2)

    images_folder = 'Images'

    url = f'https://imgflip.com/memetemplates?page={counter}'
    time.sleep(1)
    response = requests.get(url)
    time.sleep(4)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    time.sleep(2)
    #find image contents
    image = soup.find_all(class_='mt-box')
    imagelist = []
    for t in image:
        imagelist.append(str(t))

    #lists
    url_list = []
    title_list = []

    #get url and caption of each image on page
    for itera in imagelist:
        url_beg = itera.find("src")+7
        url_end = itera.find('"', itera.find("src")+5, 50000)
        title_beg = itera.find("title=")+7
        title_end = itera.find('"', itera.find("title=")+7, 50000)
        url_list.append(itera[url_beg:url_end])
        title_list.append(itera[title_beg:title_end])

    if len(url_list) == len(title_list):
        for xyz in range(len(url_list)):
            #print(os.getcwd())
            time.sleep(2)
            img = Image.open(requests.get(f"http://{url_list[xyz]}", stream = True).raw)
            time.sleep(4)
            img.save(f"{os.getcwd()}\TAMUhack2021\{images_folder}\{title_list[xyz]}.jpg", "JPEG")
            time.sleep(2)

    else:
        print("File lengths are different sizes")
    
    counter += 1        