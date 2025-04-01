random_number = random.randint(1, 100)
guess = -1
while guess != random_number:
    guess = int(input("Guess the number (1-100): "))
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
print("Correct! The number was", random_number)