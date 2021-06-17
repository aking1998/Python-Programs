"""
Convert Weight from lbs to kg
"""



lbs = float(input("Enter Weight in Pounds(lbs) : "))
kgs = lbs * 0.45
message = f'{lbs} pounds weight {kgs} in kilograms'  #Formatted String used to dynamically insert values
print(message)



"""
Using Lambda Function:

kgs = lambda lbs : lbs * 0.45
print(kgs(50))

"""