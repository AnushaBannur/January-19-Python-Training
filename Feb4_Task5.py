##Task5:
##
##Collect two strings from user
##
##string1: wikipedia
##string2: typescript
##
##output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
##(ord , chr)====>use these inbuilt methods for find the ascii values

str1=input("Enter str1:")
str2=input("Enter str2:")

length_of_str1=len(str1)
Mid_char_str1_position=length_of_str1//2
Mid_char_str1=str1[Mid_char_str1_position]
print("Middle char of str1: ",Mid_char_str1)
Mid_char_str1_ascii_val=ord(Mid_char_str1)
print("Middle char ascii val of str1: ",Mid_char_str1_ascii_val)

length_of_str2=len(str2)
Mid_char_str2_position=length_of_str2//2
Mid_char_str2=str2[Mid_char_str2_position]
print("Middle char of str2: ",Mid_char_str2)
Mid_char_str2_ascii_val=ord(Mid_char_str2)
print("Middle char ascii val of str2: ",Mid_char_str2_ascii_val)

print("Sum of the ascii values of the mid chars of the str1 and str2: ",Mid_char_str1_ascii_val+Mid_char_str2_ascii_val)
