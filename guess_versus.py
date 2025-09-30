import random

def versus():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    random_number = random.randint(min_value, max_value)
    print(f"A number has been chosen between {min_value} and {max_value}. Try to guess it before the computer!")

    human_attempts = 0
    human_prev_diff = None

    computer_attempts = 0
    low, high = min_value, max_value

    turn = random.choice(['human', 'computer'])

    while True:
        if turn == "human":
            guess = int(input(f'Your turn! Guess a number between {min_value} and {max_value}: '))
            human_attempts += 1
            diff = abs(random_number - guess)

            if guess == random_number:
                print(f'Yay, congrats! You have guessed the number {random_number} correctly in {human_attempts} tries!')
                break

            if human_prev_diff is None:
                if diff > 0:
                    print('Cold')
            else:
                if diff < human_prev_diff:
                    print('Warmer')
                elif diff > human_prev_diff:
                    print('Colder')
                else:
                    print('Same')

            human_prev_diff = diff
            turn = "computer"
        else:
            guess = random.randint(low, high)
            computer_attempts += 1
            print(f"Computer's turn! It guesses {guess}.")

            if guess == random_number:
                print(f'The computer guessed your number {random_number} correctly in {computer_attempts} tries!')
                break

            if guess < random_number:
                low = guess + 1
                print("Too low!")
            else:
                high = guess - 1
                print("Too high!")

            turn = "human"

versus()