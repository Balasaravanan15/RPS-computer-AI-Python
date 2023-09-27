import random

print('rock')
print('paper')
print('scissors')

player = input("Enter Player's Choice: ").lower()

rand_num = random.randint(0, 2)

if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print('computer plays '+ str(computer))

if player == computer:
    print('It is a tie!')

elif player == 'rock':
    if computer == 'scissors':
        print('player wins!')
    if computer == 'paper':
        print('computer wins!')

elif player == 'paper':
    if computer == 'rock':
        print('player wins!')
    if computer == 'scissors':
        print('computer wins!')
        
elif player == 'scissors':
    if computer == 'rock':
        print('computer wins!')
    if computer == 'paper':
        print('player wins!')
        
else:
    print('something went wrong')
