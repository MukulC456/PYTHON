"""
Write a python program to find area and perimeter of rectangle by taking length and breadth 
from user as inputs.
"""
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length*breadth
perimeter = 2*(length+breadth)

print(f"Area of rectangle is {area}")
print(f"Perimeter of rectangle is {perimeter}")