import random

CHOICES = ['r', 'p', 's']
    
def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play_round():

    while True:
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()
        if user in CHOICES:
            break
        print("Invalid input. Please try again.")
    computer = random.choice(['r', 'p', 's'])
    print(f'You chose {user}, computer chose {computer}.')

    if user == computer:
        print('round tie!')
        return 0
    if is_win(user, computer):
        print('You won this round!')
        return 1
    
    print('Computer won this round!')
    return -1

def game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("First to 3 wins is the champion!")
    while user_score < 2 and computer_score < 2:
        result = play_round()
        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1
        print(f'Score -> You: {user_score}, Computer: {computer_score}\n')
        
    if user_score == 2:
        print("Congratulations! You are the overall winner!")
    else:
        print("Computer is the overall winner! Better luck next time.")
        
game()