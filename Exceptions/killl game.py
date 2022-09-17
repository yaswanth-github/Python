l = list(range(1,101))
# print(l)
print(len(l))
a=0
while len(l) != 1:
    j=100
    while len(l) == j:
        i=1
        print(l)
        del l[i]
        i=+2
        j=j/2

print(l)