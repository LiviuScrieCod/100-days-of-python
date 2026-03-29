import random
import math

maze_art = {
    "inner_wall": "#####",
    "outer_wall": "  #  ",
    "trap": "  T  ",
    "exit": "EXIT!",
    "player": ".  R ",
    "player_victory": "!*R*!",
    "clear_path": ".    ",
    "sprung_trap": ". >R<"
}


def create_maze(rows, columns):
    maze = []
    for row_index in range(rows):
        row = []
        if row_index == 0 or row_index == rows - 1:
            for col_index in range(columns):
                row.append(maze_art['outer_wall'])
        else:
            for col_index in range(columns):
                if col_index == 0:
                    row.append(maze_art['outer_wall'])
                elif col_index == columns - 1:
                    row.append(maze_art['outer_wall'])
                else:
                    row.append(maze_art['clear_path'])
        maze.append(row)
    return maze


def create_maze_exit(rows, columns):
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


def add_obstacles(rows, columns, exit_row, exit_column, obstacles_percentage, maze):
    maze_surface = (rows - 2) * (columns - 2)
    obstacles_total = math.ceil(obstacles_percentage / 100 * maze_surface)
    obstacles_counter = 0
    attempts = 0

    while obstacles_counter < obstacles_total:
        if attempts > 500:
            if obstacles_total > 5:
                obstacles_total -= 2
                attempts = 0
                print(f"This maze is way to fun! Getting rid of some obstacles to make it playable!")
            else:
                break

        attempts += 1
        r = random.randint(1, rows - 2)
        c = random.randint(1, columns - 2)

        # check if door
        near_exit = abs(r - exit_row) + abs(c - exit_column)

        if near_exit <= 2:
            continue
        elif maze[r][c] == maze_art['clear_path']:
            trap_or_wall = random.randint(1, 10)
            if trap_or_wall <= 3:
                maze[r][c] = maze_art['trap']
            else:
                maze[r][c] = maze_art['inner_wall']
            obstacles_counter += 1

        if obstacles_counter >= obstacles_total:
            break

    return maze


def spawn_robot(rows, columns, exit_row, exit_column, maze):
    min_dist_from_exit = (rows - 2 + columns - 2) / 3
    battery = math.ceil(min_dist_from_exit + 10)

    while True:
        r = random.randint(1, rows - 2)
        c = random.randint(1, columns - 2)

        if maze[r][c] == maze_art['clear_path']:
            safe_spawn = abs(r - exit_row) + abs(c - exit_column)
            if safe_spawn >= min_dist_from_exit:
                queue = [(r, c)]
                visited = set()
                visited.add((r, c))

                while queue:
                    row_index, column_index = queue.pop(0)

                    if row_index == exit_row and column_index == exit_column:
                        maze[r][c] = maze_art['player']
                        return r, c, maze, battery

                    for next_row, next_column in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        new_row, new_column = row_index + next_row, column_index + next_column
                        if 0 <= new_row < len(maze) and 0 <= new_column < len(maze[0]):
                            if maze[new_row][new_column] not in [maze_art['inner_wall'], maze_art['outer_wall']] and (
                                    new_row,
                                    new_column) not in visited:
                                visited.add((new_row, new_column))
                                queue.append((new_row, new_column))


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

    if destination in [maze_art['inner_wall'], maze_art['outer_wall']]:
        print("\nWalls hurt face!\n")
        return current_row, current_column, False, 0

    if destination == maze_art['trap']:
        print("\nYour foot is stuck in inconvenience!\n")
        maze[current_row][current_column] = maze_art['clear_path']
        maze[new_row][new_column] = maze_art['sprung_trap']
        return new_row, new_column, False, 4

    if destination == maze_art['exit']:
        print("\nCongrats! You made it out!\n")
        maze[current_row][current_column] = maze_art['clear_path']
        maze[new_row][new_column] = maze_art['player_victory']
        return new_row, new_column, True, 1

    if destination == maze_art['clear_path']:
        maze[current_row][current_column] = maze_art['clear_path']
        maze[new_row][new_column] = maze_art['player']
        return new_row, new_column, False, 1

    return current_row, current_column, False, 0
