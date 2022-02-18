#Strip method usage

string1= "***python***"
print(string1.strip("*"))  #if * is not mentioned then by default it stips the empty space

string2= "**python********"
print(string2.rstrip("*"))

string3= "********java*******"
print(string3.lstrip("*"))

string4= "***  *****java*******"
print(string4.lstrip("*"))  #it removes the * till the space on the left side of the string as lstrip is 
                            #used otherwise it removes white space from either side if just strip is used.


string5= "           java"
print(string5.strip()) #if no parameter is passed inside the strip func then by default it removes the white space



 
