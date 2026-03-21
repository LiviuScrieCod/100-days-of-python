import random
import time
from project_data import *

generated_password = []
all_characters_list = []
for key, value in validation.items():
    if "characters" in value:
        all_characters_list += value["characters"]
generated_passwords_list = []

print("Welcome to the totally unique and unheard of")
print(art_assets["logo"])
print("")

while True:
    print(f"Choose one of the available services:")
    print("[1] Leet-alizer")
    print("[2] Hax0r Password generator")
    print("[3] Security audit")
    print("[Q]uit")

    menu_choice = input("What will it be? >>> ").strip().lower()
    if menu_choice == "q":
        print("Sad to see you go...")
        print("Don't let the hax0r hack at night!")
        time.sleep(1.5)
        break
    elif menu_choice == "1":
        leetalize = True
        while leetalize:
            print("\nLet's 1337-41!23 your password!")
            user_password = input("Enter your password: >>> ")
            hacker_password = ""
            cool_score = 0

            for _ in user_password:
                lower_char = _.lower()
                if lower_char in hax0rize:
                    replace_character_list = list(hax0rize[lower_char].keys())
                    new_character = random.choice(replace_character_list)
                    hacker_password += new_character
                    cool_score += hax0rize[lower_char][new_character]
                else:
                    hacker_password += lower_char

            print(f"\nYou new and improved password is: {hacker_password}")
            final_score = cool_score / len(user_password)
            print(f"On a scale of tool to cool, your password has the following rating:")
            if final_score <= 0.5:
                print("BROKE! You're a basic middle management web surfer!")
            elif final_score <= 1.0:
                print("NOVICE! Are you even trying, bro?")
            elif final_score <= 1.5:
                print("CYBER! Now you just have to slop it up some more!")
            elif final_score <= 2.0:
                print("CYBER PUNK! Full package, still not impressive tho...")
            elif final_score <= 2.5:
                print("SYSTEM OVERRIDE! It's starting to get interesting")
            elif final_score <= 3.0:
                print("Hax0r! Welcome to the above average league!")
            elif final_score <= 3.5:
                print("3|173 Nerdz0|2 5000! All you hacking are belong to us!")
            elif final_score <= 4.95:
                print("PINNACLE OF HAx0RRING! Living GOD among programming crabs!")
            elif final_score <= 5.0:
                print("You cheated! |3ooooooo!")

            print("")
            while True:
                again = input("1337-41!23 another password? [y/n] >>> ").strip().lower()
                if again == "y":
                    break
                elif again == "n":
                    print("")
                    leetalize = False
                    break
                else:
                    print("Not an option!")


    elif menu_choice == "2":
        create_password = True
        while create_password:
            for index, (key, value) in enumerate(validation.items()):
                while True:
                    if index == 0:
                        prompt = f"{value['question']}" + " (use numbers) >>> "
                    else:
                        prompt = f"{value['question']}" + (
                            f" (use numbers; {available_characters_remaining} characters "
                            f"available) >>> ")
                    try:
                        value['answer'] = int(input(prompt))
                        if index == 0:
                            available_characters_remaining = value['answer']
                        else:
                            if available_characters_remaining < value['answer']:
                                print(
                                    f"That's too many {key}! Only {available_characters_remaining} characters "
                                    f"available!")
                                continue
                            available_characters_remaining -= value['answer']
                        break
                    except ValueError:
                        print("That's not a number!")

            print("")
            password_config = [
                (validation['letters']['answer'], validation['letters']['characters']),
                (validation['numbers']['answer'], validation['numbers']['characters']),
                (validation['symbols']['answer'], validation['symbols']['characters']),
            ]

            for number, source in password_config:
                for _ in range(number):
                    generated_password.append(random.choice(source))

            if available_characters_remaining > 0:
                for _ in range(available_characters_remaining):
                    generated_password.append(random.choice(all_characters_list))

            random.shuffle(generated_password)
            generated_passwords_list.append("".join(generated_password))

            loading = ux_lines[:]
            for _ in range(len(ux_lines)):
                line = random.choice(loading)
                print(line)
                loading.pop(loading.index(line))
                time.sleep(1.5)
            print("Aaaaaand we're done!")
            time.sleep(1)
            print(f"Your new password is: {''.join(generated_password)}\n")

            while True:
                generated_password = []
                available_characters_remaining = None
                for key, value in validation.items():
                    value['answer'] = None
                new_password = input(
                    "Would you like to [g]enerate a new password or [r]eview the passwords you've generated "
                    "so far? [g/r/n] >>> ")
                if new_password == "g":
                    break
                elif new_password == "n":
                    print("\nThank you for using Hax0r Password generator!")
                    print("Have an unhackable day!\n")
                    create_password = False
                    break
                elif new_password == "r":
                    print(f"Your passwords are: {', '.join(generated_passwords_list)}")
                else:
                    print(
                        "Please enter either 'g' to generate a new password, 'r' to review previously generated "
                        "passwords "
                        "or "
                        "'n' to exit")
    elif menu_choice == "3":
        break
    elif menu_choice not in ["q", "1", "2", "3"]:
        print("\n404! User_intention unc134r!\n")
