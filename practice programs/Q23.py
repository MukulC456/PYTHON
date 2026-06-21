"""
Ask a number form user input. Print from 1 to that number using for loop
"""
num = int(input("Enter a number: "))

for i in range(1,num+1,+1):
    print(i,end = " ")