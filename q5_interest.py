#Write a Python program to calculate the simple interest with user input for principal amount,
#rate, and time.

principal_amount = float(input("enter the amount"));
rate = float(input("enter the rate"));
time = float(input("enter the time"));
intrest = (principal_amount * rate * time)/100;
print(f"Principal intrest is {intrest}")
