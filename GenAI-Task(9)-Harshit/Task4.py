# 4.Aggregation  Operations
import numpy as np
data = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
rsum = np.sum(data,axis = 1) #Row wise sum
csum = np.sum(data,axis = 0) #Col wise sum
mini = np.min(data)
maxi = np.max(data)
mean = np.mean(data)

print(rsum)
print(csum)
print(mini)
print(maxi)
print(mean)