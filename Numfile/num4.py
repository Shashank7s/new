import numpy as np
a=np.array([[1,2,3],[4,5,6]],dtype=np.int32)
b=np.array([[4,6,8],[7,8,9]],dtype=np.int32)
# print(a,b)
c=np.concatenate([a,b])
print(c)