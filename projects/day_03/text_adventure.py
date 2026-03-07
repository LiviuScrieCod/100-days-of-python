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
    # 2. First encounter
    # 2.1. Inventory logic
    while True:
        choice = input(prompts["first_encounter"]["door"]).lower().strip()
        if choice == "ignore":
            print(story_texts["first_encounter"]["ignore_door"])
            break
        elif choice == 'enter':
            print(story_texts["first_encounter"]["chamber"])
            choice2 = input(prompts["first_encounter"]["explore"]).lower().strip()
            if choice2 == "center":
                print(story_texts["first_encounter"]["healing_potion"])
                player_stats["inventory"].append("healing_potion")
                print(story_texts["first_encounter"]["exit_chamber"])
                break
            elif choice2 == 'corner':
                continue
            elif choice2 == 'leave room':
                print(story_texts["first_encounter"]["exit_chamber"])
                break
            else:
                print("Focus brave knight, time is of the essence!")

        else:
            print("Focus brave knight, time is of the essence!")



    # 3. Noise further ahead in the tunnel
    # 3.1. Go left outcome
    # 3.2. Go right account
    # 4.2. Trap encounter
    # 5.2. Triple choice encounter
    # 5.2.1. Door on left encounter
    # 5.2.2. Door on right encounter
    # 5.2.3. Forward towards the BBEG
    # 5.2.3.1. Fight the BBEG
    # 5.2.3.2. Epilogue
    # implement global keywords for retreat/game over and healing
    break