import random
import time
import os
import platform
from project_data import *

generated_password = []
all_characters_list = []
for key, value in validation.items():
    if "characters" in value:
        all_characters_list += value["characters"]

passwords_vault = {}
passwords_doc = []

print("Welcome to the totally unique and unheard of:")
print(art_assets["logo"])
print("")

while True:
    print("Recommended workflow: use [1] and/or [2] to generate your password(s), than use the security audit to "
          "evaluate your password(s) and then save them in a file using the [4] vault")
    print(f"Choose one of the available services:")
    print("[1] Leet-alizer")
    print("[2] Hax0r Password generator")
    print("[3] Security audit")
    print("[4] Vault")
    print("[Q]uit")

    menu_choice = input("What will it be? >>> ").strip().lower()
    if menu_choice == "q":
        print("Sad to see you go...")
        print("Don't let the hax0r hack at night!")
        time.sleep(1.5)
        break
    elif menu_choice == "1":
        leetalize = True
        leet_passwords = []
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
            rating = ""
            print(f"On a scale of tool to cool, your password has the following rating:")
            if final_score <= 0.5:
                print("BROKE! You're a basic middle management web surfer!")
                rating = "BROKE!"
            elif final_score <= 1.0:
                print("NOVICE! Are you even trying, bro?")
                rating = "NOVICE!"
            elif final_score <= 1.5:
                print("CYBER! Now you just have to slop it up some more!")
                rating = "CYBER!"
            elif final_score <= 2.0:
                print("CYBER PUNK! Full package, still not impressive tho...")
                rating = "CYBER PUNK!"
            elif final_score <= 2.5:
                print("SYSTEM OVERRIDE! It's starting to get interesting")
                rating = "SYSTEM OVERRIDE!"
            elif final_score <= 3.0:
                print("Hax0r! Welcome to the above average league!")
                rating = "Hax0r!"
            elif final_score <= 3.5:
                print("3|173 Nerdz0|2 5000! All you hacking are belong to us!")
                rating = "3|173 Nerdz0!"
            elif final_score <= 4.95:
                print("PINNACLE OF HAx0RRING! Living GOD among programming crabs!")
                rating = "PINNACLE OF HAx0RRING!"
            elif final_score <= 5.0:
                print("You cheated! |3ooooooo!")
                rating = "You cheated!"

            leet_passwords.append(f"Password: {hacker_password} | Rating: {rating}")
            entry_id = len(passwords_vault) + 1
            password_data = {
                "password_type": "leet",
                "original_password": user_password,
                "new_password": hacker_password,
                "cool_rating": rating,
                "security_rating": "Not audited",
            }
            passwords_vault[entry_id] = password_data

            print("")

            while True:
                again = input("1337-41!23 another password? [y/n] >>> ").strip().lower()
                if again == "y":
                    break
                elif again == "n":
                    print("")
                    leetalize = False
                    leet_passwords = []
                    break
                else:
                    print("Not an option!")
    elif menu_choice == "2":
        create_password = True
        generated_passwords_list = []
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
            generated_password_final = "".join(generated_password)
            generated_passwords_list.append(generated_password_final)

            entry_id = len(passwords_vault) + 1
            password_data = {
                "password_type": "generated",
                "original_password": None,
                "new_password": generated_password_final,
                "cool_rating": None,
                "security_rating": 'Not audited',
            }
            passwords_vault[entry_id] = password_data

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
        while True:
            if not passwords_vault:
                print("The Vault is empty! Generate/Convert some passwords first!")
                break
            else:
                print("------VAULT CONTENTS------")
                print(f"Your vault contains {len(passwords_vault)} entries!")
                for key, value in passwords_vault.items():
                    format_row = " | ".join([f"{subkey.replace('_', ' ').title()}: {subvalue}" for subkey, subvalue in
                                             value.items()])
                    display_row = f"{key}: {format_row}"
                    print(display_row)
            print("")
            print("In the security audit center you may: ")
            print("[B]ulk audit")
            print("[I]ndividual audit")
            print("[D]elete entry")
            print("[R]eturn to main menu")
            request_audit = input("What would you like to do? >>> ").lower().strip()
            if request_audit not in ["b", "i", "d", "r"]:
                print("Not an option")
                continue
            elif request_audit == "b":
                for key, value in passwords_vault.items():
                    audit_score = 0
                    if value['security_rating'] == "Not audited":
                        if len(value['new_password']) >= 10:
                            audit_score += 1
                        if any(char.isdigit() for char in value['new_password']):
                            audit_score += 1
                        if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in value['new_password']):
                            audit_score += 1
                        if any(char.isupper() for char in value['new_password']) and any(
                                char.islower() for char in value['new_password']):
                            audit_score += 1
                        if value['password_type'] == 'leet':
                            audit_score += 1
                        value['security_rating'] = (audit_score * "⭐") + ((5 - audit_score) * "☆")
            elif request_audit == "i":
                while True:
                    item_number = input("Which password do you want audited next? Type password number or q to quit "
                                        ">>> "
                                        "").lower().strip()
                    if item_number == "q":
                        break
                    try:
                        item_number = int(item_number)
                    except ValueError:
                        print("Please use numbers only")
                        continue
                    if item_number in passwords_vault:
                        audit_score = 0
                        target_id = passwords_vault[item_number]
                        if len(target_id['new_password']) >= 10:
                            audit_score += 1
                        if any(char.isdigit() for char in target_id['new_password']):
                            audit_score += 1
                        if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in target_id['new_password']):
                            audit_score += 1
                        if any(char.isupper() for char in target_id['new_password']) and any(
                                char.islower() for char in target_id['new_password']):
                            audit_score += 1
                        if target_id['password_type'] == 'leet':
                            audit_score += 1
                        target_id['security_rating'] = (audit_score * "⭐") + ((5 - audit_score) * "☆")
                        print(f"\nYour password {item_number}. {target_id['new_password']} is:"
                              f" {target_id['security_rating']}!")
                    else:
                        print("That ID doesn't exist in the vault")
            elif request_audit == "d":
                while True:
                    item_number = input("Which password do you want to delete next? Type password number or q to quit "
                                        ">>> "
                                        "").lower().strip()
                    if item_number == "q":
                        break
                    try:
                        item_number = int(item_number)
                    except ValueError:
                        print("Please use numbers only")
                        continue
                    if item_number in passwords_vault:
                        del passwords_vault[item_number]
                        print(f"\nYour password has been successfully deleted!")
                    else:
                        print("That ID doesn't exist in the vault")
            elif request_audit == "r":
                break
    elif menu_choice == "4":
        while True:
            passwords_doc = []
            if not passwords_vault:
                print("The Vault is empty! Generate/Convert some passwords first!")
                break
            else:
                while True:
                    user_choice = input("Would you like to look up a password or display your entire "
                                        "vault? [y/n]: >>> ").lower().strip()
                    if user_choice not in ["y", "n"]:
                        print("Not an option.")
                        continue
                    if user_choice == "n":
                        break
                    else:
                        lookup = input("Input your password or part of your password: >>> ").lower().strip()
                        found = False
                        for key, value in passwords_vault.items():
                            if lookup.lower() in value['new_password'].lower():
                                found = True
                                password_info = " | ".join(f"{k.replace('_', ' ').title()}: {v}" for k,
                                v in value.items())
                                print(f"Your password info is: {key}. {password_info}")

                        if not found:
                            print(f"Password not in the vault.")
                        continue

                print("------VAULT CONTENTS------")
                for key, value in passwords_vault.items():
                    format_row = " | ".join([f"{subkey.replace('_', ' ').title()}: {subvalue}" for subkey, subvalue in
                                             value.items()])
                    display_row = f"{key}: {format_row}"
                    passwords_doc.append(display_row)
                    print(display_row)

                while True:
                    save_input = input("\nDo you want to save your passwords in a file? [y/n]: >>> ")
                    if save_input == "y":
                        with open("passwords_vault.txt", "w", encoding="utf-8") as f:
                            f.write("\n".join(passwords_doc))
                        print("Your file was successfully saved as 'passwords_vault.txt' ")

                        user_system = platform.system()
                        python_file_path = os.getcwd()

                        if user_system == "Windows":
                            os.startfile(python_file_path)
                        elif user_system == "Darwin":
                            os.system(f'open "{python_file_path}"')
                        else:
                            os.system(f"xdg-open {python_file_path}")
                        break
                    elif save_input == "n":
                        print("Suite yourself!")
                        break
                    else:
                        print("wardrobe.")
                print("")
                break
    elif menu_choice not in ["q", "1", "2", "3", "4"]:
        print("\n404! User_intention unc134r!\n")
