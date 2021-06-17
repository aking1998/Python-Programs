"""
Check if given name is between 3 to 50 characters,Display appropriate messages for every case.
"""

name = input("Enter your name : ")
count = len(name)                          # len() function is used.

if count<=3 or count>=50:                  # Logical Operator
    print("Incorrect name length !!")
else:
    print("Your Name looks good!!")