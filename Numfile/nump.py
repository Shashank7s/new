import numpy as np

a=np.array([1,2,3,4,5,6])
a=a.reshape(3,2)
a1=a.reshape(2,-1)
a2=a.ravel()
print(a)
print(a1)
print(a2)