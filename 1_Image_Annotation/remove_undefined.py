import os

#Change directory
main_dir = r'C:\Users\const\Desktop\dataset\test_set'

img_dir = main_dir+'\\images'
ann_dir = main_dir+'\\annotations'

#Remove annotations without image
for ann_file in os.listdir(ann_dir):
    found = False
    for img_file in os.listdir(img_dir):
        if img_file[:-3] == ann_file[:-3]:
            found = True
            break
    if found == False:
        os.remove(ann_dir+'\\'+ann_file)

#Remove images without annotation
for img_file in os.listdir(img_dir):
    found = False
    for ann_file in os.listdir(ann_dir):
        if img_file[:-3] == ann_file[:-3]:
            found = True
            break
    if found == False:
        os.remove(img_dir+'\\'+img_file)