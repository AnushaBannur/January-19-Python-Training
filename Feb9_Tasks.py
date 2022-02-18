##Dict (Feb 9)

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dict1)

#Extract "bobtn" from above dictionary
temp_list=dict1[3]
print(temp_list)
print(temp_list[0][0::2])

#Extract "arbeg" from above dictionary
print(temp_list[2][-1:-6:-1])


#print all keys in dictionary and convert it into tuple
print(tuple(dict1.keys()))

#Find the average of all numbers available under key "2"

temp_key_2=dict1[2]
Sum=sum(temp_key_2)
Len=len(temp_key_2)
Avg=Sum/Len
print("Average=", Avg)
