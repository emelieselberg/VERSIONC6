# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def encoder(password):
    encoded_password = ''
    for char in password:
        encoded_password += str(int(char) + 3)

    return encoded_password

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        password = ''
        if option == 1:
            password = input("Please enter your password to encode: ")
            print(encoder(password))
        elif option == 2:
            print("ignore this")
        elif option == 3:
            break



