#Remove multiple elements from a list in Python

#using remove method
Li1=[11, 2, 3, 15, 91, 23, 66, 100]

for i in Li1:
    if i % 2 == 0:
        Li1.remove(i)
    print(Li1)

#using del method
Li2=[10, 5, 4, 15, 56, 23, 44, 101]
del(Li2[1:3])
print(Li2)


