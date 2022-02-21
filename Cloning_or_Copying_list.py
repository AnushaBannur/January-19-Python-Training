#Python | Cloning or Copying a list

#using slicing

def cloning_list_1(Li):
    list_copy = Li[:]
    return(list_copy)


#using extend method

def cloning_list_2(Li):
    list_copy = []
    list_copy.extend(Li)
    return(list_copy)

#using copy method

def cloning_list_3(Li):
    list_copy = []
    list_copy=Li1.copy()
    return(list_copy)

#using assignment of one list to another

def cloning_list_4(Li):
    list_copy = Li
    return(list_copy)

#using append method

def cloning_list_5(Li):
    list_copy = []
    for i in Li:
        list_copy = list_copy.append(i)
    return(list_copy)


Li = [2,1,4,6,9,10]
Li1 = cloning_list_1(Li)
print(Li1)
Li2 = cloning_list_2(Li)
print(Li2)
Li3 = cloning_list_3(Li)
print(Li3)
Li4 = cloning_list_4(Li)
print(Li4)
Li5 = cloning_list_4(Li)
print(Li5)
