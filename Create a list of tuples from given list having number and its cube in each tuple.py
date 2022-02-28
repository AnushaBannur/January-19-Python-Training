# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
  
# creating a list

list1 = [1, 2, 5, 6]
res = []  

for i in list1:
    temp = (i,pow(i,3))
    print(temp)
    res.append(temp)

print(res)    
  

