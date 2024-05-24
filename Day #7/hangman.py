# Replit link --> https://replit.com/@Maester/Day-7-Hangman-5-Start#main.py

from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list 
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"
    
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in display:
        print("This letter has already been used.\n")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:

        if guess not in display:
            print(f'{guess} is not in the word! You lost a life.\n')
            
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    
    print(stages[lives])