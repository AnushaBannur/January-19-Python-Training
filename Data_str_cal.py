#Project1: Data Structure calculator

def List_opt():
    print("=======Welcome to LIST Data structure========= ")
    print("Please select any one LIST method,")
    print("1.append ")
    print("2.pop ")
    print("3.concatenate ")
    print("4.sum ")
    print("5.len ")
    print("6.min ")
    print("7.max ")
    print("8.insert ")
    print("9.extend ")
    print("10.index ")
    print("11.copy ")
    print("12.count ")
    print("13.reverse ")
    print("14.remove ")
    print("15.clear ")
        

    Li = []
    Li1 = []
    Li2 = []

    while True:
        select = input("Enter select(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")

        if select in ('1', '2', '3', '4','5','6', '7', '8', '9','10','11', '12', '13', '14','15'):

            print(select)

            n = int(input("Enter num of elements in Li:")  )
            
            for i in range (0,n):
                Li_elements = int(input("Enter the Li elements:"))
   #     Li_elements = [input(), int(input("Enter the Li elements:")) ]       
                Li.append(Li_elements)            
            print("List : ", Li)

            if select == '1':
                print("1.append : ")
                Li.append(int(input("enter the element you want to append : ")))
                print("List is appended with new element : ", Li)

            elif select == '2':
                print("2.pop : ")
                Li.pop(int(input("enter the place of the element you want to pop : ")))
                print("List is poped with one element : ", Li)

            elif select == '3':
                for i in range (0,n):
                    Li1_elements = int(input("Enter the Li1 elements:"))
                    Li1.append(Li1_elements)    
                print("List_1 elements  : ", Li1)
                print("3.concatenate : ")
                print("Concatenated list (Li + Li1) : ",(Li + Li1))

            elif select == '4':
                print("4.sum : ")
                print("Sum of Li elements : ", sum(Li))

            elif select == '5':
                print("5.len : ")
                print("Length of Li elements : ", len(Li))

            elif select == '6':
                print("6.min : ")
                print("Minimum of Li elements : ", min(Li))

            elif select == '7':
                print("7.max : ")
                print("Maximum of Li elements : ", max(Li))

            elif select == '8':
                print("8.insert : ")
                print("insert element in Li : ")
                Li.insert(int(input("enter the position of the element to be inserted in a Li : ")), int(input("enter the element to be inserted in a Li : ")))
                print("Print updated Li",Li)

            elif select == '9':
                for i in range (0,n):
                    Li2_elements = int(input("Enter the Li2 elements:"))
                    Li2.append(Li2_elements)    
                print("List_2 elements  : ", Li2)
                print("9.extend : ")
                print("extend Li with Li2 : ")
                Li.extend(Li2)
                print("Li extended with Li2 : ",Li)

            elif select == '10':
                print("10.index : ")
                print("index of an element in Li is: ", Li.index(int(input("enter the element in Li: "))))

            elif select == '11':
                print("11.copy : ")
                Li_copy = Li.copy()
                print("copy of Li is created Li_copy : ", Li_copy)

            elif select == '12':
                print("12.count : ")                
                print("count element occurence : ", Li.count(int(input("enter the element whose occurence has to be counted in Li: "))))

            elif select == '13':
                print("13.reverse : ")                
                Li.reverse()
                print("reversed list : ", Li)

            elif select == '14':
                print("14.remove : ")                
                Li.remove(int(input("enter the element to be removed from Li: ")))
                print("updated list : ", Li)

            elif select == '15':
                print("15.clear : ")                
                print("clear the list : ", Li.clear())
            break

        else:
            print("Invalid input")                    



def Tuple_opt():

    print("=======Welcome to TUPLE Data structure========= ")
    print("Please select any one TUPLE method,")
    print("1.index ")
    print("2.count ")
    print("3.concatenation ")
    print("4.sum ")
    print("5.len ")
    print("6.min ")
    print("7.max ")


    Li = []
    Li1 = []
    tup = []
    tup1 = []

    while True:
        select = input("Enter select(1/2/3/4/5/6/7): ")

        print(select)

        n = int(input("Enter num of elements in Li:")  )

        for i in range (0,n):
            Li_elements = int(input("Enter the Li elements:"))
            Li.append(Li_elements)
            tup = tuple(Li)            
        print("Tuple : ", tup)        

        if select in ('1', '2', '3', '4', '5', '6', '7'):

            if select == '1':
                print("1.index : ")
                tup_index = tup.index(int(input("enter the element in tup:")))
                print("index of an element in tup is: ", tup_index)

            elif select == '2':
                print("2.count : ")                
                print("count element occurence : ", tup.count(int(input("enter the element whose occurence has to be counted in tup:"))))         


            elif select == '3':
                for i in range (0,n):
                    Li1_elements = int(input("Enter the Li1 elements:"))
                    Li1.append(Li1_elements)
                tup1 = tuple(Li1)
                print("tup_1 elements  : ", tup1)
                print("3.concatenate : ")
                tup2 = tup + tup1
                print("Concatenated tuple (tup + tup1) : ",tup2)

            elif select == '4':
                print("4.sum : ")
                print("Sum of tup elements : ", sum(tup))

            elif select == '5':
                print("5.len : ")
                print("Length of tup elements : ", len(tup))

            elif select == '6':
                print("6.min : ")
                print("Minimum of tup elements : ", min(tup))

            elif select == '7':
                print("7.max : ")
                print("Maximum of tup elements : ", max(tup))
            break

        else:
            print("Invalid input")


def set_opt():
    print("=======Welcome to SET Data structure========= ")
    print("Please select any one SET method,")
    print("1.add ")
    print("2.copy ")
    print("3.difference ")
    print("4.difference_update ")
    print("5.union ")
    print("6.intersection ")
    print("7.intersection_update ")
    print("8.symmetric_difference ")
    print("9.symmetric_difference_update ")
    print("10.isdisjoint ")
    print("11.issubset ")
    print("12.issuperset ")
    print("13.sum ")
    print("14.len ")
    print("15.min ")
    print("16.max ")


    while True:
        select = input("Enter select(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")


        if select in ('1', '2', '3', '4','5','6', '7', '8', '9','10','11', '12', '13', '14','15'):

            print(select)

            n = int(input("Enter num of elements in set1:")  )
            set1 = set()
            set2 = set()
            set3 = set()
                
            for i in range (0,n):
                set1_elements = int(input("Enter the set1 elements:"))
                set1.add(set1_elements)        
            print("set1 is : ", set1)

            if select == '1':
                print("adds an element to the set : ", set1.add(int(input("enter the element into set : "))))
                print("set1 is : ", set1)
                print("====ADD operation is completed====")

            elif select == '2':
                set_copy = set1.copy()
                print("copy of set1 is created in set_copy : ", set_copy)
                print("====COPY operation is completed====")                

            elif select == '3':
                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                 
                set_difference = set1.difference(set2)
                print("difference of set1 and set2 : ", set_difference)
                print("====DIFFERENCE operation is completed====")                

            elif select == '4':
         
                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                set1.difference_update(set2)              
                print("difference of set1 and set2 updated in set1 : ", set1)
                print("====DIFFERENCE_UPDATE operation is completed====")

            elif select == '5':

                n1 = int(input("Enter num of elements in set2:"))
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                 
                set_union = set1.union(set2)
                print("union of set1 and set2 : ", set_union)
                print("====UNION operation is completed====")                

            elif select == '6':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                 
                set_intersection = set1.intersection(set2)
                print("intersection of set1 and set2 : ", set_intersection)
                print("====INTERSECTION operation is completed====")                

            elif select == '7':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                set1.intersection_update(set2)
                print("intersection of set1 and set2 updated in set1 : ", set1)
                print("====INTERSECTION_UPDATE operation is completed====")                 

            elif select == '8':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                 
                set_symmetric_difference = set1.symmetric_difference(set2)
                print("symmetric_difference of set1 and set2 : ", set_symmetric_difference)
                print("====SYMMETRIC_DIFFERENCE operation is completed====")                

            elif select == '9':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                set1.symmetric_difference_update(set2)
                print("symmetric_difference of set1 and set2 updated in set1 : ", set1)
                print("====SYMMETRIC_DIFFERENCE_UPDATE operation is completed====")                 

            elif select == '10':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                
                print("If common elements NOT present in set1 and set2 'isdisjoint' returns TRUE else returns FALSE====== ", set1.isdisjoint(set2))
                print("====ISDISJOINT operation is completed====")                 

            elif select == '11':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                
                print("If all the elements set2 are present in set1 'issubset' returns TRUE else returns FALSE====== ", set1.issubset(set2))
                print("====ISSUBSET operation is completed====")                

            elif select == '12':

                n1 = int(input("Enter num of elements in set2:")  )
                for i in range (0,n1):
                    set2_elements = int(input("Enter the set2 elements:"))
                    set2.add(set2_elements)
                print("set2 is",set2)
                
                print("If set1 contains all the elements of set2 'issuperset' returns TRUE else returns FALSE====== ", set1.issuperset(set2))
                print("====ISSUPERSET operation is completed====")                

            elif select == '13':
                
                print("Sum of set elements : ", sum(set1))
                print("====SUM operation is completed====")                 

            elif select == '14':
                
                print("Length of set elements : ", len(set1))
                print("====LEN operation is completed====")                

            elif select == '15':
                
                print("Minimum of set elements : ", min(set1))
                print("====MIN operation is completed====")                

            elif select == '16':
                
                print("Maximum of set elements : ", max(set1))
                print("====MAX operation is completed====")                
                break                            

        else:
            print("Invalid input")




def dict_opt():
    print("=======Welcome to DICTIONARY Data structure========= ")
    print("Please select any one DICTIONARY method,")
    print("1.copy ")
    print("2.keys ")
    print("3.values ")
    print("4.items ")
    print("5.pop ")
    print("6.popitem ")
    print("7.update ")
    print("8.setdefault ")
    print("9.get ")
    print("10.fromkeys ")



    while True:
        select = input("Enter select(1/2/3/4/5/6/7/8/9/10): ")


        if select in ('1', '2', '3', '4','5','6', '7', '8', '9','10'):

            print(select)

            Li1 = []
            Li2 = []
            Li3 = []

            n1 = int(input("Enter num of elements in Li1:")  )            
                
            for i in range (0,n1):
                Li1_elements = int(input("Enter the Li1 elements:"))
                Li1.append(Li1_elements)        
            print("Li1 is : ", Li1)

            n2 = int(input("Enter num of elements in Li2:")  )            
                
            for i in range (0,n2):
                Li2_elements = input("Enter the Li2 elements:")
                Li2.append(Li2_elements)        
            print("Li2 is : ", Li2)
            dict1 = dict(zip(Li1, Li2))
            print("The dictionary dict1 is  :   ", dict1)

            if select == '1':
                dict_copy = dict1.copy()
                print("copy of dict1 is created in dict_copy : ", dict_copy)
                print("====COPY operation is completed====")             

            elif select == '2':
                print("Returns a list containing the dictionary's keys : ", dict1.keys())
                print("====KEYS operation is completed====")

            elif select == '3':
                print("Returns a list of all the values in the dictionary : ", dict1.values())
                print("====VALUES operation is completed====")

            elif select == '4':
                print("Returns a list containing a tuple for each key value pair : ", dict1.items())
                print("====ITEMS operation is completed====")

            elif select == '5':
                print("Removes the element with the specified key : ", dict1.pop(int(input("Enter the key value from the dict1 : "))))
                print("dict1 after POP operation is : ", dict1)
                print("====POP operation is completed====")

            elif select == '6':
                print("Removes the last inserted key-value pair : ", dict1.popitem())
                print("dict1 after POPITEM operation is : ", dict1)
                print("====POPITEM operation is completed====")

            elif select == '7':
                dict1.update({'3': 'Anusha'})
                print("Updates the dictionary with the specified key-value pairs : ", dict1)
                print("dict1 after UPDATE operation is : ", dict1)
                print("====UPDATE operation is completed====")

            elif select == '8':
                setdefault_dict = dict1.setdefault(int(input("Enter the key of dict1 : ")), 'Anusha')
                print("Returns the value of the specified key. If the key does not exist: insert the key, with the specified value : ", setdefault_dict)
                print("dict1 after setdefault operation is : ", dict1)
                print("====SETDEFAULT operation is completed====")

            elif select == '9':
                get_dict = dict1.get(int(input("Enter the key of dict1 : ")))
                print("Returns the value of the specified key : ", get_dict)
                print("====GET operation is completed====")

            elif select == '10':
                n3 = int(input("Enter num of elements(keys) in Li:")  )            
                Li = []
                for i in range (0,n3):
                    Li_key_elements = int(input("Enter the Li key_elements:"))
                    Li.append(Li_key_elements)        
                print("Li is : ", Li)
                
                fromkeys_dict = dict.fromkeys(Li)
                print("Returns a dictionary with the specified keys and the specified value : ", fromkeys_dict)
                print("====FROMKEYS operation is completed====")                 
                break            
                                

        else:
            print("Invalid input")              



#main program
print("Welcome to Data structure calculator")
print("Please select any one Data structure,")
print("1.List ")
print("2.Tuple ")
print("3.Set ")
print("4.Dictionary ")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
           

        if choice == '1':
            print("List operations", List_opt())

        if choice == '2':
            print("Tuple operations", Tuple_opt())

        elif choice == '3':
            print("Set operations", set_opt())

        elif choice == '4':
            print("Dictionary operations", dict_opt())
        break
    else:
        print("Invalid Input")
