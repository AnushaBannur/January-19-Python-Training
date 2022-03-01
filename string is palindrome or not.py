# program to check if a string is palindrome or not
 
def isPalindrome(str):
    return str == str[::-1]
 
 
str = input("Enter a string : ")
res = isPalindrome(str)
 
if res:
    print("Yes, string is Palindrome")
else:
    print("No, string is not Palindrome")
