import random
import time
from art_assets import *
from game_data import *

player_score = 0.0

multiplier = 1.0
multiplier_record = 1.0

strike = 0
active_title = " "
last_title = "unremarkable"
league_standing = {}

change_opponent = True

print("")
print(f'{utility["logo"]}\n')
print("Welcome to the 1978 Rock paper scissors olympics!\n")

player_name = input("What is your name? (EVERYONE has two names separated by a space!) >>> ").strip().title().split()
if len(player_name) < 2:
    player_name.append("Icouldn'tbeaskedovich")
elif len(player_name) > 2:
    player_name= [player_name[0], "Ican'ttakeahintson"]

print("\nThis edition's main events are:")
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
        time.sleep(1)
        break
    elif choose_game_type == "s":
        while True:
            if change_opponent:
                new_opponent_index = random.randrange(len(random_opponents))
                new_opponent = random_opponents[new_opponent_index][0]
                new_opponent_title= random_opponents[new_opponent_index][1]
                print(f"{new_opponent} steps into the limelight against {player_name[0]}{active_title}{player_name[1]}!\n")
            else:
                print(f"It will take more than that to get {new_opponent} off the stage!\n")

            print(utility["delimiter"])
            if strike==3:
                print("You forfeit the round!")
                multiplier = 1.0
                strike=0
                time.sleep(1.5)
                change_opponent=True
                continue

            neat_score = int(player_score) if player_score % 1 == 0 else player_score
            print(f"{player_name[0]}{active_title}{player_name[1]}'s Score: {neat_score}")
            print(f"Current Multiplier: {multiplier}")
            print(f"Max Multiplier: {multiplier_record}")
            print(f"Formerly known as: {last_title}\n")
            ai_choice = random.randrange(len(valid_moves))
            print(ai_choice)
            player_choice = input("Contestants choose: 'rock', 'paper' or 'scissors'? (q to wuss out of it) >>> ").strip().lower()
            if player_choice == "q":
                print("Wow... look at him go... the pressure must've been too much! Game Over!\n")
                player_score = 0.0

                multiplier = 1.0
                multiplier_record = 1.0

                strike = 0

                active_title = " "
                last_title = "*none_on_record*"
                league_standing = {}

                change_opponent = True
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
            print(f"{player_name[0]}{active_title}{player_name[1]} picks: \n{basic_choices[player_choice]}")
            print(f"{new_opponent} picks: \n{basic_choices[ai_choice]}")
            if player_choice == ai_choice:
                print(outcome["draw"])
            elif (player_choice-ai_choice) % 3 == 1:
                change_opponent = False
                league_standing[new_opponent] = league_standing.get(new_opponent, 0) + 1
                player_score+=1*multiplier
                if multiplier ==1.0:
                    print(outcome["first_victory"])
                    active_title = " "
                else:
                    print(outcome["sustained_victory"])
                multiplier += 0.5
                if multiplier>multiplier_record:
                    multiplier_record = multiplier
                if league_standing[new_opponent]==3:
                    active_title = f" '{new_opponent_title}' "
                    print(f"THOU SHALT REMAIN ON THE STAGE AND CARRY FORTH THE TITLE OF {active_title}\n")
                    league_standing[new_opponent] = 0
                    change_opponent=True
            else:
                league_standing[new_opponent] = 0
                last_title = active_title if active_title != " " else last_title
                change_opponent = True
                if multiplier == 1.0:
                    print(outcome["first_defeat"])
                    active_title = " "
                else:
                    print(outcome["sustained_defeat"])
                    active_title = " 'Nouveau Peasant' "
                    print("All was for nought... time to forgo your glory")
                multiplier = 1.0


            next_round = input("Type 'q' to quit, anything else to continue >>> ").lower().strip()
            print("")
            print(league_standing)
            if next_round == "q":
                player_score = 0.0

                multiplier = 1.0
                multiplier_record = 1.0

                strike = 0

                active_title = " "
                last_title = "*none_on_record*"
                league_standing={}

                change_opponent = True
                break

