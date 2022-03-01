#Find length of a string in python

#Using len method

str = input("Enter string : ")

print("Length of str using len module : ", len(str))


#Using for loop

count = 0
for i in str:
    count = count +1
print("Length of str using for loop : ", count)


#Using while loop

count = 0
while str[count:]:
    count = count +1
print("Length of str using while loop : ", count)  
    
    
