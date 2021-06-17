# Guess the number

n=int(input("Enter number to be guessed : "))
num=1

while num<4:
    guess = int(input("Guess : "))
    if guess == n:
        print("Correct guess!!")
    else:
        num = num + 1
else:
    print("Sorry!! You failed..")