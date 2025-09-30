import random

def computer_guess():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    print(f"Think of a number between {min_value} and {max_value}. I will try to guess it!")
    input("Press Enter when you're ready...")

    attempts = 0
    low = min_value
    high = max_value
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since low == high

        attempts += 1
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Yay! I guessed your number {guess} correctly in {attempts} tries!')
        else:
            print("Please enter H, L, or C.")

computer_guess()