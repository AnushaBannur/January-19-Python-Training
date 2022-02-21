#Python program to find sum of elements in list

#sum of elements in list using function and for loop

def addtion_1(Li):
    sum = 0
    for i in Li:        
        sum = sum + i
    return sum

Li = [1, 2, 6, 4, 9, 7, 1, 0]
print("Sum of list elements : ",addtion_1(Li))


#sum of elements in list using function and while loop

def addtion_2(Li):
    sum = 0
    i = 0
    while(i<=7):        
        sum = sum + Li[i]
        i = i + 1
    return sum

Li = [1, 2, 6, 4, 9, 7, 1, 0]
print("Sum of list elements : ",addtion_2(Li))

#sum of elements in list using sum() method
Li = [1, 2, 6, 4, 9, 7, 1, 0]
print("Sum of list elements : ",sum(Li))





    
    
    
