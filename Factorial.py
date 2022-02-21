#Program to find the factorial of a number 

def fact(num):
    if(num>1):
        f=num*fact(num-1)
        return f
    else:
        return 1    

n=int(input("Enter a number="))
fact1=fact(n)
print("Factorial of a number is=",fact1)
