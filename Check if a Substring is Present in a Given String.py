#Check if a Substring is Present in a Given String

# function to check if small string is 
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO, substring is not found")
    else:
        print("YES, substring is found")
            
#main
string = "geeks for geeks"
sub_str =input("Enter substring : ")
check(string, sub_str)

