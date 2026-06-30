'''
Ask 2 numbers from user. Calculate their total. Print if the sum is odd or even.
Use 2 functions add() and check()
'''
def add(num1,num2):
    total = num1 + num2
    return total

def check(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

# take inputs in x and y so that value of x will be passed to num1 and y to num2.
# here we can take diff variables. don't take same name. num1 and num2 is for everyone who is using this func
x = int(input("Enter number 1: ")) 
y = int(input("Enter number 2: "))
s = add(x,y)  # returned total is stored in s
check(s)

