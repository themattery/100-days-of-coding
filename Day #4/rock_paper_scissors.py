import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors!")

user_index = int(input("Type 0 for rock, 1 for paper and 2 for scissors!\n "))

option = [rock, paper, scissors]

user_input = option[user_index]

pc_index = random.randint(0, 2)
pc_input = option[pc_index]

print(f'You chose: {user_input}\n')
print(f'The PC chose: {pc_input}\n')

if pc_index == user_index:
    print('It\'s a draw!')
elif pc_index == 0 and user_index == 1:
    print('You win!')
elif pc_index == 1 and user_index == 2:
    print('You win!')
elif pc_index == 0 and user_index == 2:
    print('You lose!')
elif user_index == 0 and pc_index == 1:
    print('You lose!')
elif user_index == 1 and pc_index == 2:
    print('You lose!')
elif user_index == 0 and pc_index == 2:
    print('You win!')
else:
    print('well, i didn\'t plan that')
