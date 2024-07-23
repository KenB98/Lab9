def encode(password):
    encoded = ""
    for char in password:
        num = int(char)
        new_num = (num + 3) % 10
        encoded += str(new_num)
    return encoded


def decode(password):
    decoded = ""
    for char in password:
        num = int(char)
        new_num = (num - 3) % 10
        decoded += str(new_num)
    return decoded