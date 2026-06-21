"""
Write a python program to find perccentage of a student in class by asking user input
5 subjects marks.
"""
subject1 = float(input("Enter marks of subject 1: "))
subject2 = float(input("Enter marks of subject 2: "))
subject3 = float(input("Enter marks of subject 3: "))
subject4 = float(input("Enter marks of subject 4: "))
subject5 = float(input("Enter marks of subject 5: "))

total_marks = float(input("Enter total marks: "))
marks_obtained = subject1+subject2+subject3+subject4+subject5

percentage = (marks_obtained/total_marks) * 100
print(f"Your percentage is {percentage}%")