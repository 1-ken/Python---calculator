import random
#function to get the game going
def guess_the_number():
    secret_number = random.randint(1, 10)
    while True:
        guess = int(input("guess the number between 1 - 10:"))
        if guess_the_number == secret_number:
            print("cograts you just won")
        else:
            print("please try again")

guess_the_number()