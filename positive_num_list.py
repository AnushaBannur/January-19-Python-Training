#Python program to print positive numbers in a list


def positive_numbers(Li):

    for i in Li:

        if i > 0:
            print(i,"Num is positive")


Li=[11, 2, -3, 15, -91, 23, -6, 100]
print(positive_numbers(Li))
