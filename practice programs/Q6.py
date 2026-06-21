"""
Take salary as input from user and update the salary of employee.
salary less than 10000 5% increment
salary between 10000 and 20000 10% increment
salary between 20000 and 50000 15% increment
salary above 50000 20% increment
"""

salary = float(input("Enter your salary: "))

if salary <= 10000 :
    updated_salary = salary + (5/100)*salary
    print(f"Salary after increment is {updated_salary} ")

elif 10000 < salary < 20000:
    updated_salary = salary + (10/100)*salary
    print(f"Salary after increment iss {updated_salary}")

elif 20000 <= salary < 50000:
    updated_salary = salary + (15/100)*salary
    print(f"Salary after increment is {updated_salary}")

else:
    updated_salary = salary + (20/100)*salary
    print(f"Salary after increment is {updated_salary}")
