import xml.etree.ElementTree as ET
import os
import csv

save_path = "test_coco_xml"
train_csv = 'test.csv'
'''
with open(train_csv) as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        filename_value = row[0]
        width_value = row[1]
        height_value = row[2]
        name_value = row[3]
        xmin_value = row[4]
        ymin_value = row[5]
        xmax_value = row[6]
        ymax_value = row[7]


        # create the file structure
        annotation = ET.Element('annotation')

        folder = ET.SubElement(annotation, 'folder')
        folder.text = 'images'
        filename = ET.SubElement(annotation, 'filename')
        filename.text = filename_value
        path = ET.SubElement(annotation, 'path')
        path.text = filename_value

        source = ET.SubElement(annotation, 'source')
        database= ET.SubElement(source, 'database')
        database.text = 'Unknown'

        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        width.text = width_value
        height = ET.SubElement(size, 'height')
        height.text = height_value
        depth = ET.SubElement(size, 'depth')
        depth.text = "3"


        segmented =  ET.SubElement(annotation, 'segmented')
        segmented.text = '0'
        object =  ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name')
        name.text = name_value
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = ET.SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = '0'

        bndbox = ET.SubElement(object, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        xmin.text = xmin_value
        ymin = ET.SubElement(bndbox, 'ymin')
        ymin.text = ymin_value
        xmax = ET.SubElement(bndbox, 'xmax')
        xmax.text = xmax_value
        ymax = ET.SubElement(bndbox, 'ymax')
        ymax.text = ymax_value

        # create a new XML file with the results
        mydata = ET.tostring(annotation)
        myfile = open(os.path.join(save_path, str(i)+ ".xml"), "wb")
        myfile.write(mydata)
        i+=1
'''
for file in os.listdir(save_path):
    cmd_str1 = ' xmllint {} --format > {}'.format(os.path.join(save_path,file), os.path.join("test_modify_xml", file))
    os.system(cmd_str1)
