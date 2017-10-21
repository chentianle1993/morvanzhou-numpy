import numpy as np

a = np.array([
    [1,2,3],
    [2,3,4]
])
b = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

c = np.arange(1,13,1).reshape(3,2,2) #类型为整数
d = np.linspace(1,12,12).reshape(3,2,2) #类型为小数
# c.shape= (3,2,2)
# c的最外层是三个对象构成，最里层是两个对象，即：
# c=[[[ 1  2]
#   [ 3  4]]
#
#  [[ 5  6]
#   [ 7  8]]
#
#  [[ 9 10]
#   [11 12]]]
e = np.arange(1,13,1)
print(e.shape)
e[:,np.newaxis].shape# (12,1)