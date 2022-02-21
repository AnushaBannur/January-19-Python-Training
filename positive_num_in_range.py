#Python program to print all positive numbers in a range


def positive_numbers_in_range(Li):

    for i in range(start, end):

        if Li[i] > 0:
            print(Li[i],"Num is positive")


Li=[11, 2, -3, 15, -91, 23, -6, 100]
start = int(input("Enter start val:"))
end = int(input("Enter end val:"))
print(positive_numbers_in_range(Li))
