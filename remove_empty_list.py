#Python – Remove empty List from List


Li=[11, 2, [], 15, 91, [], 66, 100,[]]
print("List with empty list",Li)
for i in Li:
    if i == []:
        Li.remove([])
print("List without empty list",Li)
