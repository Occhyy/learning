import random

menu = "coffe, latte, cappuccino, tea"


def pickDrink() -> str:
    # barista robot exercise

    print("Hello, I am your barista robot.")
    name = str(input("what is your name? "))
    print(
        "Nice to meet you, "
        + name
        + " what from the menu would you like to order? "
        + menu
    )
    drink = input("what would you like to order? ")
    return drink


def pickDrink(drink, menu):
    if drink in menu:

        coffe = 1
        latte = 1.5
        cappuccino = 1.70
        tea = 1.20

    else:
        print("Sorry, we don't have that on the menu. Please choose from " + menu)
    if drink == "coffe":
        print("That will be " + str(coffe) + " €, please.")
    elif drink == "latte":
        print("That will be " + str(latte) + " €, please.")
    elif drink == "cappuccino":
        print("That will be " + str(cappuccino) + " €, please.")
    elif drink == "tea":
        print("That will be " + str(tea) + " €, please.")
    else:
        print("Sorry, we don't have that on the menu. Please choose from " + menu)


# dictionary example
"""
collectionOfDrinks = {
    "coffe": 1,
    "latte": 1.5,
    "cappuccino": 1.70,
    "tea": 1.20,
}
"""
# Loop cez dictionary
"""
for item in collectionOfDrinks:
    print(item, collectionOfDrinks[item])
"""
"""
drinks = ["coffe", "latte", "cappuccino", "tea", "beer"]
for st in range(len(drinks)):
    print(drinks[st])
"""

"""
stevec = 0  # oziroma i
while stevec < 5:
    print(stevec)
    stevec += 1  # stevec = stevec + 1
"""

stevec = 5  # obrnjeno, da se števec zmanjšuje
while stevec > 0:
    print(stevec)
    stevec -= 1  # stevec = stevec - 1
