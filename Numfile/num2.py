import numpy as np
from time import process_time

pyList=[]
for i in range(1000000):
    pyList.append(i)
    
# start_time=process_time()
# pyList=[i+5 for i in range(1000000)]
# end_time=process_time()
# print(end_time-start_time)

pyList=[i for i in range(1000000)]

np_array=np.array(pyList)
start_time=process_time()
np_array +=5
end_time=process_time()
print(end_time-start_time)