#collect three strings from user  name<space>float
#add float values for example 10.30 + 12.19 + 20.20 ===> output ===> add it 42.69

string1=input("Enter name of the person1 and the percentage ")
string2=input("Enter name of the person2 and the percentage ")
string3=input("Enter name of the person3 and the percentage ")

# split method splits the string at white spaces
string1_split=string1.split()
print(string1_split[-1])
string2_split=string2.split()
print(string2_split[-1])
string3_split=string3.split()
print(string3_split[-1])

Sum=float(string1_split[-1])+float(string2_split[-1])+float(string3_split[-1])

print("Sum of float values:",Sum)





