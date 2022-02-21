#Python program to print negative numbers in a list


def negative_numbers(Li):

    for i in Li:

        if i < 0:
            print(i,"Num is negative")


Li=[11, 2, -3, 15, -91, 23, -6, 100]
print(negative_numbers(Li))
