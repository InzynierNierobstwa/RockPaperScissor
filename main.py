import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input('Type Rock, Paper, Scissor or Quit if you would like to stop: ')
    if user_input.lower() == 'quit':
        break

    if user_input.lower() not in options:
        print('sth wrong, repeat')
        continue

    random_number = random.randint(0, 2)# 0: rock; 1: paper; 2: scissor
    computer_pick = options[random_number]
    print(computer_pick)

    if user_input == 'rock' and computer_pick == 'scissor':
        user_wins += 1
        print('You won!')
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print('You won!')
    elif user_input == 'scissor' and computer_pick == 'paper':
        user_wins += 1
        print('You won!')
    elif (user_input == 'rock' and computer_pick == 'rock') or (user_input == 'paper' and computer_pick == 'paper') or (user_input == 'scissor' and computer_pick == 'scissor'):
        print('Draw! No one win!')
    else:
        computer_wins += 1
        print('Computer win!')

print(f'You won {user_wins} times')
print(f'Computer won {computer_wins} times')
print('Bye!')