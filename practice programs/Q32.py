'''
Given a list [1,2,3,4,5]. Print the sum of elements of this list.
'''
def addition_list(x): # x is single element of list
    total = 0
    for i in x:
        total = total + i
    print(total)

my_list = [1,2,3,4,5]
addition_list(my_list)