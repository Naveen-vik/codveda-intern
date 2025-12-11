import random

gen_rand_num = random.randint(1, 100)
attempts = 5

print("Guess the number between 1 and 100!")
print("-"*50)

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if guess == gen_rand_num:
        print("Nice! you guess the correct number!")
        break
    elif guess > gen_rand_num:
        print("Too High!")
    else:
        print("Too Low!")

else:
    print(f"\n Out of attempts! The correct number was {gen_rand_num}.")