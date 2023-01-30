def sum_list():

    size = int(input("Enter size of list :"))

    lst=[]
    for i in range(size):
        elements=int(input("Enter elements into list :"))
        lst.append(elements)

    print("The list elements are:",lst)

    sum = 0
    for i in lst:
        sum += i
    return sum

sum_of_list = sum_list()

print("The sum of elements in the list is :",sum_of_list)