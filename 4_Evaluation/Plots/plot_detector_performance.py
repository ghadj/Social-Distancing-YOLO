import matplotlib.pyplot as plt
import numpy as np

file_read = open(r'C:\Users\const\Desktop\test\test_data_output.txt', 'r')
file_content = file_read.read()

time_yolo = []
for line in file_content.split('\n'):
    if 'Time spent:' in line:
        line_split = line.split(' ')
        time_yolo.append(float(line_split[2][:-3]))
file_read.close()

file_read = open(r'C:\Users\const\Desktop\test\test_data_output_tiny.txt', 'r')
file_content = file_read.read()

time_yolo_tiny = []
for line in file_content.split('\n'):
    if 'Time spent:' in line:
        line_split = line.split(' ')
        time_yolo_tiny.append(float(line_split[2][:-3]))

time_yolo = time_yolo[1:]
time_yolo_tiny = time_yolo_tiny[1:]

fig = plt.figure('Detector Speed')
fig.suptitle('Detector Speed')
plt.plot(range(0, len(time_yolo)), time_yolo, label='Person YOLOv3')
plt.plot(range(0, len(time_yolo_tiny)), time_yolo_tiny, label='Person YOLOv3-tiny')
plt.xlabel('Image ID')
plt.ylabel('Time (sec)')
plt.legend()
plt.show()

fig = plt.figure('Detector FPS')
fig.suptitle('Detector FPS')
x_labels = ['Person YOLOv3', 'Person YOLOv3-tiny']
y_labels = [len(time_yolo)/np.sum(time_yolo), len(time_yolo_tiny)/np.sum(time_yolo_tiny)]
plt.ylabel('Frames per Second (FPS)')
plt.bar(x_labels, y_labels)
plt.show()