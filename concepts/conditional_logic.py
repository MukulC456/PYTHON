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