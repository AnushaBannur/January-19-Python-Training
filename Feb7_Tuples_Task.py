####Tuples

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9) 
tup1=(1,4,5,6,7,8)
print(tup1)
tup2=5,6,7,8,9  #we can create tuple without specifying round bracket but comma(,) is mandatory
print(tup2)


#Find the common elements between two tuples
tup1=(1,4,5,6,7,8)
tup2=(5,6,7,8,9)
List=[]

for i in tup1:
    if i in tup2:
        List.append(i)
print(List)


#Concatenate both tuples and remove duplicates from tuple
tup1=(1,4,5,6,7,8)
tup2=(5,6,7,8,9)
tup3=tup1 + tup2
print("Concatenated tuple:", tup3)

#remove duplicates from tuple
List=[]

for i in tup3:
    if i not in List:
        List.append(i)

tup4=tuple(List)
print("Concatenated string after duplicates removal : ", tup4 )

#Find the index value of 9 (after concatenation)

print(tup3.index(9))

#multiply above elements 3 times

print(tup4 * 3)


