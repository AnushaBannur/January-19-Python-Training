##write a function to return whether middle character is vowel or not 



def middle_Char(var_string):
    vowel_Letter=[]
    vowel_List=['a', 'e', 'i', 'o', 'u'] 
    str_len=len(var_string)
    mid_char_index=str_len//2       
    mid_char=var_string[mid_char_index]
##    print(mid_char)    

    if mid_char in vowel_List:
        print(mid_char)
        
    
##    
##    for i in range(i,mid_char_index,i+1):
##        if (str_len % 2 != 0):
##            if var_string[mid_char_index] in vowel_List :
##                return (var_string[mid_char_index])
##        else:
##            for ((var_string[mid_char_index-1],var_string[mid_char_index]) in vowel_List) :
##                return (var_string[mid_char_index-1],var_string[mid_char_index])  
##

             


var_string = input("Enter string : ")
middle_Char(var_string)

        
