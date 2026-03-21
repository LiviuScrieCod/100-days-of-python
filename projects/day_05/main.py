import random
import time

print("Welcome to the totally unique and unheard of")
print(r''' ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  
______ 
| |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| |
|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |
|______||______||______||______||______||______||______||______||______||______||______||______||______||______|
 ______                                                                                                  ______ 
| |__| |                   █████   █████                          █████                                 | |__| |
|  ()  |                  ░░███   ░░███                         ███░░░███                               |  ()  |
|______|                   ░███    ░███   ██████   █████ █████ ███   ░░███ ████████                     |______|
 ______                    ░███████████  ░░░░░███ ░░███ ░░███ ░███    ░███░░███░░███                     ______ 
| |__| |                   ░███░░░░░███   ███████  ░░░█████░  ░███    ░███ ░███ ░░░                     | |__| |
|  ()  |                   ░███    ░███  ███░░███   ███░░░███ ░░███   ███  ░███                         |  ()  |
|______|                   █████   █████░░████████ █████ █████ ░░░█████░   █████                        |______|
 ______                   ░░░░░   ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░    ░░░░░░   ░░░░░                          ______ 
| |__| |                                                                                                | |__| |
|  ()  |                                                                                                |  ()  |
|______|                                                                                                |______|
 ______     ███████████                                                                   █████          ______ 
| |__| |   ░░███░░░░░███                                                                 ░░███          | |__| |
|  ()  |    ░███    ░███  ██████    █████   █████  █████ ███ █████  ██████  ████████   ███████          |  ()  |
|______|    ░██████████  ░░░░░███  ███░░   ███░░  ░░███ ░███░░███  ███░░███░░███░░███ ███░░███          |______|
 ______     ░███░░░░░░    ███████ ░░█████ ░░█████  ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███           ______ 
| |__| |    ░███         ███░░███  ░░░░███ ░░░░███ ░░███████████  ░███ ░███ ░███     ░███ ░███          | |__| |
|  ()  |    █████       ░░████████ ██████  ██████   ░░████░████   ░░██████  █████    ░░████████         |  ()  |
|______|   ░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░     ░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░          |______|
 ______                                                                                                  ______ 
| |__| |                                                                                                | |__| |
|  ()  |                                                                                                |  ()  |
|______|                                                               █████                            |______|
 ______                                                               ░░███                              ______ 
| |__| |     ███████  ██████  ████████    ██████  ████████   ██████   ███████    ██████  ████████       | |__| |
|  ()  |    ███░░███ ███░░███░░███░░███  ███░░███░░███░░███ ░░░░░███ ░░░███░    ███░░███░░███░░███      |  ()  |
|______|   ░███ ░███░███████  ░███ ░███ ░███████  ░███ ░░░   ███████   ░███    ░███ ░███ ░███ ░░░       |______|
 ______    ░███ ░███░███░░░   ░███ ░███ ░███░░░   ░███      ███░░███   ░███ ███░███ ░███ ░███            ______ 
| |__| |   ░░███████░░██████  ████ █████░░██████  █████    ░░████████  ░░█████ ░░██████  █████          | |__| |
|  ()  |    ░░░░░███ ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░           |  ()  |
|______|    ███ ░███                                                                                    |______|
 ______    ░░██████                                                                                      ______ 
| |__| |    ░░░░░░                                                                                      | |__| |
|  ()  |                                                                                                |  ()  |
|______|                                                                                                |______|
 ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______ 
| |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| || |__| |
|  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  ||  ()  |
|______||______||______||______||______||______||______||______||______||______||______||______||______||______|''')
print("")
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '_']
generated_password = []
all_characters_list = letters_list + numbers_list + symbols_list
generated_passwords_list = []
create_password = True

while create_password:
    while True:
        try:
            total_password_length = int(input("How long do you want your password to be? (use numbers) >>> "))
            break
        except ValueError:
            print("That's not a number. Try again!")
    while True:
        try:
            total_letters_count = int(
                input(f"How many letters do you want? (use numbers; {total_password_length} characters "
                      f"available) >>> "))
            if total_letters_count > total_password_length:
                print(f"Only {total_password_length} characters available!")
                continue
            break
        except ValueError:
            print("That's not a number. Try again!")
    while True:
        try:
            total_symbols_count = int(input(f"How many symbols do you want? (use numbers; "
                                            f"{total_password_length - total_letters_count} characters available) >>> "
                                            f""))
            if total_symbols_count > total_password_length - total_letters_count:
                print(f"Only {total_password_length - total_letters_count} characters available!")
                continue
            break
        except ValueError:
            print("That's not a number. Try again!")
    while True:
        try:
            total_numbers_count = int(input(f"How many numbers do you want? (use numbers; "
                                            f"{total_password_length - total_letters_count - total_symbols_count} "
                                            f"characters available) >>> "))
            if total_numbers_count > total_password_length - total_letters_count - total_symbols_count:
                print(f"Only {total_password_length - total_letters_count - total_symbols_count} characters available!")
                continue
            break
        except ValueError:
            print("That's not a number. Try again!")

    password_config = [
        (total_letters_count, letters_list),
        (total_numbers_count, numbers_list),
        (total_symbols_count, symbols_list),
    ]

    for number, source in password_config:
        for _ in range(number):
            generated_password.append(random.choice(source))

    if total_password_length > len(generated_password):
        for _ in range(total_password_length - len(generated_password)):
            generated_password.append(random.choice(all_characters_list))
            
    random.shuffle(generated_password)
    generated_passwords_list.append("".join(generated_password))

    print("Performing cybernetic witchcraft...")
    time.sleep(1.5)
    print("Disregarding latest technologies and best practices in cybersecurity...")
    time.sleep(1.5)
    print("Discombobulating hackers world wide...")
    time.sleep(1.5)
    print("Aaaaaand we're done!")
    time.sleep(1)
    print(f"Your new password is: {''.join(generated_password)}")

    while True:
        generated_password = []
        new_password = input("Would you like to [g]enerate a new password or [r]eview the passwords you've generated "
                             "so far? [g/r/n] >>> ")
        if new_password == "g":
            break
        elif new_password == "n":
            print("Thank you for using Hax0r Password generator!")
            print("Have an unhackable day!")
            create_password = False
            break
        elif new_password == "r":
            print(f"Your passwords are: {', '.join(generated_passwords_list)}")
        else:
            print("Please enter either 'g' to generate a new password, 'r' to review previously generated passwords or "
                  "'n' to exit")
