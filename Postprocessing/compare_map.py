import matplotlib.pyplot as plt

yolo = [0.8498541492235221, 0.8367965334927187, 0.832038024769675, 0.8085879519902677, 0.7711010191776417, 0.5488574909953613, 0.3786564896950986, 0.15532596814369198, 0.02125597238609824, 0.0016713867867589023]
yolo_tiny = [0.842643233068131, 0.7778794304101156, 0.700204664067667, 0.5744472220490147, 0.3762599127263797, 0.22140145401239478, 0.11720347304871084, 0.020599395638193827, 0.0010304183935061207, 0.0]
yolo = [x*100 for x in yolo]
yolo_tiny = [x*100 for x in yolo_tiny]
iou_thrs = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
fig = plt.figure('AP')
fig.suptitle('Average Precision (AP)')
plt.plot(iou_thrs, yolo, label='Person YOLOv3')
plt.plot(iou_thrs, yolo_tiny, label='Person YOLOv3-tiny')
plt.xlabel('IoU Threshold')
plt.ylabel('Average Precision (%)')
plt.legend()
plt.show()

labels = ['YOLO', 'R-CNN BB', 'SDS', 'R-CNN', 'Person YOLOv3', 'Person YOLOv3-tiny']
values = [57.9, 53.3, 50.7, 49.6, 52.04, 36.32]

fig = plt.figure('mAP_comparison')
fig.suptitle('mAP Comparison')
plt.bar(labels, values, color=['blue', 'blue', 'blue', 'blue', 'green', 'green'])
plt.xlabel('Neural Network')
plt.ylabel('mAP (%)')
plt.xticks(rotation=10)
plt.show()