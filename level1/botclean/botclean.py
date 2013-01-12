#!/usr/bin/python
# Head ends here
import collections

def next_move(posx, posy, board):
    # Split method for testing
    print decide_move(posx, posy, board)


def decide_move(posx, posy, board):
    # Check if on dirty cell
    if board[posx][posy] == "d":
        return "CLEAN"

    current_coordinates = (posx, posy)
    return determine_next_move(current_coordinates, calculate_target_cell(collections.deque().append(current_coordinates)))

def calculate_target_cell(queue):
    current_coordinates = queue.popleft()
    if board[current_coordinates[0]][current_coordinates[1]] == "d":
        return current_coordinates
    # Enqueue neighboring cells
    else:
        for next_coordinates in find_existing_neighbors(current_coordinates):
            queue.append(next_coordinates)

    return calculate_target_cell(queue)

# Finds neighbors assuming 5x5 board
def find_existing_neighbors(coordinates):
    neighbors = []
    newcoordinates = (coordinates[0], coordinates[1]+1)
    if check_coordinates(newcoordinates):
        neighbors.append(newcoordinates)
    newcoordinates = (coordinates[0], coordinates[1]-1)
    if check_coordinates(newcoordinates):
        neighbors.append(newcoordinates)
    newcoordinates = (coordinates[0]+1, coordinates[1])
    if check_coordinates(newcoordinates):
        neighbors.append(newcoordinates)
    newcoordinates = (coordinates[0]-1, coordinates[1])
    if check_coordinates(newcoordinates):
        neighbors.append(newcoordinates)

    return neighbors

def check_coordinates(coordinates):
    return 0 <= coordinates[0] <= 4 and 0 <= coordinates[1] <= 4

def determine_next_move(current_coordinates, destination_coordinates):
    if destination_coordinates[0] - current_coordinates[0] > 0:
        return "RIGHT"
    elif destination_coordinates[0] - current_coordinates[0] < 0:
        return "LEFT"
    elif destination_coordinates[1] - current_coordinates[1] > 0:
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
