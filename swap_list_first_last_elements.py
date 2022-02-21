#Python program to interchange first and last elements in a list

def swap_First_Last_elements(Li1):

    index_0, last_index = 0, -1
    
    temp_li=Li1[index_0]

    Li1[index_0]=Li1[last_index]

    Li1[last_index]=temp_li

    return(Li1)


Li1= [1,2,4,7,3,9,10]
print(swap_First_Last_elements(Li1))


