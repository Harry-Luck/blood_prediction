from tokenize import group
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense,Embedding, BatchNormalization
import matplotlib.pyplot as plt
group_size = 7
total = []
# print(group_size)
data = pd.read_excel('1.xlsx',sheet_name='Sheet1')
df = pd.DataFrame(data, columns= ['A+','A-','B+','B-', 'AB+', 'AB-', 'O+','O-'])
list = df.values.tolist()
total = np.array(list)
x = []
y = []
for i in range(len(list)-group_size):
    temp = total[i:i+group_size]
    x.append(temp)
    y.append(total[i+group_size])
x = np.array(x)
y = np.array(y)
train_x = x[:390]
train_y = y[:390]
test_x = x[390:]
test_y = y[390:]
len(train_x)
len(test_x)
model = Sequential()
# model.add(BatchNormalization())
model.add(LSTM(units=5, return_sequences=True, input_shape=(train_x[0].shape)))
# model.add(Dropout(0.3))
model.add(LSTM(units=5))
model.add(Dense(8))
model.compile(loss='mse', optimizer='adam')
# model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_x, train_y, epochs=30, batch_size=5, validation_data=(test_x, test_y), verbose=1, shuffle=False)

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()