#Python program to print all negative numbers in a range


def negative_numbers_in_range(Li):

    for i in range(start, end):

        if Li[i] < 0:
            print(Li[i],"Num is negative")


Li=[11, 2, -3, 15, -91, 23, -6, 100]
start = int(input("Enter start val:"))
end = int(input("Enter end val:"))
print(negative_numbers_in_range(Li))
