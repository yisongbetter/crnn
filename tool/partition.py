# creat images and annotations

import sys
import os, shutil
data_source = './'
dirs = os.listdir(data_source)

for dir in dirs:
    file_path = os.path.join(data_source, dir)
    for file in os.listdir(file_path):
        src_path = os.join(file_path, file)
        if file.endswith('jpg'):
            dest_path = os.path.join('./Images', file)
        elif file.endswith('xml'):
            dest_path = os.path.join('./Annotations', file)

        shutil.copy(src_path, dest_path)


