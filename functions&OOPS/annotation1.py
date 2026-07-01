from typing import *

def sum_of_list(x:List[int]) -> None:
    sum = 0
    for i in x: 
        sum = sum + i
    return sum

store = sum_of_list([10,20,30,40,50])
print(store)