#Write a Python program that takes user input for their name and greets the user.
 #Then, prompt the user to enter two values.
 #After receiving the values, swap them and print both the ordiginal values and the swapped values.

name = input("Enter the username")
print(f"good morning {name}")
a = input();
b = input();
print(f"the values before swapping {a,b}")
a,b = b,a;
print(f"the values after swapping{a,b}")
