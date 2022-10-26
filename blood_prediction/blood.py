from tokenize import group
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense,Embedding, BatchNormalization
group_size = 7
total = []
# print(group_size)
data = pd.read_excel('1.xlsx',sheet_name='Sheet1')
df = pd.DataFrame(data, columns= ['A+','A-','B+','B-', 'AB+', 'AB-', 'O+','O-'])
list = df.values.tolist()
for i in range(len(list)):
    total.append(df.iloc[i])
total = np.array(total)
train_x = []
train_y = []
for i in range(len(list)-group_size):
    temp = total[i:i+group_size]
    train_x.append(temp)
    train_y.append(total[i+group_size])
train_x = np.array(train_x)
train_y = np.array(train_y)
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(train_x[0].shape)))
model.add(LSTM(units=50))
# model.add(Dense(8,activation='softmax'))
model.add(Dense(8))
# model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_x, train_y, epochs=40, batch_size=5)
# model.save('1.h5')