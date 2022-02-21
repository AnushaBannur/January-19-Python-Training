#Python program to find second largest number in a list


def second_largest_num_in_list(Li):
    Li.sort()
    return(Li[-2])

Li = [10,4,6,15,2,5]
print(second_largest_num_in_list(Li))

