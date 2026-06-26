'''
Arrays: Numerical data types, all must be of same type
Lists: Store anything, store any type
'''

'''
# lists
names = ["Mukul","Khush"]
scores = [] # empty list
scores.append(98)  # append() adds items in list
scores.append(99)
print(names)
print(scores)
print(scores[1])  # we can access specific item through it's index
print(names[0])
'''
'''
# common operations on list
names = ["Mukul", "Khush", "Vraj"]
print(len(names)) # total length or size of list
names.insert(2,"Aryan") # inserting item at index 2
print(names)
names.sort() # sorts items in alphabetical order for strings and ascending order for numbers
print(names)
'''
# ranges in list

'''
for example we have: 
list_name = [item1, item2, item3, item4]  put indexes on commas and square brackets.
            0     1      2      3      4
'''
'''
names = ["Mukul","Khush","Aryan","Vraj"]
required = names[1:3]  # start and end index
print(required)
required = names[1:]  # this is same as [1:4]
print(required)
required = names[:3]  # this is same as [0:3]
print(required)
required = names[:]   # this is same as [0:4]
print(required)
'''

