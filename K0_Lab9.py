def menu():
    print("Menu")
    print("-"*13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    new = []
    for num in password:
        number = int(num)
        new.append(number)

    encoded = ""
    for val in new:
        if val < 7:
            val += 3
            encoded += str(val)
        else:
            if val == 7:
                val = "0"
            elif val == 8:
                val = "1"
            elif val == 9:
                val = "2"
            encoded += str(val)
    return "".join(encoded)


def decode(password):
    decoded = ""
    for char in password:
        num = int(char)
        new_num = (num - 3) % 10
        decoded += str(new_num)
    return decoded


def main():

    while True:
        menu()
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            original = decode(encoded)
            print(f"The encoded passwrod is {encoded}, and the original password is {original}.")
            print()
        elif option == 3:
            break


if __name__ == "__main__":
    main()
