# Higher Lower Game Project
from random import choice
from art import logo, vs
from game_data import data
# from replit import clear

def pick_person():
  """Picks a random person from the data"""
  return choice(data)

def format_data(person):
  """Formats the data into a printable statement"""
  name = person['name']
  description = person['description']
  country = person['country']
  return f'{name}, a {description}, from {country}'

def checkRep(a, b):
  """Checks for repetition of B"""
  while b == a:
    return pick_person()
  return b

def checkFollowers(a, b):
  """Checks who has more followers."""
  follows_a = a['follower_count']
  follows_b = b['follower_count']
  if follows_a >= follows_b:
    return 'a'
  elif follows_b >= follows_a:
    return 'b'

def checkAnswer(answer, guess, score):
  """Checks if guess is correct"""
  if answer == guess:
    return True
  return False

def game():
  print(logo)
  person_b = pick_person()
  score = 0
  game_continue = True
  
  while game_continue:
    person_a = person_b
    person_b = pick_person()
    person_b = checkRep(person_a, person_b)
    
    print(f"Compare A: {format_data(person_a)}.")
    print(vs)
    print(f"Against B: {format_data(person_b)}.")
 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # clear() #replit only
    print(logo)
    
    answer = checkFollowers(person_a, person_b)

    is_correct = checkAnswer(guess, answer, score)
    
    if is_correct:
      score+=1
      print(f'You got it right! Current score: {score}')
    else:
      game_continue = False
      print(f'Sorry, that\'s wrong. Final score: {score}')
  
game()