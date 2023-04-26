import random

def play_game():
    while True:
        valid_user_choices = ['rock', 'paper', 'scissors']
        user_choice = input("Rock, paper, or scissors? ")
        if user_choice.lower() not in valid_user_choices:
            print("Please choose between rock, paper or scissors")
        else:
            opp_choice = random.choice(['rock', 'paper', 'scissors'])
            print(f"Opponent chose {opp_choice}")
            if opp_choice == user_choice.lower():
                print('Tie!')
            elif opp_choice == 'rock' and user_choice.lower() == 'scissors':
                print('Rock beats scissors, I win!')
                return False
            elif opp_choice == 'scissors' and user_choice.lower() == 'paper':
                print('Scissors beats paper! I win!')
                return False
            elif opp_choice == 'paper' and user_choice.lower() == 'rock':
                print('Paper beats rock, I win!')
                return False
            else:
                print('You win!\n')
                return False

def play_status():
    while True:
        response = input("Would you like to play? ")
        if response.lower() == 'yes':
            play_game()
        elif response.lower() == 'no':
            break
        else:
            print("Please answer 'yes' or 'no'.")

play_status()
