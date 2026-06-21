"""
Calculate how many numbers are divisible by both 6 & 7 from 1 to 200 using for loop
"""
count = 0
for i in range(1,201,+1):
    if i%6==0 and i%7==0:
        count = count+1
print(count)