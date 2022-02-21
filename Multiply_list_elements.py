#Python | Multiply all numbers in the list



def multiply_1(Li):
    mul=1
    for i in Li:
        mul = mul * i
    return mul    

Li = [1,2,3,4,5]
print("Multiplication of all numbers in the list",multiply_1(Li))


def multiply_2(Li):
    mul=1
    i=0
    while(i<=4):
        mul = mul * Li[i]
        i = i + 1
    return mul    

Li = [1,2,3,4,5]
print("Multiplication of all numbers in the list",multiply_2(Li))


