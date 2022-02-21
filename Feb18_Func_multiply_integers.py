##Write a function multiply three different integers and return a int


def integer_Multiplication(int1,int2,int3):
    product=int1*int2*int3
    return(product)


integer1=int(input("Enter int1 : "))
integer2=int(input("Enter int2 : "))
integer3=int(input("Enter int3 : "))

print("Integer multiplication of int1, int2, int3 : ",integer_Multiplication(integer1,integer2,integer3))
