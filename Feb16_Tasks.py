##===============================
##Feb 16
##==============================
##
##Task1:

###Using Range function  print multiples of 5 from 0 to 75
##
##for i in range(0,75):
##    if (i % 5 == 0):
##        print("Multiples of 5 : ",i)
##
###Using Range function  print multiples of 8 from 0 to 72
##
##for i in range(0,72):
##    if (i % 8 == 0):
##        print("Multiples of 8 : ",i)    
##
###Using Range function  print multiples of 5 from 75 to 0
##
##for i in range(75,0,-1):
##    if (i % 5 == 0):
##        print("Multiples of 5 : ",i)
##        
###Using Range function  print multiples of 8 from 96 to 72
##
##for i in range(96,72,-1):
##    if (i % 8 == 0):
##        print("Multiples of 8 : ",i)

##Task2:
##
##Get a dynamic list from user        

##Li1=[]
##n=int(input("Enter no of elements:")
##for i in range(0,n):
##    list_ele=int(input("enter val :"))
##    Li1.append(list_ele)
##print(Li1)


##Task3:
##
##Get a dynamic dictionary from user

##Li1=[]
##Li2=[]
##n=int(input("Enter no of elements:"))
##for i in range(0,n):
##    keys=int(input("Enter keys:"))  
##    vals=input("enter val :")
##    Li1.append(keys)
##    Li2.append(vals)
##print(dict(zip(Li1,Li2)))              
             


##Task4:
##
##Get two integers from user
##print multiples of 8 between them
##
##clues:
##Use range function in for loop
##Use if condition inside for loop
##add in to list
##
##input 10 100
##multiples of 8
##
##[16,24,32.....,96]

##int1=int(input("Enter integer1:"))
##int2=int(input("Enter integer2:"))
##Li1=[]
##for i in range(int1,int2):
##    if(i%8==0):
##        Li1.append(i)
##        print("Multiples of 8:",Li1)


##Task5:
##
##Input:
##Li1 = [3,4,5,2,7,8,9,10]
##
##Output:
##Li_odd = [3,5,7,9]
##Li_even = [4,2,8,10]
##
##
##Li1 = [3,4,5,2,7,8,9,10]
##
##for i in Li1:
##    if(i % 2 == 0):
##        print("Li_even")
##    else:
##        print("Li_odd")


##Task6:
##
##Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
##    
##Output:
##neg_LI = [-1,-7,-3]
##pos_LI = []
##Zeros = []
##
##Numeber of postivie ele: 7
##Number nega: 3
##Number of zeros: 2

##Li1= [-1, -7,8,10,20,21,17,28,-3,0,0,]
##pos_Li=[]
##neg_Li=[]
##zero_Li=[]
##
##for i in Li1:
##    if (i > 0):
##        pos_Li.append(i)
##        print("Positive vals in the list: ",pos_Li)
##    elif (i < 0):
##        neg_Li.append(i)
##        print("Negative vals in the list: ",neg_Li)
##    else:
##        zero_Li.append(i)
##        print("Zeros in the list: ",zero_Li)


##Task7:
##
##Study range function and for loop properly
##
##print(list(range(5)))
##print(list(range(1,5)))
##print(list(range(5,20)))
##print(list(range(-5,5)))
##print(list(range(10,100,10)))
##print(list(range(10,0,-1)))
##print(list(range(-5,5,3)))
##print(list(range(10,100,5)))
##print(list(range(10,0,-2)))

for i in range(5):
    print(list(range(5)))

for i in range(1,5):
    print(list(range(1,5)))

for i in range(5,20):    
    print(list(range(5,20)))

for i in range(-5,5):    
    print(list(range(-5,5)))

for i in range(10,100,10):
    print(list(range(10,100,10)))

for i in range(10,0,-1):    
    print(list(range(10,0,-1)))

for i in range(-5,5,3):    
    print(list(range(-5,5,3)))

for i in range(10,100,5):    
    print(list(range(10,100,5)))

for i in range(10,0,-2):    
    print(list(range(10,0,-2)))    

        
         

