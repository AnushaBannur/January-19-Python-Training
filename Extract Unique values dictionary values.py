#Extract Unique values dictionary values


# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
  
# printing original dictionary
print("The original dictionary is : ",test_dict)
  
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()

for i in test_dict:
    res = test_dict.values()
  
# printing result 
print("The unique values list is : " + str(res)) 
