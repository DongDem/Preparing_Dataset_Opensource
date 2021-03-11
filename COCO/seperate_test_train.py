import xml.etree.ElementTree as ET
import os
import csv
import shutil

root_path = 'downloaded_images'
save_path = "images_train"
train_csv = 'train.csv'

with open(train_csv) as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:

        if i == 0:
            print('dong')
        else:
            filename_value = row[0]
            print(filename_value)
            m = shutil.copy(os.path.join(root_path, filename_value), os.path.join(save_path, filename_value))
        i = i + 1
