import numpy as np

arr=np.array([1,2,3,2,4,1,5,6,7,4,6,6,6])
mostfrequentvalue=np.bincount(arr).argmax()
print(mostfrequentvalue)