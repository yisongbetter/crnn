import sys, os
import cv2
import lmdb
import numpy as np
import shutil

def list_gen(): 
    thresh = 600

    data_source = './Challenge2_Training_Task3_Images_GT'
    output_source ='./output'
    train_lmdb = os.path.join(output_source, 'train')
    test_lmdb = os.path.join(output_source, 'test')
    if os.path.exists(train_lmdb):
        shutil.rmtree(train_lmdb)
    os.mkdir(train_lmdb)
    if os.path.exists(test_lmdb):
        shutil.rmtree(test_lmdb)
    os.mkdir(test_lmdb)



    img_source = data_source
    annotation_path = os.path.join(data_source,'gt.txt') 
    annotation = open(annotation_path)

    train_list = []
    train_label = []
    test_list = []
    test_label = []

    cnt = 0
    for line in annotation:
        cnt = cnt+1
        img_name = line.split(',')[0].strip()
        img_path = os.path.join(img_source, img_name)
        label = line.split(',')[1].strip().strip('""')
        if cnt <= thresh:
            train_list.append(img_path)
            train_label.append(label)
        #   print train_label
        else:
            test_list.append(img_path)
            test_label.append(label)
    
    #print len(test_list)
    #print len(test_label)
        #    print test_label
    return train_lmdb, train_list, train_label, test_lmdb, test_list, test_label

# list_gen()   

