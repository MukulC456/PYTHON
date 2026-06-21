"""
Ask a number form user input. Print from that number to 1 by a difference of 3 using for loop
"""
num = int(input("Enter a number: "))

for i in range(num,0,-3):
    print(i,end = " ")