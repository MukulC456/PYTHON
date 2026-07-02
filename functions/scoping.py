def addition():
    num1 = int(input("Enter first number: "))  # num1 and num2 are defined only for this function
    num2 = int(input("Enter second number: "))
    print(f"Answer is {num1+num2}")

def subtraction():
    num1 = int(input("Enter first number: ")) # num1 and num2 are defined only for this function
    num2 = int(input("Enter second number: ")) # num1 and num2 of this func is different from previous func.
    print(f"Answer is {num1-num2}")

addition()
subtraction()
#print(num1+num2)  # num1+num2 is not defined for global
#print(num1)       # num 1 is not defined for global