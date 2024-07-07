# Number Guessing Game Project
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
difficulty = input("Choose a difficulty -> 'easy' or 'hard': \n")

if difficulty == 'easy':
  lives = 10
else:
  lives = 5

game_on = True

while game_on:
  print(f"You have {lives} attempts remaining to guess the number")
  
  print(f"Answer: {number}")
  
  guess = int(input("Make a guess: "))
  
  if guess > number:
    print("Too high.")
    lives -= 1
  elif guess < number:
    print("Too low.")
    lives -= 1
  else:
    print(f"You got it! The answer was {number}.")
    game_on = False

  if lives == 0:
    print("You've run out of guesses, you lose.")
    game_on = False