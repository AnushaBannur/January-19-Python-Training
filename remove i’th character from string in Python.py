#remove i’th character from string in Python

test_str = "ElectronicsCommunication"
  
# Printing original string 
print ("The original string is : ", test_str)
  
# Removing char at pos 3(index 2)
# using slice + concatenation
new_str = test_str[:2] +  test_str[3:]
  
# Printing string after removal  
# removes ele. at 3rd index
print ("The string after removal of i'th character : ", new_str)
