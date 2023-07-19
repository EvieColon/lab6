# this is Evelyn Colon's decoder/encoder file

def encode(password):
    new_password_list = []
    for number in password:
        new_number = str(int(number) + 3)
        if len(new_number) == 2:
            new_number = new_number[-1]
        new_password_list.append(new_number)
    new_password = ''.join(new_password_list)
    return new_password

def decode(original_password, encoded_password):
    print(f"The encoded password is {encoded_password}, and the original password is {original_password}")


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decode(original_password, encoded_password)
        elif option == 3:
            break
