#Python program to find Cumulative sum of a list

Li=[10,20,30,40,50]
print("Original list :", Li)
new_list=[]
j=0
for i in range(0,len(Li)):
    j = j + Li[i]
    new_list.append(j)
     
print("New list :",new_list)

