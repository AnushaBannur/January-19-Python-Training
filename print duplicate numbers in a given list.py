#program to print duplicate numbers in a given list

Li = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]

new_Li = []

print(Li)

for i in Li:
    n = Li.count(i)

    if n > 1:
        if new_Li.count(i) == 0:
            new_Li.append(i)
print(new_Li)
        
        
