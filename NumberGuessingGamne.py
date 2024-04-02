import random
top_number = input("Please enter the top range number: ")
if top_number.isdigit():
    top_number = int(top_number)
    if top_number <= 0:
        print("Please enter the values greater than 0 next try!")
        quit()
else:
    print("Enter a valid number in next try!")
    quit()

random_number = random.randint(1, top_number)
guesses = 0

while True:
    guesses += 1
    guess = input("Enter the guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a valid guess number!")
        continue
    if guess == random_number:
        print("Great! You won the game.")
        break
    elif guess < random_number:
        print("Guess Higher!")
    else:
        print("Guess Lower!")
print("You got in", guesses, "guesses!")




