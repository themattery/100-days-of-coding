MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def get_resources():
    """Returns each resource quantity."""
    return f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${resources['money']}"""


def check_drink_resources(drink_resources):
    """Checks if there are enough resources to make the drink and returns boolean."""
    for item in drink_resources:
        if drink_resources[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def calculate_payment():
    """Returns total from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * QUARTER
    dimes = int(input("How many dimes? ")) * DIME
    nickels = int(input("How many nickels? ")) * NICKEL
    pennies = int(input("How many pennies? ")) * PENNY
    total = quarters + dimes + nickels + pennies
    return total


def check_transaction(payment, drink_cost):
    """Checks validity of transaction and returns boolean."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources['money'] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients used from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    order = input("What's your order? (espresso/latte/cappuccino): ")
    if order == 'off':
        is_on = False
    elif order == 'report':
        print(get_resources())
    else:
        drink = MENU[order]
        if check_drink_resources(drink['ingredients']):
            payment = calculate_payment()
            if check_transaction(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])
                