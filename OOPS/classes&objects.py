class Student: # Class name starts with uppercase letter
    name = "" # attribute 1
    id = 0    # attribute 2
    age = 0   # attribute 3
    gender = "" # attribute 4
    address = "" # attribute 5

s1 = Student()  # s1 and s2 are objects for class 'Student'
s2 = Student()

s1.name = "Mukul"  
s2.name = "Khush"
s1.age = 22
s1.gender = "Male"
print(s1.name)
print(s2.name)
print(s1.age)
print(s1.gender)