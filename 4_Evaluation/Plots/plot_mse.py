import matplotlib.pyplot as plt

file_read = open(r'C:\Users\const\Desktop\train\yolo.txt', 'r')
file_content = file_read.read()

train_error = []
val_error = []
for line in file_content.split('\n'):
    if 'val_loss' in line:
        i = 0
        line_split = line.split(' ')
        for elem in line_split:
            if elem == 'loss:':
                train_error.append(float(line_split[i + 1]))
            if elem == 'val_loss:':
                val_error.append(float(line_split[i + 1]))
            i+=1

epochs = list(range(1, len(train_error)+1))

fig = plt.figure()
fig.suptitle('YOLOv3 Neural Network Training on our Database')
plt.plot(epochs, train_error, label='Training Error')
plt.plot(epochs, val_error, label='Validation Error')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()
