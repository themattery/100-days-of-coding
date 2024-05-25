from art import logo
from caesar import caesar

print(logo)

restart = True

while restart:
  direction = input("Type 'encode' to encrypt, type   'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart_option = input("Would you like to restart? Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
  
  if restart_option == 'no':
    restart = False
    print('Goodbye. 👋')