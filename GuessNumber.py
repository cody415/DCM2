import random

number_to_guess = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
