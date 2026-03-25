import random
import math


# TODO:
# 1.   Generate a maze
def create_maze(rows, columns):
    rows += 2
    columns += 2
    maze = []
    for row_index in range(rows):
        row = []
        if row_index == 0 or row_index == rows - 1:
            for col_index in range(columns):
                row.append('  #  ')
        else:
            for col_index in range(columns):
                if col_index == 0:
                    row.append('  #  ')
                elif col_index == columns - 1:
                    row.append('  #  ')
                else:
                    row.append('.    ')
        maze.append(row)
    return maze


# 1.1. Generate a random maze with an exit (exit at random point)
def create_maze_exit(rows, columns):
    rows += 2
    columns += 2
    walls = ["up", "right", "down", "left"]
    random_wall = random.choice(walls)

    if random_wall == "up":
        r, c = 0, random.randint(1, columns - 2)
    elif random_wall == "right":
        r, c = random.randint(1, rows - 2), columns - 1
    elif random_wall == "down":
        r, c = rows - 1, random.randint(1, columns - 2)
    elif random_wall == "left":
        r, c = random.randint(1, rows - 2), 0

    return r, c


# 1.2. Generate a random maze with random obstacles (dead ends, wall islands etc.)
def add_obstacles(rows, columns, exit_row, exit_column, obstacles_percentage, maze):
    rows += 2
    columns += 2
    maze_surface = rows * columns
    obstacles_total = math.ceil(obstacles_percentage / 100 * maze_surface)
    obstacles_counter = 0

    while obstacles_counter < obstacles_total:
        r = random.randint(1, rows - 2)
        c = random.randint(1, columns - 2)

        # check if door
        near_exit = abs(r - exit_row) + abs(c - exit_column)

        if near_exit <= 2:
            continue
        elif maze[r][c] == ".    ":
            trap_or_wall = random.randint(1, 10)
            if trap_or_wall <= 2:
                maze[r][c] = "  T  "
            else:
                maze[r][c] = "#####"
            obstacles_counter += 1
        else:
            continue

    return maze


# 2.   Spawn robot
# 2.1. Spawn robot at random location in maze
# 2.2. Spawn robot at random location in maze and make sure maze has a solution
def spawn_robot(rows, columns, exit_row, exit_column, maze):
    rows += 2
    columns += 2
    min_dist_from_exit = (rows - 2 + columns - 2) / 3

    while True:
        r = random.randint(1, rows - 2)
        c = random.randint(1, columns - 2)

        if maze[r][c] == ".    ":
            safe_spawn = abs(r - exit_row) + abs(c - exit_column)
            if safe_spawn >= min_dist_from_exit:
                maze[r][c] = ". R  "
                queue = [(r, c)]
                visited = set()
                visited.add((r, c))

                while queue:
                    row_index, column_index = queue.pop(0)

                    if row_index == exit_row and column_index == exit_column:
                        return r, c, maze

                    for next_row, next_column in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        new_row, new_column = row_index + next_row, column_index + next_column
                        if 0 <= new_row < len(maze) and 0 <= new_column < len(maze[0]):
                            if maze[new_row][new_column] not in ["#####", "  #  "] and (new_row,
                                                                                        new_column) not in visited:
                                visited.add((new_row, new_column))
                                queue.append((new_row, new_column))


# 3.   Get robot to move throughout the maze
def robot_move(current_row, current_column, maze, movement_direction):
    new_row, new_column = current_row, current_column
    if movement_direction == "w":
        new_row = current_row - 1
    elif movement_direction == "s":
        new_row = current_row + 1
    elif movement_direction == "a":
        new_column = current_column - 1
    elif movement_direction == "d":
        new_column = current_column + 1

    destination = maze[new_row][new_column]

    if destination in ["  #  ", "#####"]:
        print("\nWalls hurt face!")
        return current_row, current_column, False

    if destination == "  T  ":
        print("\nYour foot is stuck in inconvenience!")
        return new_row, new_column, False

    if destination == "EXIT!":
        print("\nCongrats! You made it out!")
        maze[current_row][current_column] = ".    "
        maze[new_row][new_column] = "  R  "
        return new_row, new_column, True

    if destination == ".    ":
        maze[current_row][current_column] = ".    "
        maze[new_row][new_column] = "  R  "
        return new_row, new_column, False

    return current_row, current_column, False

# 3.1. Create algorithm to allow robot to navigate the maze

# 4.   Implement extra features
# 4.1. Scoreboard
# 4.2. Sounds
# 4.3. Max moves allowed
