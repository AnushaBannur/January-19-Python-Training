#Program to accept the strings which contains ALL vowels


def check(string):
	string = string.replace(' ', '')
	print(string)
	string = string.lower()
	print(string)
	vowel = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')]

	# If 0 is present in vowel count array
	if vowel.count(0) > 0:
		return('not accepted')
	else:
		return('accepted')


# Main code
string = input("Enter a string : ")

print(check(string))
