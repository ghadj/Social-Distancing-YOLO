import pandas as pd
import json

dir = r'C:\Users\const\Desktop\dataset\INRIAPerson\data_train.txt'

f = open(dir, "r")
file = f.read()

data = {}

for line in file.split('\n'):
    elem = line.split(' ')
    filename = elem[0].split('/')[-1]
    data[filename] = {'boxes':[], 'scores':[]}

dir = r'C:\Users\const\Desktop\dataset\test_set\Detection_Results_tiny.csv'
f = open(dir, "r")

df = pd.read_csv(dir)

for index, row in df.iterrows():
    data[str(row['image'])]['boxes'].append([row['xmin'], row['ymin'], row['xmax'], row['ymax']])
    data[str(row['image'])]['scores'].append(row['confidence'])

f = open(r'C:\Users\const\Desktop\dataset\test_set\test_data_predictions_tiny.json', 'w')

app_json = json.dumps(data, sort_keys=True)
f.write(str(app_json))
f.close()



