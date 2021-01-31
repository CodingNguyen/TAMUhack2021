import numpy as np
import imutils
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def add_text(imagename, text):
    image = Image.open(imagename)
    
    image.show()    

def deep_fry(imagename, top, bottom):
    image = Image.open(imagename)

    imageSize = image.size
    fontSize = int(imageSize[1]/10)
    x = int(imageSize[1]/4)
    yTop = 0
    yBottom = imageSize[1]

    font = ImageFont.truetype("impact.ttf", fontSize)
    draw = ImageDraw.Draw(image)

    draw.text((x-1, yTop-1), text=top, font=font, fill="black")
    draw.text((x+1, yTop-1), text=top, font=font, fill="black")
    draw.text((x-1, yTop+1), text=top, font=font, fill="black")
    draw.text((x+1, yTop+1), text=top, font=font, fill="black")
    draw.text((x, yTop), text=top, fill=(255,255,255), font=font)

    draw.text((x-1, yBottom-1), text=bottom, font=font, fill="black")
    draw.text((x+1, yBottom-1), text=bottom, font=font, fill="black")
    draw.text((x-1, yBottom+1), text=bottom, font=font, fill="black")
    draw.text((x+1, yBottom+1), text=bottom, font=font, fill="black")
    draw.text((x, yBottom), text=bottom, fill=(255,255,255), font=font)
    
    im3 = ImageEnhance.Color(image)
    im3.enhance(40.0).show()

deep_fry("Images2/24_Img.jpg", "TOP TEXT", "BOTTOM TEXT")