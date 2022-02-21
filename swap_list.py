#Python program to interchange first and last elements in a list

def swap_List(Li1):

    index_1 = int(input("Enter any index index_1: "))
    index_2 = int(input("Enter any index index_2: ")) 
    
    temp_li=Li1[index_1]

    Li1[index_1]=Li1[index_2]

    Li1[index_2]=temp_li

    return(Li1)


Li1= [1,2,4,7,3,9,10]
print(swap_List(Li1))


