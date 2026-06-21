"""
Write a program to take a number from user and check if last digit is divisible by 5
"""

num = int(input("Enter a number: "))

last_digit = num%10

if last_digit%5 == 0 :
    print("Last digit divisible by 5")

else:
    print("Last digit not divisible by 5")
