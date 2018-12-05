import numpy as np
x = np.array([1, 2, 3, 3, 0, 1, 4])
w = np.array([0.3,0.5,0.7,0.6,0.1,-0.9,1])
print(x)
print(np.bincount(x))
print(np.bincount(x,weights=w))
print(np.bincount(x,minlength=7))

x = [[1,3,3],
     [7,5,2]]
print(np.argmax(x,axis=0))
x = [[1,3,3],
     [7,5,2]]
print(np.argmax(x,axis=1))

x = np.array([1, 3, 2, 3, 0, 1, 0])
print(x.argmax())

x = np.array([1, 2, 3, 3, 0, 1, 4])
print(np.argmax(np.bincount(x)))