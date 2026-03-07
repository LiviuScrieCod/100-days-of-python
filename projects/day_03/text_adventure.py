import random
from game_data import story_texts
from game_data import prompts
from game_data import wounds
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
                    print(f'{" ".join(wounds["rat"])}. Your HP is now {player_stats["hp"]}')
                    print(story_texts["first_encounter"]["exit_chamber"])
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
            # add clear, add GO art
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
                print(wounds["death"])
                # add clear, add GO art
            break
    if not player_stats["is_alive"]:
        break
    print("-------------------------------------------------------------------")

    # 5. Encounter Hub
    print(story_texts["hub_encounter"]["hub"])
    print("-------------------------------------------------------------------")
    while True:
        choice5 = input(prompts["hub_encounter"]["hub"]).lower().strip()
        #if goblin alerted - skip hub!
    # 5.1. Left door
        if choice5 == "left":
            print(story_texts["hub_encounter"]["left_door"]["door"])
            choice5_left_room = input("Do you try to 'take' the key or 'leave' before the goblin wakes up? >>>  ").lower().strip()
            if choice5_left_room == "take":
                wakes_up = random.choice([True, False])
                if wakes_up:
                    print(story_texts["hub_encounter"]["left_door"]["stealth_failure"])
                    print("-------------------------------------------------------------------")
                    print(story_texts["hub_encounter"]["ahead"]["tunnel"])
                    break
                else:
                    print(story_texts["hub_encounter"]["left_door"]["stealth_success"])
                    player_stats["inventory"].append("iron_key")
                    # add text to remind player he's already visited this room

    # 5.2. Right door
        elif choice5 == "right":
            if "iron_key" in player_stats["inventory"]:
                print(story_texts["hub_encounter"]["right_door"]["door_key"])
                player_stats["inventory"].remove("iron_key")
                player_stats["inventory"].append("healing_potion")
                #set door is open, if player returns after opening the door
            else:
                print(story_texts["hub_encounter"]["right_door"]["door_no_key"])
                #change text if player has already opened the door
    # 5.3. BBEG tunnel
        elif choice5 == "ahead":
            print(story_texts["hub_encounter"]["ahead"]["tunnel"])
            break

    # 5.2.3.1. Fight the BBEG
    # 5.2.3.2. Epilogue
    # implement global keywords for retreat/game over and healing