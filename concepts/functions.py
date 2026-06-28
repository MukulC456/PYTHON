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
def get_initial(name):
    initial = name[0:1]
    return initial

first_name = input("Enter your first name: ").capitalize()
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ").capitalize()
last_name_initial = get_initial(last_name)

print(f"Your first initial is {first_name_initial} and last initial is {last_name_initial}" )
'''

'''
1. Fucntions do make your code more readable and easier to maintain
2. Always add comment to explain the purpose of function
3. Functions must be DECLARED before the line of code where the fucntion is called
'''