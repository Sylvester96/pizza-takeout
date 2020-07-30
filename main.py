import time
import intro


def main():
    confirmation = "no"
    while confirmation == "no" or confirmation == "n":
        intro.intro()
        confirmation = input("\nDo you confirm your order? ('no' or 'n' 'to re-enter your order details): \n>>> ").lower()
        print("You're order is all set now. Kindly wait as we prepare your order in afew mins.")
        print("\nThank you for choosing us. Bon Apetite!")


if __name__ == "__main__":
    main()
