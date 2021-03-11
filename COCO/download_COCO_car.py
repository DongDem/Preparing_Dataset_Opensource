from pycocotools.coco import COCO
import requests
import csv
coco = COCO('annotations/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['car'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
print("imgIds: ", imgIds)
print("images: ", images)


for im in images:
    print("im: ", im)
    img_data = requests.get(im['coco_url']).content
    with open('downloaded_images/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)


classes= "car"
#Download annotations
with open('annotations_download_' + classes + '.csv', mode='w', newline='') as annot:
    for im in images:
        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        for i in range(len(anns)):
            annot_writer = csv.writer(annot)
            #annot_writer.writerow([im['coco_url'], anns[i]['bbox'][0], anns[i]['bbox'][1], anns[i]['bbox'][0] + anns[i]['bbox'][2], anns[i]['bbox'][1] + anns[i]['bbox'][3], classes])
            annot_writer.writerow([ im['file_name'], int(round(im['height'])),int(round(im['width'])), classes, int(round(anns[i]['bbox'][0])), int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][0] + anns[i]['bbox'][2])), int(round(anns[i]['bbox'][1] + anns[i]['bbox'][3]))])
            #print("anns: ", im['coco_url'], anns[i]['bbox'][0], anns[i]['bbox'][1], anns[i]['bbox'][0] + anns[i]['bbox'][2], anns[i]['bbox'][1] + anns[i]['bbox'][3], 'person')
annot.close()
