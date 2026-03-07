# -*- coding: utf-8 -*-
import subprocess
import random
from game_data import story_texts
from game_data import prompts
from game_data import wounds
from game_data import art_assets
from game_data import music

player_stats = {
    "hp":100,
    "inventory": [],
    "is_alive": False,
    "acc": 70,
    "dmg": (5,10)
}

round_no = 1

bbeg_stats = {
    "hp": 100,
    "acc": 40,
    "special_att": 2,
    "dmg": {
        "regular": (8,12),
        "special": {
            "smash": {
                "acc": 50,
                "dmg": 25
            },
            "slash": {
                "acc": 65,
                "dmg": 35
            },
        }
    },
    "is_alive": True,
}

print(art_assets["opening_screen_art"])
while True:
    start = input(story_texts["adventure_start"]).lower().strip()
    if start == "start":
        player_stats["is_alive"] = True
        bgtrack = subprocess.Popen(['powershell', music["background_music"]])
        break
    else:
        print("A simple 'start' will suffice...")

while player_stats["is_alive"]:
    # TODO:
    # 1. Entering the cave
    print(story_texts["first_encounter"]["cave_entrance"])
    print("-------------------------------------------------------------------")
    print(story_texts["first_encounter"]["door"])
    print(art_assets["first_encounter"]["old_door"])

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
                    print(art_assets["first_encounter"]["altar"])
                    print(story_texts["first_encounter"]["healing_potion"])
                    player_stats["inventory"].append("healing_potion")
                    print(story_texts["first_encounter"]["exit_chamber"])
                    break
                elif choice2 == 'corner':
                    print(art_assets["first_encounter"]["junk"])
                    print(story_texts["first_encounter"]["rat_bite"])
                    player_stats["hp"] -= random.randint(1, 5)
                    print(f'{" ".join(wounds["rat"])}. Your HP is now {player_stats["hp"]}')
                    print(story_texts["first_encounter"]["exit_chamber"])
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

    #freeze text
    useless_input = input("Press any key to continue >>> ")

    # 3. Second encounter
    print(story_texts["second_encounter"]["tunnel_split"])
    print(art_assets["second_encounter"]["tunnel_split"])
    while True:
        choice3 = input(prompts["second_encounter"]["two_tunnels"]).lower().strip()
        # 3.1. 'Go left' outcome
        if choice3 == "left":
            print(story_texts["second_encounter"]["tunnel_split_left"])
            print("")
            print(art_assets["misc"]["go"])
            player_stats["is_alive"] = False
            bgtrack.terminate()
            break
        # 3.2. 'Go right' account
        elif choice3 == "right":
            print(story_texts["second_encounter"]["tunnel_split_right"])
        else:
            print("Focus brave knight, time is of the essence!")
            continue
        break

    if not player_stats["is_alive"]:
        break
    print("-------------------------------------------------------------------")

    # 4. Third encounter
    print(art_assets["third_encounter"]["surprise"])
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
                bgtrack.terminate()
            print(f'Your HP is now {player_stats["hp"]}')
            break
    if not player_stats["is_alive"]:
        break
    print("-------------------------------------------------------------------")

    # freeze text
    useless_input = input("Press any key to continue >>> ")

    # 5. Encounter Hub
    print(art_assets["hub_encounter"]["cave_hub"])
    print(story_texts["hub_encounter"]["hub"])
    print("-------------------------------------------------------------------")
    grabbed_key = False
    is_looted = False
    while True:
        choice5 = input(prompts["hub_encounter"]["hub"]).lower().strip()
    # 5.1. Left door
        if choice5 == "left":
            print(art_assets["hub_encounter"]["door_left"])
            if not grabbed_key:
                print(story_texts["hub_encounter"]["left_door"])
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
                        grabbed_key = True
                elif choice5_left_room == "leave":
                    continue
                elif choice5_left_room not in ["take", "leave"]:
                    print("Focus brave knight, time is of the essence!")
                    continue
            else:
                print(story_texts["hub_encounter"]["visited"]["goblin"])
                continue

    # 5.2. Right door
        elif choice5 == "right":
            if not is_looted:
                print(art_assets["first_encounter"]["old_door"])
                if "iron_key" in player_stats["inventory"]:
                    print(story_texts["hub_encounter"]["right_door"]["door_key"])
                    player_stats["inventory"].remove("iron_key")
                    player_stats["inventory"].append("healing_potion")
                    is_looted = True
                else:
                    print(story_texts["hub_encounter"]["right_door"]["door_no_key"])
            else:
                print(art_assets["hub_encounter"]["door_left"])
                print(story_texts["hub_encounter"]["visited"]["potion"])
                continue

    # 5.3. BBEG tunnel
        elif choice5 == "ahead":
            print("-------------------------------------------------------------------")
            print(story_texts["hub_encounter"]["ahead"]["tunnel"])
            break

        elif choice5 not in ["left", "right", "ahead"]:
            print("Focus brave knight, time is of the essence!")

    # freeze text
    useless_input = input("Press any key to continue >>> ")

    # 6. BBEG encounter:
    print(story_texts["bbeg"]["boss_chamber"])
    print(art_assets["bbeg"]["bbeg"])
    print(story_texts["bbeg"]["monster_desc"])
    print("-------------------------------------------------------------------")
    finale= input(prompts["bbeg"]["final_decision"]).lower().strip()
    bgtrack.terminate()
    combat_track = subprocess.Popen(['powershell', music["combat_music"]])
    if finale not in ['flee', 'fight']:
        print("Focus brave knight, time is of the essence!")
    elif finale == "flee":
        #print art!
        print(story_texts["epilogue"]["flee"])
        print(art_assets["misc"]["pathetic"])
        break
    elif finale == "fight":
        print(story_texts["bbeg"]["cta"])
        while player_stats["is_alive"]:
            # 6.1. Hero round
            print("///////////////////////////////////////////////////////////////////")
            print(f"Round {round_no}")
            hp_turn_start = player_stats["hp"]
            choiceF = input(prompts["bbeg"]["hero_action"]).lower().strip()
            if choiceF not in ["a", "attack", "h", "heal", "i", "inventory"]:
                print("Focus brave knight, your life is at stake!")
                continue
            elif choiceF in ["h", "heal"]:
                if "healing_potion" in player_stats["inventory"]:
                    print(art_assets["misc"]["caduceus"])
                    player_stats["hp"] = min(100, player_stats["hp"]+50)
                    print(f"You regain your strength! Your HP is now {player_stats['hp']}")
                    player_stats["inventory"].remove("healing_potion")
                else:
                    print("Alas, Sir Knight, you've run out of healing potions!")
                    continue
            elif choiceF in ["i", "inventory"]:
                if not player_stats["inventory"]:
                    print("Your sack is empty, Sir Knight!")
                    continue
                else:
                    print(f"You still carry {', '.join(player_stats['inventory'])}")
                    continue
            elif choiceF in ['a', 'attack']:
                print(art_assets["fight"]["hero_attacks"])
                hero_strike = random.randint(1, 101)
                if hero_strike <= player_stats["acc"]:
                    print(story_texts["bbeg"]["hero_hit"])
                    dmg = random.randint(player_stats["dmg"][0], player_stats["dmg"][1])
                    bbeg_stats["hp"]-=dmg
            # 6.1.1. Check boss stats
                    if bbeg_stats["hp"] <= 0:
                        print(story_texts["bbeg"]["bbeg_death"])
                        bbeg_stats["is_alive"] = False
                        combat_track.terminate()
                        break
                elif hero_strike > player_stats["acc"]:
                    print(story_texts["bbeg"]["hero_miss"])
            print("-------------------------------------------------------------------")
            # 6.2.1. Boss round
            print(story_texts["bbeg"]["bbeg_action"])
            special_att_chance = random.randint(1, 5)
            bbeg_strike = random.randint(1, 101)
            if (bbeg_stats["hp"] <= 32 or special_att_chance == 1) and bbeg_stats["special_att"] > 0:
                print(story_texts["bbeg"]["bbeg_special"])
                special_choice = random.choice(["smash", "slash"])
                attack_type = bbeg_stats["dmg"]["special"][special_choice]
                if bbeg_strike<= attack_type["acc"]:
                    bbeg_stats["special_att"] -= 1
                    dmg = attack_type["dmg"]
                    player_stats["hp"] -= dmg
                else:
                    print(story_texts["bbeg"]["bbeg_miss"])
            else:
                if bbeg_strike <= bbeg_stats["acc"]:
                    dmg=random.randint(bbeg_stats["dmg"]["regular"][0], bbeg_stats["dmg"]["regular"][1])
                    player_stats["hp"]-=dmg
                else:
                    print(story_texts["bbeg"]["bbeg_miss"])

            if player_stats["hp"] <= 0:
                player_stats["is_alive"] = False
                print(wounds["death"])
                combat_track.terminate()
                #print art
                break
            elif hp_turn_start > player_stats["hp"]:
                print(story_texts["bbeg"]["bbeg_hit"])
                print(f"You have {player_stats['hp']} HP left! Steel yourself!")

            round_no+=1

    # 7. Epilogue
    if player_stats["is_alive"]:
        print(story_texts["epilogue"]["victory"])
        #print art
    elif not player_stats["is_alive"]:
        print(story_texts["epilogue"]["defeat"])
        #print art
    break