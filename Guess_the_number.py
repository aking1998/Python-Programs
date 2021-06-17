# Guess the number

number_to_be_guessed=int(input("Enter number to be guessed : "))
num=1

while num<4:
    guess = int(input("Guess : "))
    if guess == number_to_be_guessed:
        print("Correct guess!!")
        break
    else:
        num = num + 1
else:
    print("Sorry!! You failed..")
