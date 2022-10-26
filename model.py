import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Embedding

def multi(weight, data):
    return np.dot(weight, data)/sum(weight)

group_size = 10
rate = 0.8
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
# x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
# y_train = np.array(y_train)
x_test = np.array(multi(weight, total_data[total_size-group_size-1:total_size-1]))
y_hat = total_data[total_size-1]
diff = abs(x_train - x_test)
most_min = min(diff)
index = np.where(diff == most_min)
index = int(index[0])
print(y_train[index])

# model = Sequential()
# model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train[0].shape)))
# model.add(LSTM(units=100))
# model.add(Dense(1,activation='sigmoid'))
# model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# # model_lstm = Sequential()
# # model_lstm.add(LSTM(50, return_sequences = True, input_shape = (x_train.shape[1], x_train.shape[2])))
# # model_lstm.add(LSTM(units=1024, return_sequences=True))
# # model_lstm.add(LSTM(units=1024, return_sequences=True))
# # model_lstm.add(LSTM(units=50))
# # model_lstm.add(Dense(units=1, activation='relu'))
# # model_lstm.compile(loss = 'mse', optimizer = 'adam')
# # model_lstm.summary()

# model.fit(x_train, y_train, epochs=10, batch_size=5)
# model.save('3.h5')
# y_pred = model.predict(x_test)
# print(y_hat, ":", y_pred)
