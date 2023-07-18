def encoder(password):
    new_password_list = []
    for number in password:
        new_number = str(int(number) + 3)
        if len(new_number) == 2:
            new_number = new_number[-1]
        new_password_list.append(new_number)
    new_password = ''.join(new_password_list)
    return new_password


def decoder(password):
    old_password_list = []
    for number in password:
        old_number = int(number) - 3
        if old_number < 0:
            old_number = old_number + 10
        old_number = str(old_number)
        old_password_list.append(old_number)
    old_password = ''.join(old_password_list)
    return old_password


if __name__ == '__main__':
    while True:
        print("Decoder/Encoder Menu")
        print("--------------------")
        print("1. Encode password")
        print("2. Decode password")
        print("3. Exit program")
        option = int(input("Please select an option: "))
        if option == 1:
            original_password = input("Please enter the password to be encoded: ")
            print(f"Encoded password: {encoder(original_password)}")
        elif option == 2:
            encoded_password = input("Please enter the password to be decoded: ")
            print(f"Decoded password: {decoder(encoded_password)}")
        elif option == 3:
            break
        else:
            print("Invalid input! Please make another selection.")
