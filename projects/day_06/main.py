import os
import math
import random
import copy
from game_data import *

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

rows += 2
columns += 2


def escape_maze():
    escaped = False

    # create maze
    test_maze = create_maze(10, 10)
    exit_row, exit_column = create_maze_exit(10, 10)
    test_maze[exit_row][exit_column] = "EXIT!"
    final_maze = add_obstacles(10, 10, exit_row, exit_column, 15, test_maze)

    # starting position
    robot_current_r, robot_current_c, final_maze = spawn_robot(10, 10, exit_row, exit_column, final_maze)
    # restart prep
    clean_maze = copy.deepcopy(final_maze)
    restart_robot_current_r = robot_current_r
    restart_robot_current_c = robot_current_c
    while not escaped:
        os.system("cls" if os.name == "nt" else "clear")
        for row in final_maze:
            print(" ".join(row))
        while True:
            print("\nIf you want to quit type 'q'; type 'r' to restart the level")
            movement_direction = input("Where do you want to go? [w/a/s/d] >>> ")
            print("")
            if movement_direction in ["w", "a", "s", "d"]:
                robot_current_r, robot_current_c, escaped = robot_move(robot_current_r, robot_current_c, final_maze,
                                                                       movement_direction)
                break
            elif movement_direction == "q":
                print("\nHA! You remain stuck!\n")
                escaped = True
                break
            elif movement_direction == "r":
                print("\nFine, give it another go...\n")
                final_maze = copy.deepcopy(clean_maze)
                robot_current_r = restart_robot_current_r
                robot_current_c = restart_robot_current_c
                break
            else:
                print("\nThe robot can only move up, down, left or right")


escape_maze()
