# Python3 code to demonstrate working of 
# Convert Nested Tuple to Custom Key Dictionary

  
# initializing tuple
tup1 = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
  
# printing original tuple
print("tuple : ", tup1)
  
# Convert Nested Tuple to Custom Key Dictionary
for i in tup1:
    res = [{'key': i[0], 'value': i[1], 'id': i[2]}]
  
    # printing result 
    print("The converted dictionary : ",res)
