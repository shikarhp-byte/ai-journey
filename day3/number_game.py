import random
number = random.randint(1,10)
print("Welcome to the number guessing game")
while True:
    guess = int(input("Enter your guess (1-10): "))
    if guess == number:
        print("Correct! You win!")
        break
    elif guess < number:
        print("Too low! Try Again ")
    else:
        print("Too High! Try Again")