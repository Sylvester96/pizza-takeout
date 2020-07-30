import time
import main
import menu


def intro():
    print("\n ~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("|    SHABBAZ PIZZA    |")
    print("|    TAKEAWAY    |")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("")
    print("Welcome to SHABBAZ PIZZA your one stop pizza joint that will leave you craving for more")
    print("\nTo make your order kindly follow the following instructions; ")
    time.sleep(2)

    name = input("Please state your name below: \n>>> ").title()

    print("\nOk " + name + ", let's get you started on your order right away, shall we.")
    time.sleep(2)

    menu.menu()
