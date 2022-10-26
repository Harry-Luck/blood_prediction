import numpy as np
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

arr = np.array([1, 2, 3, 1,2]).reshape(1,-1)

print(scaler.fit_transform(arr))