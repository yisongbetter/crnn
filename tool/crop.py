# creat train/test image and annotation

import xml.etree.ElementTree as ET
import sys
import cv2
import os, shutil


dict = {}

id_train = open('./id_card/id_train.txt', 'w')
id_test = open('./id_card/id_test.txt', 'w')

train = open('./ImageSet/train.txt', 'r')
test = open('./ImageSet/test.txt', 'r')

train_list = []
test_list = []

for line in train:
    train_list.append(line.strip())
for line in test:
    test_list.append(line.strip())

xml_source = './Annotations'
xmls = os.listdir(xml_source)

img_source = './Images'
imgs = os.listdir(img_source)

id_img = './id_card/id_imgs'

if os.path.exists(id_img):
    shutil.rmtree(id_img)
os.mkdir(id_img)

for xml in xmls:
    key = os.path.join(img_source, '{}{}'.format(xml.split('.')[0], '.jpg'))
    xml_path = os.path.join(xml_source, xml)

    tree = ET.parse(xml)
    root = tree.getroot()

    for i, child in enumerate(root):
        for j, sub in enumerate(child):
            if sub.text == 'IDnumber_value':
                dict[key] = (child[j+1].text, [[child][j+5][0].text, child[j+5][1].text, child[j+5][2].text, child[j+5][3].text])

def my_crop(img, bbox):
    return img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

for i, img in enumerate(imgs):
    key = os.path.join(img_source, img)
    if img.split('.')[0] in train_list:
        id_train.write(dict[key][0]+'\n')
    else:
        id_test.write(dict[key][0]+'\n')


    im = cv2.imread(key)
    im_crop = my_crop(im, dict[key][1])
    save_name = '{}{}'.format(dict[key][0], '.jpg')
    save_path = os.path.join(id_img, save_name)
    cv2.imwrite(save_name, im_crop)
    





