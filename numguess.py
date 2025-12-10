import random

secret_number = random.randint(1, 100)
attempts = 5

print("Guess the number between 1 and 100!")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Too Low!")

else:
    print(f"\n❌ Out of attempts! The correct number was {secret_number}.")