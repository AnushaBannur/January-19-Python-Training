#write a program to calculate area of circle with radius (float) (collect using input function)

#Formula for Area of Circle=pi*r*r
#pi=3.14

radius=float(input("Enter the radius of a circle:"))
pi=3.14
Area=pi*(radius**2)
print("Area of a circle is:", Area)
print("Area of a circle with radius {} is {}".format(radius,Area))
print(f"Area of circle is: {Area}")
