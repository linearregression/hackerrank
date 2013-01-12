#!/usr/bin/python
# Head ends here
import collections

def next_move(posx, posy, board):
    # Split method for testing
    print decide_move(posx, posy, board)


def decide_move(posx, posy, board):
    """
    If current cell is dirty, clean it
    Else use BFS to find closest dirty cell to move toward

    queue is used to store neighboring cells
    checked_grid is used to make sure each cell is added to the queue only once
    """

    # Check if on dirty cell
    if board[posx][posy] == "d":
        return "CLEAN"

    current_coordinates = (posx, posy)
    queue =  collections.deque().append(current_coordinates)
    checked_grid = [["-" for i in range(5)] for j in range(5)]
    checked_grid[posx][posy] = "c"
    return determine_next_move(current_coordinates, calculate_target_cell(queue, checked_grid))

def calculate_target_cell(queue, grid):
    if len(queue) == 0:
        return "DONE"

    current_coordinates = queue.popleft()
    if board[current_coordinates[0]][current_coordinates[1]] == "d":
        return current_coordinates
    # Enqueue neighboring cells
    else:
        queue.extend(find_existing_neighbors(current_coordinates, grid))

    return calculate_target_cell(queue, grid)


def find_existing_neighbors(coordinates, grid):
    """
    Add neighboring cells of coordinates if applicable and mark as checked on the grid
    """

    neighbors = []
    newcoordinates = (coordinates[0], coordinates[1]+1)
    if check_coordinates(newcoordinates, grid):
        neighbors.append(newcoordinates)
        grid[newcoordinates[0]][newcoordinates[1]] = "c"
    newcoordinates = (coordinates[0], coordinates[1]-1)
    if check_coordinates(newcoordinates, grid):
        neighbors.append(newcoordinates)
        grid[newcoordinates[0]][newcoordinates[1]] = "c"
    newcoordinates = (coordinates[0]+1, coordinates[1])
    if check_coordinates(newcoordinates, grid):
        neighbors.append(newcoordinates)
        grid[newcoordinates[0]][newcoordinates[1]] = "c"
    newcoordinates = (coordinates[0]-1, coordinates[1])
    if check_coordinates(newcoordinates, grid):
        neighbors.append(newcoordinates)
        grid[newcoordinates[0]][newcoordinates[1]] = "c"

    return neighbors

def check_coordinates(coordinates, grid):
    """
    Check if coordinates are on 5x5 board and that they are not already in the queue
    """

    return 0 <= coordinates[0] <= 4 and 4 >= coordinates[1] >= 0 and grid[coordinates[0]][coordinates[1]] == "-"

def determine_next_move(current_coordinates, destination_coordinates):
    if destination_coordinates[1] - current_coordinates[1] > 0:
        return "RIGHT"
    elif destination_coordinates[1] - current_coordinates[1] < 0:
        return "LEFT"
    elif destination_coordinates[0] - current_coordinates[0] > 0:
        return "DOWN"
    elif destination_coordinates[0] - current_coordinates[0] < 0:
        return "UP"
    else:
        return "ERROR"


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
