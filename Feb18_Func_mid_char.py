##Write a function to return middle char of the string


def middle_Char(var_string):
    str_len=len(var_string)
    mid_char_index=str_len//2
    i=0
    for i in range(i,mid_char_index,i+1):
        if (str_len % 2 != 0):
            print(var_string[mid_char_index])
        else:
            print(var_string[mid_char_index-1],var_string[mid_char_index])

             


var_string = input("Enter string : ")
middle_Char(var_string)
        
    
    
