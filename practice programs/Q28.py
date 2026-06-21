"""
Calculate how many numbers are divisible by 7 from 1 to 100 using for loop.
"""
count = 0
for i in range(1,101,+1):
    if i%7==0:
        count = count+1
print(count)