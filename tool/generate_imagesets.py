# generate imagesets

import sys, os

data_source = './'
dirs = os.listdir(data_source)
train = open('./ImageSet/train.txt', 'w')
test = open('./ImageSet/test.txt', 'w')
for dir in dirs:
    if dir == 'something':
        file_path = os.path.join(data_source, dir)
        for file in os.listdir(file_path):
            if file.endswith('jpg'):
                test.write(file.split('.')[0] + '\n')
        else:
            file_path = os.path.join(data_source. dir)
            for file in os.listdir(file_path):
                if file.endswith('jpg'):
                    train.write(file.split('.')[0] + '\n')


            
