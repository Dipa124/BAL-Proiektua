import random
import string
from colorama import Fore, Style, Back


# Pasahitza sortzen duen funtzioa
def password_creator(num):
    password = ""
    for n in range(0, int(num)):
        character_type = random.choice(("number", "letter", "symbol"))

        if character_type == "number":
            character = random.choice(string.digits)
            character = str(character)
            password += character
        elif character_type == "letter":
            character = random.choice(string.ascii_letters)
            password += character
        elif character_type == "symbol":
            character = random.choice(string.punctuation)
            password += character
    return password


# Programaren buklea
def main():
    print(Style.BRIGHT + Fore.CYAN + Back.LIGHTBLACK_EX +
          "---PASAHITZA SORTZAILEA---" + Style.RESET_ALL)

    while True:
        num = input("Pasahitzaren luzeera sartu (zenbaki osoetan): ")
        try:
            int(num)
            break
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "\nEmandako erantzuna ez da zuzena.",
                  "\nZiurtatu zaitez ez duzunik zenbakia ez den bestelako karakterik",
                  "eta sartutako zenbakia osoa dela" + Style.RESET_ALL)

    print("\n" + Style.BRIGHT + "Pasahitza hurrengoa da: " + Style.RESET_ALL + password_creator(num))


# Kodea executatu
if __name__ == "__main__":
    main()
