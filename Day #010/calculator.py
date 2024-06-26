# Calculator Project
from art import logo

#Add function
def add(a, b):
  return a + b 

#Subtract
def subtract(a, b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input('Type in the first number: '))
  for sign in operations:
    print(sign)
  
  should_continue = True
  
  while should_continue:
    sign = input('Pick an operation: ')
    num2 = float(input('Type the second number: '))
    function = operations[sign]
    answer = function(num1, num2)
  
    print(f"{num1} {sign} {num2} = {answer}")
    
    continue_calc =  input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new operation: ")
    
    if continue_calc == 'y':
      num1 = answer
    else:
      calculator()

calculator()