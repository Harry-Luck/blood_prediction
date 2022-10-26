from keras.models import load_model
import numpy as np
import time

group_size = 100
model = load_model('1.h5')
base = 0
while(1):
    with open('Data.txt') as f:
        lines = f.readlines()
        length = len(lines)
        if length != base:
            total_data = [float(line.rstrip().split(':')[1]) for line in lines]
            x_test = total_data[length-group_size-1:length-1]
            base = length
            y_pred = model.predict(np.array(x_test).reshape(1,group_size,1))
            print(total_data[length-1],":",float(np.array(y_pred[0])))
    time.sleep(2)