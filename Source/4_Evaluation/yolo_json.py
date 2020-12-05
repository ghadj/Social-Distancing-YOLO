import json

dir = r'C:\Users\const\Desktop\dataset\test_set\data_train.txt'

f = open(dir, "r")
file = f.read()

data = {}

for line in file.split('\n'):
    elem = line.split(' ')
    filename = elem[0].split('/')[-1]
    for i in range(1, len(elem)):
        coor = elem[i].split(',')
        x_min = int(coor[0])
        y_min = int(coor[1])
        x_max = int(coor[2])
        y_max = int(coor[3])

        if filename in data:
            data[filename].append([x_min, y_min, x_max, y_max])
        else:
            data[filename] = [[x_min, y_min, x_max, y_max]]


f = open(r'C:\Users\const\Desktop\dataset\test_set\test_data_ground_truth.json', 'w')
app_json = json.dumps(data, sort_keys=True)
f.write(str(app_json))
f.close()
