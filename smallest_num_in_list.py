#Python program to find smallest number in a list

def smallest_num_in_list_1(Li):
    Li.sort()
    return(Li[0])

def smallest_num_in_list_2(Li):
    return(min(Li))       


Li = [10,4,6,9,2,5]
print(smallest_num_in_list_1(Li))
print(smallest_num_in_list_2(Li))
