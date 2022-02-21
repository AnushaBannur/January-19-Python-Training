#Python program to print all even numbers in a range


def even_numbers_in_range(Li):

    for i in range(start, end):

        if (Li[i] % 2 == 0):
            print(Li[i],"Num is even")


Li=[11, 2, 3, 14, 91, 24, 61, 100]
start = int(input("Enter start val:"))
end = int(input("Enter end val:"))
print(even_numbers_in_range(Li))
