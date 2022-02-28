#Python – Adding Tuple to List and vice – versa

Li1 = [1,2,3,4,5]

tup1 = (6,7)

#Adding Tuple to List
Li1 += tup1
print(Li1)

#Adding List to Tuple

#converting tup1 to list
Li2 = list(tup1)

res  = Li1+Li2
print(tuple(res))
