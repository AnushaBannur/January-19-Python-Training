#Collect radius and height from user,
#calculate Area of cone (area of cone = 0.33 * pi * r * r * h) output shold be in int format

pi=3.14
radius=float(input("Enter radius of a cone:"))
height=float(input("Enter height of a cone:"))
Area=0.33*pi*(radius**2)*height
print("Area of the cone is",Area)
print("Area of the cone with radius {} and height {} is {}".format(radius,height,Area))
print("Area of the cone with height {1} and radius {0} is {2}".format(radius,height,Area))
print("Area of the cone with height {} and radius {} is {}".format(height,radius,Area)) 
print(f"Area of the cone is {Area}")
