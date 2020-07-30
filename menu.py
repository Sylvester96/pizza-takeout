import time
import main
import intro


def menu():
    print("\n******** Main Menu ********")
    print(
        "We have the following flavours available; \n F1. Hawaiian \n F2. Chicken & Mushroom \n F3. Chicken Tikka \n "
        "F4. "
        "BBQ Steak \n F5. Boerewors \n F6. Veggie")
    print("\n***Toppings***")
    print(" T1. Extra cheese \n T2. Sweet chilli \n T3. Tikka sauce \n T4. Sweet corn \n T5. Red/green pepper")
    print("\n***Crust***")
    print(" C1. Thick crust \n C2. Thin and crispy")
    print("\n***Available sizes***")
    print(" S1. Small @ 500/- \n S2. Medium @ 750/- \n S3. Large @ 950/- \n S4. Extra Large @ 1150/- ")
    time.sleep(2)
    order()


def order():
    print("\nPlease type in your: ")
    flavour = (input("Flavour: \n>>> ")).title()
    toppings = (input("Toppings: \n>>> ")).title()
    crust = (input("Crust type: \n>>> ")).title()
    size = (input("Size: \n>>> ")).title()
    quantity = int(input("Please enter the quantity of pizza(s) you'd like to order: \n>>> "))
    time.sleep(1)

    print(f'\nYou have ordered; {quantity}, {size}, {flavour}, pizza with {toppings} toppings, and a {crust}.')

    if size == "Small":
        print("\nYour total comes to: ksh", 500 * quantity)
    elif size == "Medium":
        print("\nYour total comes to: ksh", 750 * quantity)
    elif size == "Large":
        print("\nYour total comes to: ksh", 950 * quantity)
    elif size == "Large":
        print("\nYour total comes to: ksh", 1150 * quantity)
    else:
        print("\nInvalid choice. "
              "Please select again")



