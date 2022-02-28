#Remove empty tuples from a list

def remove_Empty_Tuple(List_with_empty_tuple):
    List_with_empty_tuple = list(filter(None, List_with_empty_tuple))
    return List_with_empty_tuple
    

List_with_empty_tuple = [(), (1,2), ('ram', 'laxman'), (111, 222, 333), ()]

print(remove_Empty_Tuple(List_with_empty_tuple))
