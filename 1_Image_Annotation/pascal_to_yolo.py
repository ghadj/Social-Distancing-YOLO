import os
import re

img_dir = r'C:\Users\const\Desktop\dataset\test_set\images'
ann_dir = r'C:\Users\const\Desktop\dataset\test_set\annotations'
file_write = open(r'C:\Users\const\Desktop\dataset\test_set\data_train.txt', 'w')
class_id = 0

for filename in os.listdir(img_dir):
    ann_path = os.path.join(ann_dir, filename[:-3]+'txt')
    file_read = open(ann_path, 'r')
    file_content = file_read.read()

    file_write.write('/home/ubuntu/TrainYourOwnYOLO/Data/Source_Images/Training_Images/'+filename)
    for line in file_content.split('\n'):
        if 'Bounding box for object' in line:
            #print(line)
            line_split = line.split(' ')
            x_mix = line_split[12].replace('(', '').replace(',', '')
            y_min = line_split[13].replace(')', '')
            x_max = line_split[15].replace('(', '').replace(',', '')
            y_max = line_split[16].replace(')', '')
            (x_mix, y_min, x_max, y_max)
            file_write.write(' '+x_mix+','+y_min+','+x_max+','+y_max+','+str(class_id))
    file_write.write('\n')
    file_read.close()
file_write.close()