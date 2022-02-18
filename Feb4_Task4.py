##Task4:
##
###collect two strings from user
##
##string1: python
##String2: java
##
##output ===> jythonpava64hv
##
##string1: maths
##string2: science
##
##output ===> sathsmcience57te
##

str1=input("Enter str1:")
str2=input("Enter str2:")

#Get one string from user identify the middle character of the string

length_of_str1=len(str1)
Mid_char_str1=length_of_str1//2

length_of_str2=len(str2)
Mid_char_str2=length_of_str2//2

print(str2[0]+str1[1:]+str1[0]+str2[1:]+str(len(str1))+str(len(str2))+str1[Mid_char_str1]+str2[Mid_char_str2])


      
