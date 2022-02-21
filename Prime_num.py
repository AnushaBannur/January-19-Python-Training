#Python program to print all Prime numbers in an Interval

lower = int(input("Enter a lower: "))
upper = int(input("Enter a upper: "))

for num in range(lower, upper):
    if num>1:    
        for i in range(2,num):
              if(num % i == 0):
                  break
        else:
            print(num)
    


