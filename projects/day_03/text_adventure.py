import random
from game_data import story_texts
from game_data import prompts
from game_data import art_assets


player_stats = {
    "hp":100,
    "inventory": [],
    "is_alive": False
}

print(art_assets["opening_screen_art"])
while True:
    start = input(story_texts["adventure_start"]).lower().strip()
    if start == "start":
        player_stats["is_alive"] = True
        break
    else:
        print("A simple 'start' will suffice...")

while player_stats["is_alive"]:
    # TODO:
    # 1. Entering the cave
    print(story_texts["first_encounter"]["cave_entrance"])
    print(story_texts["first_encounter"]["door"])
    # 2. First encounter
    while True:
        choice = input(prompts["first_encounter"]["door"]).lower().strip()
        if choice == "ignore":
            print(story_texts["first_encounter"]["ignore_door"])
            break
        elif choice == 'enter':
            print(story_texts["first_encounter"]["chamber"])
            while True:
                choice2 = input(prompts["first_encounter"]["explore"]).lower().strip()
                if choice2 == "center":
                    # 2.1. Inventory logic
                    print(story_texts["first_encounter"]["healing_potion"])
                    player_stats["inventory"].append("healing_potion")
                    # print(player_stats["inventory"])
                    print(story_texts["first_encounter"]["exit_chamber"])
                    break
                elif choice2 == 'corner':
                    print(story_texts["first_encounter"]["rat_bite"])
                    player_stats["hp"] -= random.randint(1, 5)
                    # print(player_stats["hp"])
                    break
                elif choice2 == 'leave room':
                    print(story_texts["first_encounter"]["exit_chamber"])
                    break
                else:
                    print("Focus brave knight, time is of the essence!")

        else:
            print("Focus brave knight, time is of the essence!")
            continue
        break
    print("-------------------------------------------------------------------")
    # 3. Second encounter
    print(story_texts["second_encounter"]["tunnel_split"])
    while True:
        choice3 = input(prompts["second_encounter"]["two_tunnels"]).lower().strip()
        # 3.1. 'Go left' outcome
        if choice3 == "left":
            print(story_texts["second_encounter"]["tunnel_split_left"])
            player_stats["is_alive"] = False
            break
        # 3.2. 'Go right' account
        elif choice3 == "right":
            print(story_texts["second_encounter"]["tunnel_split_right"])
        else:
            print("Focus brave knight, time is of the essence!")
            continue
        break
    print("-------------------------------------------------------------------")
    if not player_stats["is_alive"]:
        break

    # 4. Third encounter
    print(story_texts["third_encounter"]["trap"])
    while True:
        choice4 = input(prompts["third_encounter"]["trap"]).lower().strip()
        is_lucky = random.choice([True, False])
        if choice4 not in ["sprint", "roll"]:
            print(story_texts["third_encounter"]["hesitation"])
        if is_lucky:
            print(story_texts["third_encounter"]["trap_success"])
            break
        else:
            print(story_texts["third_encounter"]["trap_failure"])
            player_stats["hp"] -= 30
            if player_stats["hp"] <= 0:
                player_stats["is_alive"] = False
            break
    if not player_stats["is_alive"]:
        break
    print("-------------------------------------------------------------------")


    # 5.2. Triple choice encounter
    # 5.2.1. Door on left encounter
    # 5.2.2. Door on right encounter
    # 5.2.3. Forward towards the BBEG
    # 5.2.3.1. Fight the BBEG
    # 5.2.3.2. Epilogue
    # implement global keywords for retreat/game over and healing
    break