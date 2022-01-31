#write a program to calculate perimeter of the cricle with radius (float) (collect it through input function), with pi=3.14

#Formula to find perimeter of a circle is = 2*pi*r

radius=float(input("Enter radius:"))
pi=3.14
Perimeter=2*pi*radius
print("Perimeter of a circle is ",Perimeter)
print("Perimeter of a circle with radius {} is {}".format(radius, Perimeter))
print(f"Perimeter of a circle is = {Perimeter}")
