# Emelie Selberg

def encoder(password):
    encoded_password = ''
    for char in password:
        encoded_password += str(int(char) + 3)

    return encoded_password

def decoder(password):
    decoded = ""
    for i in password:
        decoded += str((int(i) - 3))

    return decoded

if __name__ == '__main__':
    password = ''
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print("The encoded password is " + password + ", and the original password is " + decoder(password) + ".\n")
        elif option == 3:
            break

