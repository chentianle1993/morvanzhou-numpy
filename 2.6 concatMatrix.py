import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([[3,4,5],
              [5,6,7]])
# print(np.stack((a,b),axis=2))
# print(np.stack((a,b),axis=1))
# print(np.stack((a,b),axis=0))

print(np.concatenate((a,b),axis=0))