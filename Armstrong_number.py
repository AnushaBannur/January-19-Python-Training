#Python Program to check Armstrong Number

num=int(input("Enter a number : "))

sum = 0

temp = num

while (temp>0):
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp//10

if(num == sum):
    print("Num is an Armstrong", num)
else:
    print("Num is not an Armstrong", num)

