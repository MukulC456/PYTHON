"""
Write a program to to calculate bill. Ask the amount from the user. You have to give discount
on the amount and print the final bill after discount.
50000 and above- 30% discount
40000 to 49999- 25% discount
30000 to 39999- 20% discount
10000 to 29999- 10% discount
1 to 9999- no discount
"""
amount = float(input("Enter Amount: "))

if amount >= 50000:
    bill = amount - (30/100)*amount
    print(f"Yay! you got 30% discount") 
    print(f"Your bill after discount is {bill}")

elif 40000 <= amount <= 49999:
    bill = amount - (25/100)*amount
    print(f"Yay! you got 25% discount")
    print(f"Your bill after discount is {bill}")

elif 30000 <= amount <= 39999:
    bill = amount - (20/100)*amount
    print(f"Yay! you got 20% discount")
    print(f"Your bill after discount is {bill}")

elif 10000 <= amount <= 29999:
    bill = amount - (10/100)*amount
    print(f"Yay! you got 10% discount")
    print(f"Your bill after discount is {bill}")

elif 1 <= amount <= 9999:
    bill = amount
    print("Sorry! you missed the discount")
    print(f"Your bill is {bill}")

else:
    print("Thank you for visiting.")
