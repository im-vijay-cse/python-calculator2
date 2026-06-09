mport random
secret_number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break
