import os
import math
import random
from game_data import *

rows = None
columns = None


def escape_maze():
    escaped = False
    # create maze
    test_maze = create_maze(10, 10)
    exit_row, exit_column = create_maze_exit(10, 10)
    test_maze[exit_row][exit_column] = "EXIT!"
    final_maze = add_obstacles(10, 10, exit_row, exit_column, 15, test_maze)

    # starting position
    robot_current_r, robot_current_c, final_maze = spawn_robot(10, 10, exit_row, exit_column, final_maze)

    while not escaped:
        os.system("cls" if os.name == "nt" else "clear")
        for row in final_maze:
            print("".join(row))
        while True:
            movement_direction = input("\nWhere do you want to go? [w/a/s/d] >>> ")
            print("")
            if movement_direction in ["w", "a", "s", "d"]:
                break
            else:
                print("The robot can only move up, down, left or right")

        robot_current_r, robot_current_c, escaped = robot_move(robot_current_r, robot_current_c, final_maze,
                                                               movement_direction)


escape_maze()
