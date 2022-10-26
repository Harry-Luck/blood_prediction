import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

with open('test.txt') as f:
    lines = f.readlines()
    X = [float(line.rstrip().split(':')[0]) for line in lines]
    Y = [0 if float(line.rstrip().split(':')[1]) < 2.0  else 1 for line in lines]
X_train = X[0:650]
Y_train = Y[0:650]
X_test = X[650:]
Y_test = Y[650:]
print(Y_train)
X_train = np.array(X_train).reshape(-1,1)
Y_train = np.array(Y_train).reshape(-1,1)
X_test = np.array(X_test).reshape(-1,1)
Y_test = np.array(Y_test).reshape(-1,1)
total_size = len(X)

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(np.shape(X_train))))
model.add(LSTM(units=100))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])

# # model_lstm = Sequential()
# # model_lstm.add(LSTM(50, return_sequences = True, input_shape = (x_train.shape[1], x_train.shape[2])))
# # model_lstm.add(LSTM(units=1024, return_sequences=True))
# # model_lstm.add(LSTM(units=1024, return_sequences=True))
# # model_lstm.add(LSTM(units=50))
# # model_lstm.add(Dense(units=1, activation='relu'))
# # model_lstm.compile(loss = 'mse', optimizer = 'adam')
# # model_lstm.summary()

# model.fit(X_train, Y_train, epochs=10, batch_size=5)
# model.save('1.h5')
# score, acc = model.evaluate(X_test, Y_test, batch_size=1)
# y_pred = model.predict(X_test)
# print(score, acc)
# print(y_pred)
