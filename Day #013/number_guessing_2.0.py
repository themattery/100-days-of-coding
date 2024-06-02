from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, lives):
  """Checks answer and returns lives remaining."""
  if guess > answer:
    print("Too high.")
    return lives - 1
  elif guess < answer:
    print("Too low.")
    return lives - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  """Set number of lives according to the chosen difficulty."""
  difficulty = input("Choose a difficulty -> 'easy' or 'hard': \n")
  if difficulty == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def game():
  """Begins the number guessing game."""
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  number = randint(1, 100)
    
  lives = set_difficulty()
  
  guess = 0
  while guess != number:
    print(f"You have {lives} attempts remaining to guess the number")

    guess = int(input("Make a guess: "))
    lives = check_answer(guess, number, lives)
    if lives == 0:
      print("You've run out of guesses! You lose!")
      return
  
game()