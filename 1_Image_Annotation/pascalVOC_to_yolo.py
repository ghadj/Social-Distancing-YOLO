import os
import re

main_dir = r'C:\Users\const\Desktop\dataset\INRIAPerson-part'
ann_type = 'txt'

img_dir = main_dir+'\\images'
ann_dir = main_dir+'\\annotations'
file_write = open(main_dir+'\\data_train.txt', 'w')
class_id = 0

x_mix = y_min = x_max = y_max = 0

for filename in os.listdir(img_dir):
    ann_path = os.path.join(ann_dir, filename[:-3]+ann_type)
    file_read = open(ann_path, 'r')
    file_content = file_read.read()

    file_write.write('/home/ubuntu/TrainYourOwnYOLO/Data/Source_Images/Training_Images/'+filename)

    for line in file_content.split('\n'):
        if 'xmin' in line:
            x_mix = re.split('<|>', line)[2]
        if 'ymin' in line:
            y_min = re.split('<|>', line)[2]
        if 'xmax' in line:
            x_max = re.split('<|>', line)[2]
        if 'ymax' in line:
            y_max = re.split('<|>', line)[2]
            file_write.write(' '+x_mix+','+y_min+','+x_max+','+y_max+','+str(class_id))

    file_write.write('\n')
    file_read.close()
file_write.close()