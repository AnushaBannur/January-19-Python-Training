#####LIST

#Create an empty list (two ways)

Li1=[]
print(Li1)

Li1=list()
print(Li1)

#Concatenate with [5,6,7,8]
Li2=[5,6,7,8]
print(Li1+Li2)

#add 8,9,1,5,6,7,8,1 elements to that list
Li3=[8,9,1,5,6,7,8,1]
Li4=Li2+Li3
print(Li4)

#Find frequency of 8 (count)
print(Li4.count(8))

#find the mean of the list
#mean=(sum of elements of the list/num of elements)

sum1=sum(Li4)
num_of_elements=len(Li4)
mean=sum1/num_of_elements
print("Mean:",mean)

##find sum (List) + min + Max
print(Li4)
sum1=sum(Li4)
print("Sum of the list4:",sum1)
print(min(Li4))
print(max(Li4))
print("Sum+min+max = ",sum(Li4)+min(Li4)+max(Li4))


#Find median of the list
#The median is the number in the middle {2, 3, 11, 13, 26, 34, 47}, which in this instance is 13 since there are three numbers on either side.
#To find the median value in a list with an even amount of numbers, one must determine the middle pair, add them, and divide by two.
Li6=[1,2,3,4,5,6]
lenth_of_Li=len(Li6)
print(lenth_of_Li)
Mid_val=lenth_of_Li//2
print(Mid_val)

if(lenth_of_Li%2!=0):
    print(Li6[Mid_val])
else:
    print(Li6[Mid_val-1],Li6[Mid_val])


##remove duplicates from list and give output in the format of tuple

Li7=[1,2,3,1,4,5,4,6,8,5,6,5,1]
print(tuple(set(Li7)))




