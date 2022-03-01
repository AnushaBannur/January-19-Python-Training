#Words Frequency in String Shorthands

# Words Frequency in String Shorthands
# Using Counter() + split()
#Counter is a function inside collections module
from collections import Counter

# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(test_str))

#Using split()
test_str.split()
print("String after spliting : " , test_str.split())

# Using Counter()
res = Counter(test_str.split())

# printing result
print("The words frequency : " + str(dict(res)))
