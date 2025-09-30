import random

def guess():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    random_number = random.randint(min_value, max_value)
    attempts = 0    
    prev_diff = None
    guess = None

    print(f"A number has been chosen between {min_value} and {max_value}. Try to guess it!")

    while guess != random_number:
        guess = int(input(f'Guess a number between {min_value} and {max_value}: '))
        attempts += 1
        diff = abs(random_number - guess)

        if guess == random_number:
            print(f'Yay, congrats. You have guessed the number {random_number} correctly in {attempts} try!')
            break
        
        if prev_diff is None:
            if diff > 0:
                print('Cold')
        else:
            if diff < prev_diff:
                print('Warmer')
            elif diff > prev_diff:
                print('Colder')
            else:
                print('Same')
        
        prev_diff = diff

guess()