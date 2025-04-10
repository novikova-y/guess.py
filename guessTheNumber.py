import random

def play_game():
    print('Hello. What is your name?')
    name = input()

    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    secretNumber = random.randint(1, 20)

    for guessesTaken in range(1, 7):
        print('Take a guess.')

        try:
            guess = int(input())
        except ValueError:
            print("That's not a number. Try again.")
            continue

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
            break
    else:
        print(f'Nope. The number I was thinking of was {secretNumber}.')

    print(f'You took {guessesTaken} guesses.')

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ('yes', 'y'):
        print("Thanks for playing! Goodbye.")
        break
