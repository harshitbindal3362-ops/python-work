# Guess the secret number

secret_number = 7

for attempt in range(3):  # User gets 3 chances
    guess = int(input("Enter a number between 1 and 10: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("Game Over! The secret number was", secret_number)



