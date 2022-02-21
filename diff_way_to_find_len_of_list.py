#Python | Ways to find length of list

from operator import length_hint

Li = [5,1,8,2,4,3,9,5,9,7,2,8,5,0,3]

#using inbuilt method len()

print(len(Li))

#using for loop with membership operator 'in'
count = 0
for i in Li:
    count=count+1
print(count)


#using inbuilt method length_hint()

print(length_hint(Li))




