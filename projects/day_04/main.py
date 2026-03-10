import random
import time
from art_assets import *
from game_data import *

player_score = 0.0
opponent_score = 0

multiplier = 1.0
multiplier_record = 1.0

strike = 0

print(f'{utility["logo"]}\n')
print("Welcome to the 1978 Rock paper scissors olympics!\n")
print("This edition's main events are:")
while True:
    print("[S]urvival highscore")
    print("[K]ockout")
    print("[F]riendly")
    print("[Q]uit game as if unworthy of fatherly love\n")
    choose_game_type = input("Which will it be? >>> ").lower().strip()
    if choose_game_type not in ["s", "k", "f", "q"]:
        print("We're afraid that this particular event is not available...")
        continue
    elif choose_game_type == "q":
        print("You lose Internet privileges and gain 120 SHAAAAAAAAMEZES!")
        break
    elif choose_game_type == "s":
        while True:
            if strike==3:
                print("You forfeit the round!")
                multiplier = 1.0
                opponent_score+=1
                strike=0
                time.sleep(1.5)
            print(utility["delimiter"])
            neat_score = int(player_score) if player_score % 1 == 0 else player_score
            print(f"Player Score: {neat_score}")
            print(f"Current Multiplier: {multiplier}")
            print(f"Max Multiplier: {multiplier_record}")
            print(f"Opponent Score: {opponent_score}\n")
            ai_choice = random.randrange(len(valid_moves))
            # print(ai_choice)
            player_choice = input("Contestants choose: 'rock', 'paper' or 'scissors'? (q to wuss out of it) >>> ").strip().lower()
            if player_choice == "q":
                print("Wow... look at him go... the pressure must've been too much! Game Over!\n")
                time.sleep(1)
                break
            print("ROCK!")
            time.sleep(0.5)
            print("PAPER!")
            time.sleep(0.5)
            if player_choice not in valid_moves:
                strike+=1
                print(random.choice(confusion))
                time.sleep(0.5)
                print(f"Not a valid move! Strike {strike}!")
                time.sleep(0.5)
                continue
            player_choice = valid_moves.index(player_choice)
            strike = 0
            print("SCISSORS!")
            time.sleep(0.5)
            print("GO!")
            time.sleep(1)
            print(f"You picked: \n{basic_choices[player_choice]}")
            print(f"Your opponent picked: \n{basic_choices[ai_choice]}")
            if player_choice == ai_choice:
                print(outcome["draw"])
            elif (player_choice-ai_choice) % 3 == 1:
                player_score+=1*multiplier
                if multiplier ==1.0:
                    print(outcome["first_victory"])
                else:
                    print(outcome["sustained_victory"])
                multiplier += 0.5
                if multiplier>multiplier_record:
                    multiplier_record = multiplier
            else:
                opponent_score+=1
                if multiplier == 1.0:
                    print(outcome["first_defeat"])
                else:
                    print(outcome["sustained_defeat"])
                multiplier = 1.0

            next_round = input("Type 'q' to quit, anything else to continue >>> ").lower().strip()
            print("")
            if next_round == "q":
                player_score = 0.0
                opponent_score = 0

                multiplier = 1.0
                multiplier_record = 1.0
                break

