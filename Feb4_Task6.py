##Task6:
##
##collect one string from user:
##
##string: computer
##output: c6r
##
##string: mathematics
##output: m9s

str1=input("Enter string:")
string_len=len(str1)
string_len_1=string_len-2
               
print(str1[0]+str(string_len_1)+str1[-1])

