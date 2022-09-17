#Big O Notation

# O(1)
import numpy as np;
a=np.array([1,2,3,4])
print(a[0])
 
# O(n)
for i in range(4):
    print(a[i])

# O(n*2)

for x in range(4):
    for y in range(4):
        print(a[x],a[y])
