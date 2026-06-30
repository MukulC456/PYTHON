'''
We have operators like: greater than(>), less than(<), greater than equal to(>=), less than equal to(<=),
                        equal to(==), not equal to(!=)
'''
'''
# if else example
price = input("How much did you pay? ")
price = float(price)

if price >= 1.00:
    tax = 0.07
else:
    tax = 0
print(f"Tax rate is {tax}")
'''
'''
# if elif else example
state = input("What state do you live in?: ")
state = state.capitalize()
tax = 0

if state == "Gujarat":
    tax = 7
elif state == "Maharashtra":
    tax = 7
elif state == "Rajasthan":
    tax = 5
else:
    tax = 8
print(f"Tax is {tax}%")
'''
'''
# using or 
state = input("What state do you live in?: ")
state = state.capitalize()
tax = 0

if state == "Gujarat" or state == "Maharashtra":
    tax = 7
elif state == "Rajasthan":
    tax = 5
else:
    tax = 8
print(f"Tax is {tax}%")
'''
'''
# using in 
state = input("What state do you live in?: ")
state = state.capitalize()
tax = 0

if state in ("Gujarat", "Maharashtra","Punjab"):
    tax = 7
elif state == "Rajasthan":
    tax = 5
else:
    tax = 8
print(f"Tax is {tax}%")
'''
'''
# nested if else
country = input("What country do you live in?: ")
country = country.capitalize()

if country == "India":
    state = input("What state do you live in?: ")
    state = state.capitalize()

    if state in ("Gujarat","Maharashtra","Punjab"):
        tax = 7
    elif state == "Rajasthan":
        tax = 5
    else:
        tax = 8
    
    print(f"Tax is {tax}%")

else:
    tax = 0
    print(f"Tax is {tax}%")
'''

# using boolean to make normal code efficient
'''
A student makes honour roll if their GPA is >= 8.5 and their lowest grade is not below 7.5
'''

'''
# normal code
gpa = float(input("Enter you GPA: "))
lowest_grade = float(input("Enter your lowest grade: "))

if gpa >= 8.5 and lowest_grade >= 7.5:
    print("You made the honour roll")
'''
'''
# using boolean for normal code
gpa = float(input("Enter you GPA: "))
lowest_grade = float(input("Enter your lowest grade: "))

if gpa >= 8.5 and lowest_grade >= 7.5:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:                  # We can use this to prevent writing the above if logic again and again
    print("You made honour_roll") # We can recall the condition using boolean and print the output.
'''
