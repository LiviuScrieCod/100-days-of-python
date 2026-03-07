import random
from game_data import story_texts
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
    # 1. Entering the cave scene
    # 2. Door on the left encounter
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