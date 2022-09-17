import numpy as np
a=np.array([1,2,3,4])
print(a)
for i in range(0,4):
    a[i]=a[i]*a[i]
print(a)
