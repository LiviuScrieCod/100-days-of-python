import random
import time
from project_data import *

print("Welcome to the totally unique and unheard of")
print(art_assets["logo"])
print("")

generated_password = []
all_characters_list = []
for key, value in validation.items():
    if "characters" in value:
        all_characters_list += value["characters"]
generated_passwords_list = []
create_password = True

while create_password:
    for index, (key, value) in enumerate(validation.items()):
        while True:
            if index == 0:
                prompt = f"{value['question']}" + " (use numbers) >>> "
            else:
                prompt = f"{value['question']}" + (f" (use numbers; {available_characters_remaining} characters "
                                                   f"available) >>> ")
            try:
                value['answer'] = int(input(prompt))
                if index == 0:
                    available_characters_remaining = value['answer']
                else:
                    if available_characters_remaining < value['answer']:
                        print(f"That's too many {key}! Only {available_characters_remaining} characters available!")
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
