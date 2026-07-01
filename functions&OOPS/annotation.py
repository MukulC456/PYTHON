def add(x:int, y:int) -> int:
    total = x+y
    return total

def student(name:str, age:int, gpa:float) -> None:
    print(name)
    print(age)
    print(gpa)

store = add(10,20)
print(store)

student("Mukul",22,7.88)
'''
we specified int for x and y. But only to know for what purpose we are 
using x and y. We can still add strings with the above code.
Used arrow in line1 to tell that :
    1. if we use 'return' then mention data type like int,float,str,
    bool,etc.
    2. if not use 'return' then mention 'None'
'''