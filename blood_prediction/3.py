import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

np.random.seed(42)

df = pd.read_excel('1.xlsx')
Predict_Case = ['A+','A-','B+','B-','AB+','AB-','O+','O-']
df.set_index('Record Date', inplace=True)
df.index = pd.to_datetime(df.index)
days_to_predict = 30

# This will split data into X & Y value
def data_split(data, look_back=1):
    x, y = [], []
    for i in range(len(data) - look_back - 1):
        a = data[i:(i + look_back), 0]
        x.append(a)
        y.append(data[i + look_back, 0])
    return np.array(x), np.array(y)

for i in range(1):
    dataset = df.filter([Predict_Case[i]])
    # print(dataset.head())
    # Creating train & test data for testing
    test_size = int(dataset.shape[0] * 0.3)
    train = dataset[:-test_size]
    test = dataset[-test_size:]
    # print(len(train))
    # Data normalization
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler = scaler.fit(dataset)
    all = scaler.transform(dataset)
    train = scaler.transform(train)
    test = scaler.transform(test)

    # Splitting data to get X & Y value
    look_back = 5
    X_all, Y_all = data_split(all, look_back=look_back)
    X_train, Y_train = data_split(train, look_back=look_back)
    X_test, Y_test = data_split(test, look_back=look_back)

    # We need to convert the shape of the data to LSTM shape format (samples, timesteps, features)
    # To make a model can learning from a sequence, we'll using timesteps for timeseries prediction
    X_all = np.array(X_all).reshape(X_all.shape[0], 1, 1)
    Y_all = np.array(Y_all).reshape(Y_all.shape[0], 1)
    X_train = np.array(X_train).reshape(X_train.shape[0], 1, 1)
    Y_train = np.array(Y_train).reshape(Y_train.shape[0], 1)
    X_test = np.array(X_test).reshape(X_test.shape[0], 1, 1)
    Y_test = np.array(Y_test).reshape(Y_test.shape[0], 1)

    print("sefsfsefsefs",X_train, "seefsefsefes")


    # And, this is the LSTM timeseries prediction model
    batch_size = 5
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, 
                batch_input_shape=(batch_size, X_train.shape[1], X_train.shape[2]), 
                stateful=True))
    model.add(LSTM(50, stateful=True))
    model.add(Dense(Y_train.shape[1]))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Fit the model with all data AP
    epoch = 10
    loss = []
    for j in range(epoch):
        print('Iteration ' + str(j + 1) + '/' + str(epoch))
        model.fit(X_all, Y_all, batch_size=batch_size, 
                epochs=1, verbose=1, shuffle=False)
        h = model.history
        loss.append(h.history['loss'][0])
        model.reset_states()

    # Predicting with train data
    # This will also set predict input (previous input) into LSTM state which is useful to predict future value
    all_predict = model.predict(X_all, batch_size=batch_size)

    # Predicting future value up to n-days
    # In our case, we're going to predict up to `DAYS_TO_PREDICT` days in the future
    future_predict = []
    pred_samples = all_predict[-1:]
    pred_samples = np.array([pred_samples])
    for p in range(days_to_predict):
        pred = model.predict(pred_samples, batch_size=batch_size)
        pred = np.array(pred).flatten()
        future_predict.append(pred)
        new_samples = np.array(pred_samples).flatten()
        new_samples = np.append(new_samples, [pred])
        new_samples = new_samples[1:]
        pred_samples = np.array(new_samples).reshape(1, 1, 1)
    future_predict = np.array(future_predict).reshape(len(future_predict), 1, 1)

    # Predict using previous future prediction
    f_future_predict = model.predict(future_predict, batch_size=batch_size)

    # Reset LSTM input state for safety
    model.reset_states()

    X_all_flatten = np.array(scaler.inverse_transform(np.array(X_all).reshape(X_all.shape[0], 1))).flatten().astype('int')
    X_all_flatten = np.absolute(X_all_flatten)
    Y_all_flatten = np.array(scaler.inverse_transform(np.array(Y_all).reshape(Y_all.shape[0], 1))).flatten().astype('int')
    Y_all_flatten = np.absolute(Y_all_flatten)
    all_predict_flatten = np.array(scaler.inverse_transform(np.array(all_predict).reshape(all_predict.shape[0], 1))).flatten().astype('int')
    all_predict_flatten = np.absolute(all_predict_flatten)
    future_predict_flatten = np.array(scaler.inverse_transform(np.array(future_predict).reshape(future_predict.shape[0], 1))).flatten().astype('int')
    future_predict_flatten = np.absolute(future_predict_flatten)
    f_future_predict_flatten = np.array(scaler.inverse_transform(np.array(f_future_predict).reshape(f_future_predict.shape[0], 1))).flatten().astype('int')
    f_future_predict_flatten = np.absolute(f_future_predict_flatten)
    # Getting RMSE scores
    all_predict_score = math.sqrt(mean_squared_error(Y_all_flatten, all_predict_flatten))
    print('All Score: %.2f RMSE' % (all_predict_score))
    # Generate future index(dates)
    future_index = pd.date_range(start=dataset.index[-1], periods=days_to_predict + 1, closed='right')
    print(future_index)
    print('Future Prediction up to ' + str(days_to_predict) + ' days Based on ' + Predict_Case[i] + ' :', future_predict_flatten)