'''
Make a list 0 to n. Take an argument which will be a number
'''
my_list = lambda n: [i for i in range(0,n+1)]

x = int(input("Enter length of list: "))
print(my_list(x))
# print(my_list(12))