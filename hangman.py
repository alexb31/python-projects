import random
import string
from words import get_words

FREQUENCY_ORDER = "ETAOINSHRDLUCMFYWGPBVKJXQZ"

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word or not word.isalpha():
        word = random.choice(words)
    return word.upper()

def cpu_letter(used_letters):
    remaining_letters = list(set(string.ascii_uppercase) - used_letters)
    remaining_letters.sort(key=lambda letter: FREQUENCY_ORDER.index(letter))
    return remaining_letters[0] if remaining_letters else None

def display_word(word, used_letters):
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word:', ' '.join(word_list))

def player_vs_cpu(human_lives=6, cpu_lives=6):
    words = get_words()
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    turn = random.choice(['HUMAN', 'CPU'])

    print("Hangman: Player vs CPU")
    print(f"The word has {len(word)} letters.")

    while len(word_letters) > 0 and human_lives > 0 and cpu_lives > 0:   # <-- ici
        print("\nUsed letters:", ' '.join(sorted(used_letters)) or "None")
        print(f"Human lives: {human_lives}, CPU lives: {cpu_lives}")
        display_word(word, used_letters)

        if turn == 'HUMAN':
            user_letter = input('Your turn! Guess a letter: ').strip().upper()
            if len(user_letter) != 1 or user_letter not in alphabet:
                print("Invalid input. Please enter a single A-Z letter.")
                continue
            if user_letter in used_letters:
                print("You've already guessed that letter. Try again.")
                continue

            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! {user_letter} is in the word.")
                if len(word_letters) == 0:
                    display_word(word, used_letters)
                    print("You revealed the last letter — YOU WIN!")
                    return
            else:
                human_lives -= 1
                print(f"Sorry, {user_letter} is not in the word. (-1 life)")

            turn = 'CPU'

        else:
            cpu_guess = cpu_letter(used_letters)
            if cpu_guess is None:
                print("CPU has no letters left to guess. It's a draw!")
                break

            print(f"CPU's turn! CPU guesses: {cpu_guess}")
            used_letters.add(cpu_guess)
            if cpu_guess in word_letters:
                word_letters.remove(cpu_guess)        # <-- idem
                print(f"CPU guessed correctly! {cpu_guess} is in the word.")
                if len(word_letters) == 0:
                    display_word(word, used_letters)
                    print(f"CPU revealed the last letter — CPU WINS! (Word: {word})")
                    return
            else:
                cpu_lives -= 1
                print(f"CPU guessed wrong! {cpu_guess} is not in the word. (-1 life)")

            turn = 'HUMAN'

    print(f"\nThe word was: {word}")
    if human_lives == 0 and cpu_lives == 0:
        print("Both players ran out of lives. It's a draw!")
    elif human_lives == 0:
        print("You ran out of lives. CPU WINS!")
    elif cpu_lives == 0:
        print("CPU ran out of lives. YOU WIN!")
    else:
        print("Game over.")

player_vs_cpu()
