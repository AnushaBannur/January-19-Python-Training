#Python program to print all odd numbers in a range


def odd_numbers_in_range(Li):

    for i in range(start, end):

        if (Li[i] % 2 != 0):
            print(Li[i],"Num is odd")


Li=[11, 2, 3, 14, 91, 24, 61, 100]
start = int(input("Enter start val:"))
end = int(input("Enter end val:"))
print(odd_numbers_in_range(Li))
