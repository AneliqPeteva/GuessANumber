import random
special_number = random.randint(1, 150)

while True:
    guess = input("Hi! Please, guess the number (1-150):")
    if not guess.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(guess)

    if player_number == special_number:
        print('Congratulations, you guess it! ')
        break
    elif player_number > special_number:
        print('Too High!')
    else:
        print('Too Low!')
