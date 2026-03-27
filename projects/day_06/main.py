import os
import math
import random
import copy
from game_data import *

game_on = True


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
            print(f"You sprung {sprung_traps} traps")
            while True:
                restart = input("Try again? [y/n] >>> ")
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
            movement_direction = input("Where do you want to go? [w/a/s/d] >>> ")
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
                    for row in final_maze:
                        print(" ".join(row))
                    print(f"You sprung {sprung_traps} traps")
                    # exit_game = input("Press any key to exit the game >>> ")
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


while game_on:
    print("Welcome to Discounted Game of Labyrinthine adventure - graphics not included\n")
    while True:
        try:
            rows = int(input("How many rows should the labyrinth have? digits only: >>> "))
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
            print("Run along...")
            game_on = False
            break
        elif play_again == "y":
            break
