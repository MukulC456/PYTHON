"""
Ask start and end number from user and print all numbers from start to end using for loop
"""
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start,end+1,+1):
    print(i,end = " ")