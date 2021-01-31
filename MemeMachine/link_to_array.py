from PIL import Image
import requests
import bs4
import os
import time
import csv

images_folder = 'Images2'
#soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(os.getcwd())

with open(f'{os.getcwd()}\\TAMUhack2021\\MemeMachine\\urls.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for url in csv_reader:
        url = url[0]
        #print("URL: ", url)
        #response = requests.get(url)
        try:
            if url[-4] == '.':
                img = Image.open(requests.get(url, stream = True).raw)
                img.save(f"{os.getcwd()}\\TAMUhack2021\\MemeMachine\\{images_folder}\{line_count}_Img.jpg")
            else:
                img = Image.open(requests.get(url, stream = True).raw)
                img.save(f"{os.getcwd()}\\TAMUhack2021\\MemeMachine\\{images_folder}\{line_count}_Img.jpg")
        except:
            pass
        line_count += 1
print(os.listdir(f"{os.getcwd()}\\TAMUhack2021\\MemeMachine\\{images_folder}\\"))
