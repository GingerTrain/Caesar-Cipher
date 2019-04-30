from enum import Enum
import operator


class Menu(Enum):
    ENCRYPT = 1
    DECRYPT = 2
    BRUTE = 3
    EXIT = 4
    RANGE = range(1, 5)
    ERROR = "\n-ERROR-\nPlease only use the values specified, thank you"


# Encrypts or decrypts input_text by shift_value based on crypt_choice
def crypt(input_text, shift_value, crypt_choice):
    output_text = ''

    for char in input_text:
        if char == ' ':
            output_text += ' '
        # Shifts uppercase letter by shift value and adjusts unicode value
        elif char.isupper():
            output_text += chr((crypt_choice(ord(char), shift_value) - 65)
                               % 26 + 65)
        # Shifts lowercase letter by shift value and adjusts unicode value
        else:
            output_text += chr((crypt_choice(ord(char), shift_value) - 97)
                               % 26 + 97)

    return output_text


# Brute forces input_text
def brute(input_text):
    output_text = ''

    for num in range(1, 27):
        line = ''

        for char in input_text:
            if char == ' ':
                line += char
            # Shifts uppercase letter by 1 and adjusts unicode value
            elif char.isupper():
                line += chr((ord(char) + num - 65) % 26 + 65)
            # Shifts lowercase letter by 1 and adjusts unicode value
            else:
                line += chr((ord(char) + num - 97) % 26 + 97)

        output_text += str(str(num) + " " + line + "\n")

    return output_text


# Menu loop
def main():
    while True:
        try:
            print("\n-MENU-")
            choice = int(input("1: Encrypt\n"
                               "2: Decrypt\n"
                               "3: Brute Force\n"
                               "4: Exit\n"))

            if choice not in Menu.RANGE.value:
                int("Error")

            elif choice == Menu.ENCRYPT.value:
                print("\n-ENCRYPT-")

                text = str(input("Please enter a string " +
                           "to encrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in text):
                    int("Error")

                shift = int(input("Please enter how many indexes " +
                            "you want to shift (0-25): "))
                if shift > 25 or shift < 0:
                    int("Error")

                cipher = crypt(text, shift, operator.add)

                print("Your original string is: " + text)
                print("Your encrypted string is: " + cipher)

            elif choice == Menu.DECRYPT.value:
                print("\n-DECRYPT-")

                cipher = str(input("Please enter a string " +
                             "to decrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in cipher):
                    int("Error")

                shift = int(input("Please enter how many indexes " +
                            "you want to shift (0-25): "))
                if shift > 25 or shift < 0:
                    int("Error")

                text = crypt(cipher, shift, operator.sub)

                print("Your original string is: " + cipher)
                print("Your decrypted string is: " + text)

            elif choice == Menu.BRUTE.value:
                print("\n-BRUTE FORCE-")

                cipher = str(input("Please enter a string " +
                             "to decrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in cipher):
                    int("Error")

                text = brute(cipher)

                print("Your original string is: " + cipher)
                print("Your decrypted strings are: \n" + text)

            elif choice == Menu.EXIT.value:
                break
        except ValueError:
            print(Menu.ERROR.value)
            continue

if __name__ == '__main__':
    main()
