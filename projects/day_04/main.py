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
print("Welcome to the 1978 Rock Paper Scissors Olympics!\n")

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
    # 1. Survival Mode
    # 1. TODO: Remove cheating/testing prints before push!
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
    elif choose_game_type == "k":
        # TODO:
        # 1: Infrastructura și Tragerea la Sorți
        # 1.1. Duplicate participants: Crearea unei liste temporare cu toți cei 15 oponenți disponibili (fără a strica lista originală din game_data.py).
        tournament_roster = [opponent[0] for opponent in random_opponents[:]]
        # 1.2. The Big Draw: Amestecarea listei și felierea ei în 4 Grupe (A, B, C, D) a câte 4 jucători.
        random.shuffle(tournament_roster)
        print(tournament_roster)
        tournament_draw = tournament_roster[:]
        tournament_draw.insert(random.randint(0,15), " ".join(player_name))

        groups = {}
        group_names = "ABCD"

        for letter in group_names:
            groups[letter] = []
            for _ in range(4):
                contestant = tournament_draw.pop()
                groups[letter].append(contestant)

        # Identify player group
        player_group = ""
        for letter, group in groups.items():
            if player_name in group:
                player_group = letter

        print(f"{player_name} is in group {player_group}")

        # 1.3. The Score Templates: Definirea listei de 9 scenarii de punctaj valide matematic pentru simularea grupelor de boți.

        # 2 Grupa A (Meciurile Tale)
        # 2.3. Group Stage Loop: Inițializarea unui ciclu de 3 meciuri (fiecare cu un oponent diferit din Grupa A).
        # 2.2. RPS Logic (1-Hand): Implementarea logicii de joc (Piatră-Foarfecă-Hârtie) pentru o singură mână (Victorie=3p, Egal=1p, Înfrângere=0p).
        # 2.1. Scoreboard Update: Afișarea punctajului tău după fiecare meci.

        # 3 Simularea Mondială (News Feed)
        # 3.1. Asignarea random a template-urilor de scor pentru grupele B, C și D.
        # 3.2. Generarea unor punctaje plauzibile pentru ceilalți 3 colegi de grupă (asigurând calificarea protagonistului dacă are ≥4 puncte).
        # 3.3. Afișarea tabelelor finale ale tuturor grupelor și anunțarea celor 8 calificați în Sferturi.

        # 4 Sferturi și Semifinale (Eliminatorii)
        # 4.1. Best of 3 Engine: Modificarea logicii de joc pentru a necesita 2 victorii din 3 mâini pentru a trece mai departe.
        # 4.2. Generarea automată a câștigătorilor dintre boți folosind random.choice și afișarea unor „știri dramatice” despre masacrul din celelalte meciuri.
        # 4.3. The Rock Eater Bias: Implementarea șansei de 75% pentru anumite alegeri (Piatră/Foarfecă/Hârtie) la boșii din etapele superioare.

        # 5 Finala și Epilogul (The Twist)
        # 5.1. Anunțarea finalei și execuția momentului în care AI-ul calificat îi „cedează” locul lui Mr. CHEATer.
        # 5.2. Programarea lui Mr. CHEATer să aleagă mereu mutarea care bate jucătorul (ai = (player + 1) % 3).
        # 5.3. Implementarea comenzii secrete "cheat" care ignoră logica clasică și îi aduce victoria jucătorului.
        # 5.4. Afișarea epilogului dramatic și întoarcerea la meniul principal.
        break
