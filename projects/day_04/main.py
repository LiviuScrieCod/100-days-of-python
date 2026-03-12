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
        # create contestants list
        tournament_roster = [opponent[0] for opponent in random_opponents[:]]
        random.shuffle(tournament_roster)
        # print(tournament_roster)
        tournament_draw = tournament_roster[:]
        tournament_player_name = " ".join(player_name)
        tournament_draw.insert(random.randint(0,15), tournament_player_name)

        # print(tournament_draw)

        groups = {}
        group_names = "ABCD"
        bot_groups_standings = random.sample(group_standings, 3)
        # print(bot_groups_standings)

        for letter in group_names:
            groups[letter] = []
            for bot_data in range(4):
                pop_index = random.randint(0,len(tournament_draw)-1)
                contestant = tournament_draw.pop(pop_index)
                groups[letter].append([contestant, 0])
            # print(groups[letter])

        # Identify player group
        player_group = ""
        for letter, group in groups.items():
            if any(contestant[0]==tournament_player_name for contestant in group):
                player_group = letter
                break
        non_player_groups = [g for g in groups if g != player_group]
        # print(groups)
        # print(f"{tournament_player_name} is in group {player_group}")

        player_group_bots = [bot for bot in groups[player_group] if bot[0]!=tournament_player_name]
        for i in range(4):
            if groups[player_group][i][0]==tournament_player_name:
                tournament_player_index = i
                break
        tournament_player_group_score = groups[player_group][tournament_player_index][1]

        # tournament_player_score = 0
        # bot_score = 0

        print("Welcome to the 1978 Rock Paper Scissors Olympics!\n")
        time.sleep(0.7)
        print(
            f"It's the group stage and the first match of the {player_group} group is {tournament_player_name} vs {player_group_bots[0][0]}")
        time.sleep(1)
        for index, bot_data in enumerate(player_group_bots):
            bot_name = bot_data[0]
            print(utility["delimiter"])
            print("The contestants are ready to go!")
            tournament_player_choice = input(
                "Contestants, choose your weapon!\n['rock', 'paper' or 'scissors'? (q to wuss out of it)] >>> ").strip().lower()
            if tournament_player_choice == "q":
                print("\nEXTRA, EXTRA, READ ALL ABOUT IT!")
                print(f"{tournament_player_name} buckled under the pressure and ran off into the crowd! Shame is forever theirs!")
                print("Tune in tomorrow for the finals!")
                break
            elif tournament_player_choice not in valid_moves:
                print(f"\nI don't know what happened there, but the referee will have none of it")
                time.sleep(0.7)
                print(f"{tournament_player_name} was disqualified and lost the match")
                time.sleep(0.7)
                print(f"'{tournament_player_choice}' is not a valid move! Focus, {tournament_player_name}!\n")
                time.sleep(0.7)
                bot_data[1] += 3
                continue
            time.sleep(0.5)
            print("ROCK!")
            time.sleep(0.5)
            print("PAPER!")
            time.sleep(0.5)
            print("SCISSORS!")
            time.sleep(0.5)
            print("GO!")
            time.sleep(1)
            tournament_player_choice = valid_moves.index(tournament_player_choice)
            bot_choice = random.randrange(len(valid_moves))
            print(f"{tournament_player_name} picks: {basic_choices[tournament_player_choice]}")
            print(f"opponent picks: {basic_choices[bot_choice]}")
            if tournament_player_choice == bot_choice:
                print("A draw! Not great, not terrible, but we're still in the group stage, these contestants still have a shot at the title!")
                tournament_player_group_score+=1
                bot_data[1]+=1
            elif (tournament_player_choice-bot_choice) % 3 == 1:
                print(f"{tournament_player_name} wins this round! One step closer to winning the Olympics!")
                tournament_player_group_score += 3
            else:
                print(f"Things are not going well for {tournament_player_name}! Let's hope recovery is still possible!")
                bot_data[1] += 3

            next_match = input("Type 'q' to quit, anything else to continue >>> ").lower().strip()
            if next_match == "q":
                print("\nNobody remembers a quitter...")
                break

            if index < 2:
                print(f"Get ready for the next match of the first match of the {player_group} group: {tournament_player_name} vs {player_group_bots[index+1][0]}")
            else:
                print("And that was the last match of the group! What a great show!")
                print("Let's see who qualified for the next stage!")
            time.sleep(0.7)

        groups[player_group][tournament_player_index][1] = tournament_player_group_score

        print(player_group_bots)
        for i in range(len(player_group_bots)):
            for j in range(i+1, len(player_group_bots)):
                bot1 = player_group_bots[i]
                bot2 = player_group_bots[j]
                print(f"{bot1[0]} vs {bot2[0]}")
                result = random.choice(['bot1', 'bot2', 'draw'])
                if result == 'bot1':
                    bot1[1]+=3
                elif result == 'bot2':
                    bot2[1]+=3
                else:
                    bot1[1] += 1
                    bot2[1] += 1

        print(groups[player_group])
        groups[player_group].sort(key=lambda x:(x[1], x[0] == tournament_player_name), reverse=True)

        for i, letter in enumerate(non_player_groups):
            current_group = groups[letter]
            standings = bot_groups_standings[i]
            for j in range(4):
                current_group[j][1] = standings[j]

        for letter, group in groups.items():
            print(f"\nGroup {letter} standings:")
            for member in group:
                print(f"{member[0]} --- {member[1]}")

        tournament_player_score = 0
        bot_score = 0
        qualifiers_list_permanent = []
        qualifiers_list_temp=[]

        for letter in group_names:
            winner = groups[letter][0][0]
            runner_up = groups[letter][1][0]
            qualifiers_list_permanent.append(winner)
            qualifiers_list_permanent.append(runner_up)

        print(qualifiers_list_permanent)
        random.shuffle(qualifiers_list_permanent)

        olympics_round = ["Finals","Semi-final","Quarter-finals"]
        print(utility["delimiter"])
        print("And we're back! 8 Contestants remaining and only one gold medal. Who will be the 1978 Rock Paper Scissors champion?")
        while len(qualifiers_list_permanent) > 2:
            while len(qualifiers_list_permanent)> 1:
                player1 = qualifiers_list_permanent.pop(random.randrange(len(qualifiers_list_permanent)))
                player2 = qualifiers_list_permanent.pop(random.randrange(len(qualifiers_list_permanent)))

                if tournament_player_name in [player1, player2]:
                    match_duo = [player1, player2]
                    match_duo.remove(tournament_player_name)
                    bot_opponent = match_duo[0]
                    print(f"{tournament_player_name} is on stage! One of the matches of the {olympics_round[len(olympics_round)-1]} is about to begin")
                    print(f"Which of these two has the mental fortitude to obliterate their opponent?")
                    while tournament_player_score<2 and bot_score<2:
                        tournament_player_choice = input(
                            "Contestants, choose your weapon!\n['rock', 'paper' or 'scissors'? (q to wuss out of it)] >>> ").strip().lower()
                        if tournament_player_choice == "q":
                            print("\nEXTRA, EXTRA, READ ALL ABOUT IT!")
                            print(
                                f"{tournament_player_name} buckled under the pressure and ran off into the crowd! Shame is forever theirs!")
                            print("Tune in tomorrow for the finals!")
                            break
                        elif tournament_player_choice not in valid_moves:
                            print(f"\nThis is far too important to mess around! Do it again and do it right!")
                            continue
                        time.sleep(0.5)
                        print("ROCK!")
                        time.sleep(0.5)
                        print("PAPER!")
                        time.sleep(0.5)
                        print("SCISSORS!")
                        time.sleep(0.5)
                        print("GO!")
                        time.sleep(1)
                        tournament_player_choice = valid_moves.index(tournament_player_choice)
                        bot_choice = random.randrange(len(valid_moves))
                        print(f"{tournament_player_name} picks: {basic_choices[tournament_player_choice]}")
                        print(f"opponent picks: {basic_choices[bot_choice]}")
                        if tournament_player_choice == bot_choice:
                            print(
                                "A draw! A draw?! Booooooooo!")
                        elif (tournament_player_choice - bot_choice) % 3 == 1:
                            print(f"{tournament_player_name} wins this round! One step closer to winning the Olympics!")
                            tournament_player_score += 1
                        else:
                            print(
                                f"Things are not going well for {tournament_player_name}! Let's hope recovery is still possible!")
                            bot_score += 1

                        next_match = input("Type 'q' to quit, anything else to continue >>> ").lower().strip()
                        if next_match == "q":
                            print("\nNobody remembers a quitter...")
                            break
                    if tournament_player_score == 2:
                        print(f"QUALIFIED! {tournament_player_name} has what it takes to move to the next roung!")
                        print("We'll be back after commercials")
                        qualifiers_list_temp.append(tournament_player_name)
                    elif bot_score == 2:
                        print("You don't always get what you want...")
                        print(f"As {tournament_player_name} walks towards the lockers room, fans of {bot_opponent} rush to the stage to congratulate their hero!")
                        qualifiers_list_temp.append(bot_opponent)
                else:
                    for _ in range(3):
                        stage_winner = random.choice([player1, player2])
                        print(f"WOW! Did you see that?! {stage_winner}'s hands are unstoppable!")
                    qualifiers_list_temp.append(stage_winner)

                tournament_player_score=0
                bot_score=0
            print(utility["delimiter"])
            if len(olympics_round)>1:
                print(f"We are back and the {olympics_round[len(olympics_round) - 1]} are about to start!")
            qualifiers_list_permanent = qualifiers_list_temp[:]
            qualifiers_list_temp = []
            olympics_round.pop()
    break
