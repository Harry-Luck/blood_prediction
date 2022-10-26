import numpy as np
import time

group_size = 25

def multi(weight, data):
    return np.dot(weight, data)/sum(weight)

with open('Data.txt') as f:
    lines = f.readlines()
    total_data = [float(line.rstrip().split(':')[1]) for line in lines]
total_data = np.array(total_data).reshape(-1,1)
weight = [i+1 for i in range(group_size)]
total_size = len(total_data)

x_train = []
y_train = []

for i in range(group_size, total_size-1, 1):
    temp = total_data[i-group_size:i]
    # multi = np.dot(weight, temp)/sum(weight)
    data = multi(weight, temp)
    x_train.append(data)
    y_train.append(0 if total_data[i]<2 else 1)
x_train = np.array(x_train)

base = 0
count = 0
pos = 0
predict = 0
while(1):
    with open('Data.txt') as f:
        lines = f.readlines()
        total_data = [float(line.rstrip().split(':')[1]) for line in lines]
        length = len(lines)
        if length != base:
            last = total_data[length-1]
            count += 1
            if ((float(last) < 2 and int(predict) == 0) or (float(last) >=2 and int(predict) ==1)):
                pos+=1
            base = length            
            x_test = np.array(multi(weight, total_data[length-group_size:length]))
            diff = abs(x_train - x_test)
            most_min = min(diff)
            index = np.where(diff == most_min)
            index = int(index[0][0])
            predict = y_train[index]
            print(last,":",predict, "(", pos/count*100,")")
    time.sleep(2)