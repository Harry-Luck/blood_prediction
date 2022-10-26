from random import randint
from numpy import array
from numpy import argmax
from pandas import concat
from pandas import DataFrame
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import math
import numpy as np

# # def generate_sequence(length=25):
# #     return [randint(0, 99) for _ in range(length)]

# # one hot encode sequence
# def one_hot_encode(sequence, n_unique=10):
#     encoding = list()
#     for value in sequence:
#         vector = [0 for _ in range(n_unique)]
#         vector[value-1] = 1
#         encoding.append(vector)
#     return array(encoding)

# def one_hot_encode_label(number, n_unique=10):
#     vector = [0 for _ in range(n_unique)]
#     vector[number-1] = 1
#     return array(vector)

# # decode a one hot encoded string
# def one_hot_decode(encoded_seq):
#     return [argmax(vector) for vector in encoded_seq]

# def generate_data(encoded):
#     df = DataFrame(encoded)
#     df = concat([df.shift(4), df.shift(3), df.shift(2), df.shift(1), df], axis=1)
#     values = df.values
#     values = values[5:,:]
#     # convert to 3d for input
#     X = values.reshape(len(values), 5, 10)
#     # drop last value from y
#     # y = encoded[4:-1,:]
#     return X

# group_size = 100
# total_data = []
# with open('test.txt') as f:
#     lines = f.readlines()
#     length = len(lines)
#     for line in lines:
#         temp1 = math.floor(float(line.rstrip().split(':')[1])) 
#         if temp1 < 10:
#             total_data.append(temp1)
#         else:
#             total_data.append(10)
# # for i in range(group_size, length-1, 1):
# model = Sequential()
# model.add(LSTM(50, batch_input_shape=(5, 5, 10), stateful=True))
# model.add(Dense(10, activation='softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

# for i in range(group_size, group_size+5, 1):
#     temp_train_data = total_data[i-group_size:i]
#     encoded = one_hot_encode(temp_train_data)
#     X = generate_data(encoded)
#     y = one_hot_encode_label(total_data[i]).reshape(-1,1)
#     model.fit(X, y, epochs=1, batch_size=5, verbose=2, shuffle=False)
#     model.reset_states()
# model.save('2.h5')
# X_test_data = total_data[length-group_size : length]
# X_test_encoded = one_hot_encode(X_test_data)
# X_test = generate_data(X_test_encoded)
# y_test = one_hot_encode_label(total_data[length])
# yhat = model.predict(X_test)
# print(y_test, yhat)



# # for i in range(500):
# #     X, y = generate_data()
# #     
# # X, y = generate_data()
# # yhat = model.predict(X, batch_size=5)
# # print('Expected:  %s' % one_hot_decode(y))
# # print('Predicted: %s' % one_hot_decode(yhat))



test = [[[2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7]],
        [[2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7]],
        [[2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7]],
        [[2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7]],
        [[2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7]]]
print(np.array(test).shape)
