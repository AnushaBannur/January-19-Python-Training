#Python program to print even numbers in a list


def even_numbers(Li):

    for i in Li:

        if i % 2 == 0:
            print(i,"Num is even")

Li=[11, 2, 3, 15, 91, 23, 66, 100]
print(even_numbers(Li))
