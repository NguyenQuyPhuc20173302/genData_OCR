import cv2
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

# lấy dữ liệu từ file data_word.txt
f = open('data_word_new.txt', 'r')
data_ = f.read()

# đưa dữ liệu vào list
data_ = data_.split('\n')


def gen_one_word():
    # lặp mỗi phần tử trong data_
    for data in data_:
        #  đọc ảnh
        img = Image.open("anh_nen_1.png")
        # vẽ text lên ảnh với phông chữ có thể tùy chọn ở https://github.com/opensourcedesign/fonts
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('FreeSansBold.ttf', 40)
        draw.text((0, 7), data, (0, 0, 0), font=font)
        name_ = random.randint(0, 10000000000000)
        name_image = 'dataset/' + str(name_) + '.png'
        print(name_image)
        name_txt = 'dataset/' + str(name_) + '.txt'
        print(name_txt)
        img.save(name_image)
        file = open(name_txt, 'w')
        nd = str(data)
        file.write(nd)
        file.close()

gen_one_word()
