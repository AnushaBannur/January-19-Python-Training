#second largest number in a list

# list of numbers
Li1 = [1, 75, 4, 25, 35]
print(Li1)

# using sorting method
Li1.sort()

# printing the second last element
print("Second largest element is:", Li1[-2])



# Python program to find second largest
# number in a list

# list of numbers
Li2 = [15, 75, 41, 25, 35]
print(Li2)
# temp_list is a set of Li2
temp_list = set(Li2)

# removing the largest element from temp list
temp_list.remove(max(Li2))

#Now print the largest element which will be the second largest element as the largest element is already removed in the previous step
print("Second largest element is:", max(temp_list))

