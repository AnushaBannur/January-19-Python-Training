
# Print even length words in a string

def printWords(s):
	
	# split the string
	s = s.split(' ')
	print("Original string is : ",s)
	
	# iterate in words of string
	for word in s:
		
		# if length is even
		if len(word)%2==0:
			print("Even len word is : ", word)


# main Code
s = "I am Anusha"
printWords(s)
