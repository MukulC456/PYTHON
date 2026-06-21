"""
Calculate the sum of all numbers that are divisible by 4 from 20 to 50.
"""
sum = 0
for i in range(20,51,+1):
    if i%4==0:
        sum = sum+i
print(sum)