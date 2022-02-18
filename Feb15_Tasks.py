##========================
##Feb 15
##=========================


#Task1

#hackerrank Write a function

#Task2

#hackerrank Python If-Else

#Task3

#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

num=int(input("Enter a number = "))

if(num%3==0):
    print("Fizz")
elif(num%5==0):
    print("buzz")
elif(num%3==0 and num%5==0):
    print("Fizzbuzz")
else:
    print("Invalid number")


##Task4:

#Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL


#93 ===> A
#99 ===> A
#88 ====> B

#78

#VALID MARK (between 0 to 100)
#PASS MARK (50 +)
#C

#65

mark=int(input("Enter a mark = "))

if(0<=mark<=100):
    print("Valid mark")
    if(0<=mark<=49):
        print("FAIL")
    else:
        print("PASS")
        if(50<=mark<=59):
            print("E")
        elif(60<=mark<=69):
            print("D")
        elif(70<=mark<=79):
            print("C")
        elif(80<=mark<=89):
            print("B")
        elif(90<=mark<=100):
            print("A")        
else:
    print("Invalid mark")


##Task 5:
##
###collect three marks from user
###calculate mark1 + mark2 + mark3 / 100
##
##if calculate > 90 ===> Grade A
##if calculate > 75 ==> Grade B
##calculate > 50  ==> grade C
##Other wise ===> Grade D

mark1=int(input("Enter a mark1 = "))
mark2=int(input("Enter a mark2 = "))
mark3=int(input("Enter a mark3 = "))

calculate= (mark1 + mark2 + mark3) / 100

if(calculate>90):
    print("Grade A")
elif(calculate>75):
    print("Grade B")
elif(calculate>50):
    print("Grade C")
else:
    print("Grade D")
    

        
        
