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