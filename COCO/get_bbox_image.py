import cv2
import csv
import os
import pandas as pd


image_path = 'downloaded_images'
save_path = 'bbox_image'

xml_list = []
count=1
with open('test_coco_knife.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        '''
        count+=1
        img = cv2.imread(os.path.join(image_path,str(row[0])))
        crop_img = img[int(row[5]):int(row[7]), int(row[4]):int(row[6])]
        cv2.imwrite(os.path.join(save_path,str(count)+".jpg"),crop_img)
        '''
        xml_list.append(row)
#print(count)

column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
xml_df = pd.DataFrame(xml_list, columns=column_name)
xml_df.to_csv('test_coco_knife.csv', index=None)