# Encrypts text parameter by shift amount
def encrypt(text, shift):
    cipher = ''

    for char in text:
        if char == ' ':
            cipher = cipher + ' '
        elif char.isupper():
            # Uppercase letters
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            # Lowercase letters
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

# Decrypts text parameter by shift amount
def decrypt(text, shift):
    cipher = ''

    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            # Uppercase letters
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            # Lowercase letters
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

    return cipher

# Brute forces text parameter
def brute(text):
    cipher = ''

    for num in range(1, 27):
        line = ''

        for char in text:
            if char == ' ':
                line = line + char
            elif char.isupper():
                # Uppercase letters
                line = line + chr((ord(char) + num - 65) % 26 + 65)
            else:
                # Lowercase letters
                line = line + chr((ord(char) + num - 97) % 26 + 97)

        cipher = cipher + str(str(num) + " " + line + "\n")

    return cipher

# Menu loop
while True:
    try:
        print("\n-MENU-")
        choice = int(input("1: Encrypt\n"
                           "2: Decrypt\n"
                           "3: Brute Force\n"
                           "4: Exit\n"))

        if choice > 4 or choice < 1:
            int("Error")

        # Encrypt
        elif choice == 1:
            try:
                print("\n-ENCRYPT-")
                text = str(input("Please enter a string to encrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in text):
                    int("Error")
                shift = int(input("Please enter how many indexes you want to shift (0-25): "))
                if shift > 25 or shift < 0:
                    int("Error")
                cipher = encrypt(text, shift)
                print("Your original string is: " + text)
                print("Your encrypted string is: " + cipher)
            except ValueError:
                print("\n-ERROR-")
                print("Please only use the values specified, thank you")
                continue

        # Decrypt
        elif choice == 2:
            try:
                print("\n-DECRYPT-")
                text = str(input("Please enter a string to decrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in text):
                    int("Error")
                shift = int(input("Please enter how many indexes you want to shift (0-25): "))
                if shift > 25 or shift < 0:
                    int("Error")
                cipher = decrypt(text, shift)
                print("Your original string is: " + text)
                print("Your decrypted string is: " + cipher)
            except ValueError:
                print("\n-ERROR-")
                print("Please only use the values specified, thank you")
                continue

        # Brute Force
        elif choice == 3:
            try:
                print("\n-BRUTE FORCE-")
                text = str(input("Please enter a string to decrypt (a-z or A-Z): "))
                if not all(x.isalpha() or x.isspace() for x in text):
                    int("Error")
                cipher = brute(text)
                print("Your original string is: " + text)
                print("Your decrypted strings are: \n" + cipher)
            except ValueError:
                print("\n-ERROR-")
                print("Please only use the values specified, thank you")
                continue

        # Exit
        elif choice == 4:
            break
    except ValueError:
        print("\n-ERROR-")
        print("Please only use the values specified, thank you")
        continue
