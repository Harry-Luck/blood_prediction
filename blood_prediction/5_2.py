import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

from keras.layers import Bidirectional
from keras.layers import Flatten
from keras.layers import TimeDistributed
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

# np.random.seed(42)

# df = pd.read_excel('1.xlsx')
df = pd.read_csv('2.csv')
Predict_Case = ['A+','A-','B+','B-','AB+','AB-','O+','O-']
df.set_index('Record Date', inplace=True)
df.index = pd.to_datetime(df.index)
days_to_predict = 30

def data_split(data, look_back=1):
    x, y = [], []
    for i in range(len(data) - look_back - 1):
        a = data[i:(i + look_back), 0]
        x.append(a)
        y.append(data[i + look_back, 0])
    return np.array(x), np.array(y)

for i in range(1):
    i = 0
    dataset = df.filter([Predict_Case[i]])
    # print(dataset)
    test_size = int(dataset.shape[0] * 0.3)
    all = dataset[:]
    train = dataset[:-test_size]
    test = dataset[-test_size:]


    # scaler = MinMaxScaler(feature_range=(-1, 1))
    # scaler = scaler.fit(dataset)
    # all = scaler.transform(dataset)
    # train = scaler.transform(train)
    # test = scaler.transform(test)
    all =all.values.tolist()
    all = np.array(all)
    train =train.values.tolist()
    train = np.array(train)
    test = test.values.tolist()
    print(len(test))
    test = np.array(test)

    look_back = 300
    X_all, Y_all = data_split(all, look_back=look_back)
    X_train, Y_train = data_split(train, look_back=look_back)
    X_test, Y_test = data_split(test, look_back=look_back)

    # batch_size = 30
    # model = Sequential()
    # # model.add(Bidirectional(LSTM(units=30, activation='relu', return_sequences=True, input_shape=(1,look_back))))
    # model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(1,look_back)))
    # model.add(LSTM(units=50))
    # # model.add(Dense(1))
    # model.add(Dense(1))
    # # model.compile(loss='mean_squared_error', optimizer='adam')
    # model.compile(loss='mse', optimizer='adam')
    model = Sequential()
    model.add(TimeDistributed(Conv1D(filters=64, kernel_size=1, activation='relu'), input_shape=(None, 1,look_back)))
    model.add(TimeDistributed(MaxPooling1D(pool_size=2)))
    model.add(TimeDistributed(Flatten()))
    model.add(LSTM(50, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
    X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])
    # print(X_train.shape) 
    # x = x.reshape(1, x.shape[0], x.shape[1])
    # history = model.fit(X_train, Y_train, epochs=30, batch_size=6, validation_data=(X_test, Y_test), verbose=1, shuffle=False)
    history = model.fit(X_train, Y_train, epochs=30, batch_size=6, validation_data=(X_test, Y_test), verbose=1)

    # plt.plot(history.history['loss'], label='train')
    # plt.plot(history.history['val_loss'], label='test')
    # plt.legend()
    # plt.show()

    X_data1 = X_train[0:1]
    def change(datax1, pred):
        for j in range(look_back-1):
            datax1[0, 0, j] = datax1[0, 0, j+1]
            # print("ssssefef",datax[i])
        datax1[0, 0, look_back-1] = pred    
        return datax1

    future_predict = []
    for k in range(30):
        pred = model.predict(X_data1)
        pred1 = change(X_data1, pred)
        # print(k, "awdwd", pred, "adawdawd")
        pred = np.array(pred).flatten()
        future_predict.append(pred)

    all_predict_flatten = np.array(future_predict).flatten().astype('int')

    all_predict_flatten = np.absolute(all_predict_flatten)
    # print(all_predict_flatten)
    print('Future Prediction up to ' + str(days_to_predict) + ' days Based on ' + Predict_Case[i] + ' :', all_predict_flatten)

    # diff = []
    # for k in range(30):
    #     diff[k]= Y_test[k] - all_predict_flatten[k]
    # print("difference of real value", diff)
    model.reset_states()

