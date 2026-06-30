'''
from datetime import datetime

# print the current time
def print_time():
    print("TASK COMPLETED")
    print(datetime.now())
    print()

first_name = "Mukul"
print_time()

for i in range(0,10):
    print(i)
print_time()
'''
'''
def get_initial(name):  # function named get_initial taking parameter named name inside it
    initial = name[0:1]
    return initial      # return values

first_name = input("Enter your first name: ").upper()
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ").upper()
last_name_initial = get_initial(last_name)

print(f"Your first initial is {first_name_initial} and last initial is {last_name_initial}" )
'''

'''
1. Fucntions do make your code more readable and easier to maintain
2. Always add comment to explain the purpose of function
3. Functions must be DECLARED before the line of code where the fucntion is called
'''

# Parameterized functions
'''
Named notation is the best practice for parameterized functions. We can assign the values to parameter by name
when we caall the function
'''
'''
# passing parameters name and force_uppercase to function get_initial
def get_initial(name, force_uppercase):
    if force_uppercase:                   # true then if will execute
        initial = name[0:1].upper()
    else:                                 # false then elsse will execute
        initial = name[0:1]
    return initial                        # return value

first_name = input("Enter you first name: ")
first_name_initial = get_initial(name=first_name,force_uppercase=True)

print(f"Your first name initial is {first_name_initial}")
'''