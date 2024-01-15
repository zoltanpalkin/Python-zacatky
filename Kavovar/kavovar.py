#kavovar
#definvat objekty kavovaru latte/espresso/capuccino
#mince definovat
#matika
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
 
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
    }


def display_menu(MENU):
    x = MENU.fromkeys('latte')
    print(x)
display_menu(MENU)
