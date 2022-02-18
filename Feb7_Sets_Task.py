## Sets

#Create two empty sets

set1={} # if just curly braces are provided the dic will be created and not set
print(type(set1)) 
set1=set() # to create set we need to use set() method
print(type(set1))
set2=set()
print(type(set2))

#update set1 with 7,8,9,1,2,3,4,5,0
set3={7,8,9,1,2,3,4,5,0}
set1.update(set3)
print(set1)

#update set2 with 4,5,6,0
set4={4,5,6,0}
set2.update(set4)
print(set2)

#check whether set2 is subset of set1 or no ?
print(set2.issubset(set1))

#check whether both have common elements are no ?

set5=set1.intersection(set2)
print(set5)


#remove 8 from set 1 and set 2 ==> find the inferences
set1.remove(8)
print(set1)

#discard 0 from set1 and set2
set1.discard(0)
print(set1)

set2.discard(0)
print(set2)

#find collection of both sets ===> set1 and set2

set6=set1.union(set2)
print(set6)
