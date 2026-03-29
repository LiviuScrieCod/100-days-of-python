import os
import math
import random
import copy
from game_data import *

game_on = True
session_highscore = 0


def load_highscore():
    if not os.path.exists("highscore.txt"):
        return []
    scores = []
    try:
        with open("highscore.txt", "r") as f:
            for line in f.readlines():
                clean_line = line.strip()
                if "," in clean_line:
                    name, score = clean_line.split(",")
                    scores.append({"name": name, "score": int(score)})
        return sorted(scores, key=lambda x: x["score"], reverse=True)[:10]
    except (ValueError, IOError):
        return []


def escape_maze():
    escaped = False
    sprung_traps = 0

    # create maze
    test_maze = create_maze(rows, columns)
    exit_row, exit_column = create_maze_exit(rows, columns)
    test_maze[exit_row][exit_column] = "EXIT!"
    final_maze = add_obstacles(rows, columns, exit_row, exit_column, obstacle_density, test_maze)

    # starting position
    robot_current_r, robot_current_c, final_maze, battery = spawn_robot(rows, columns, exit_row, exit_column,
                                                                        final_maze)

    # restart prep
    clean_maze = copy.deepcopy(final_maze)
    restart_robot_current_r = robot_current_r
    restart_robot_current_c = robot_current_c
    restart_battery = battery
    no_sprung_traps = 0

    def restart_game(clean_maze, restart_robot_current_r, restart_robot_current_c, restart_battery, no_sprung_traps):
        print(f"\n🔋 REBOOTING... Energy restored to: {restart_battery} units\n")
        return restart_robot_current_r, restart_robot_current_c, copy.deepcopy(
            clean_maze), restart_battery, no_sprung_traps

    while not escaped:
        os.system("cls" if os.name == "nt" else "clear")
        for row in final_maze:
            print(" ".join(row))
        print(f"\n🔋 REMAINING ENERGY: {battery if battery >= 0 else 0} units\n")
        if battery <= 0:
            print("Your robot ran out of juice... GAME OVER!")
            print("Your score is 0!")
            while True:
                restart = input("Try again? [y/n] >>> ").strip().lower()
                if restart == "y":
                    robot_current_r, robot_current_c, final_maze, battery, sprung_traps = restart_game(clean_maze,
                                                                                                       restart_robot_current_r,
                                                                                                       restart_robot_current_c,
                                                                                                       restart_battery,
                                                                                                       no_sprung_traps)
                    break
                elif restart not in ["y", "n"]:
                    print("Not an option")
                elif restart == "n":
                    escaped = True
                    break
            continue
        while True:
            print("\nIf you want to quit type 'q'; type 'r' to restart the level")
            movement_direction = input("Where do you want to go? [w/a/s/d] >>> ").strip().lower()
            print("")
            if movement_direction in ["w", "a", "s", "d"]:
                robot_current_r, robot_current_c, escaped, battery_cost = robot_move(robot_current_r, robot_current_c,
                                                                                     final_maze,
                                                                                     movement_direction)
                battery -= battery_cost
                if final_maze[robot_current_r][robot_current_c] == maze_art['sprung_trap']:
                    sprung_traps += 1
                if escaped:
                    os.system("cls" if os.name == "nt" else "clear")
                    area_score = (rows - 2) * (columns - 2)
                    energy_score = battery * 10
                    trap_penalty = sprung_traps * 50
                    global session_highscore

                    for row in final_maze:
                        print(" ".join(row))

                    total_score = max(0, area_score + energy_score - trap_penalty)
                    print(f"Area points: {area_score}")
                    print(f"Energy points: {energy_score}")
                    print(f"Trap penalty: -{trap_penalty}")
                    print(f"Final score: {total_score}")

                    global top_10
                    if total_score > session_highscore:
                        session_highscore = total_score
                        print(f"New session high score: {session_highscore}")
                        if len(top_10) < 10 or session_highscore > top_10[len(top_10) - 1]['score']:
                            player_name = input("You are worthy of the hall of fame. What is your name? >>> ").strip(

                            ).upper()[:7]
                            top_10.append({'name': player_name, 'score': session_highscore})
                            top_10 = sorted(top_10, key=lambda x: x["score"], reverse=True)[:10]

                            try:
                                with open("highscore.txt", "w") as f:
                                    for entry in top_10:
                                        f.write(f"{entry['name']},{entry['score']}\n")
                                print("Scoreboard updated!")
                            except IOError:
                                print("Something went wrong... unable to save new data.")
                                print("Make sure the record file is closed, you have write permission or the HDD has "
                                      "available space on it!")
                    break
                break
            elif movement_direction == "q":
                print("\nHA! You remain stuck!\n")
                escaped = True
                break
            elif movement_direction == "r":
                print("\nFine, give it another go...\n")
                robot_current_r, robot_current_c, final_maze, battery, sprung_traps = restart_game(clean_maze,
                                                                                                   restart_robot_current_r,
                                                                                                   restart_robot_current_c,
                                                                                                   restart_battery,
                                                                                                   no_sprung_traps)
                break
            else:
                print("\nThe robot can only move up, down, left or right")


top_10 = load_highscore()
while game_on:
    extra_break = False
    print("Welcome to the Discounted Game of Labyrinthine adventuring - graphics somewhat included\n")
    print("[1] Play")
    print("[2] Hall of Fame")
    print("[3] Exit")
    game_menu_choice = input("Select an option >>> ")

    if game_menu_choice == "3":
        break
    elif game_menu_choice == "2":
        os.system("cls" if os.name == "nt" else "clear")

        if not top_10:
            print("Perhaps you'll be the first to escape!")
        else:
            width = 30
            print("\n" + "=" * width)
            print("HALL OF FAME".center(width))
            print("=" * width)

            for i, entry in enumerate(top_10):
                nr = i + 1
                name = entry['name']
                score = entry['score']
                print(f"{nr:>2}. {name:<7} -------- {score:>9}")
            print("=" * width)
        input("\nPress any key to return to the main menu...")
        continue
    elif game_menu_choice == "1":
        while True:
            print(f"Highscore: {session_highscore}")
            while True:
                try:
                    rows = int(input("\nHow many rows should the labyrinth have? digits only: >>> "))
                    if rows < 5:
                        print("\nToo small! Make it at least 6 by 6!")
                        continue
                    break
                except ValueError:
                    print("Digits only!")

            while True:
                try:
                    columns = int(input("How many columns should the labyrinth have? digits only: >>> "))
                    if columns < 5:
                        print("\nToo small! Make it at least 6 by 6!")
                        continue
                    break
                except ValueError:
                    print("Digits only!")

            while True:
                try:
                    obstacle_density = int(input("What obstacle density do you want (15-30%)? >>> "))
                    if 15 <= obstacle_density <= 30:
                        break
                    print("\nKeep it between 15 and 30")
                except ValueError:
                    print("Digits only!")

            rows += 2
            columns += 2

            escape_maze()

            while True:
                play_again = input("Play again? [y/n] >>> ")
                if play_again not in ["y", "n"]:
                    print("Didn't quite get that...")
                elif play_again == "n":
                    print("Run along home now...")
                    game_on = False
                    extra_break = True
                    break
                elif play_again == "y":
                    break
            if extra_break:
                break
    else:
        print("Will be available in a DLC, TBR in 2028")
