# sum of elements of list
def sum_of_list(x): # x is iterable collection passed into the function
    sum = 0
    for i in x: # i is actual value/item from collection for each iteration
        sum = sum + i
    return sum

store = sum_of_list([10,20,30,40,50])
print(store)