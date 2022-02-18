#Get one string from user identify the middle character of the string

var_string = input("Enter a string :")
length_of_str=len(var_string)
print("length of string : ",length_of_str)
Mid_char=length_of_str//2
i=0 
for i in range(i,Mid_char,i+1):
    if (length_of_str%2!=0): 
        print("Middle char : ",var_string[Mid_char])
    else:
        print("Middle char : ",var_string[Mid_char-1],var_string[Mid_char])   





