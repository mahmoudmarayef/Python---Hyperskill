a = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def update_grid(coordinates, char):
    global a
    x, y = coordinates
    a[x][y] = char


def print_grid(grid):
    print('---------')
    print('|', grid[0][0], grid[0][1], grid[0][2], '|')
    print('|', grid[1][0], grid[1][1], grid[1][2], '|')
    print('|', grid[2][0], grid[2][1], grid[2][2], '|')
    print('---------')


def check_cell_empty(coordinates):
    x, y = coordinates
    if a[x][y] == ' ':
        return True
    else:
        return False


def check_inside_grid(coordinates):
    if coordinates[0] in range(0,3) and coordinates[1] in range(0,3):
        return True
    else:
        return False


print_grid(a)

player_move = "O"
moves = 0
while True:
    try:
        coordinates = [int(a) - 1 for a in input().split()]
    except ValueError:
        print('You should enter numbers!')
        continue
    else:
        if not check_inside_grid(coordinates):
            print('Coordinates should be from 1 to 3!')
            continue
        elif not check_cell_empty(coordinates):
            print('This cell is occupied! Choose another one!')
            continue
        else:
            if player_move == "O":
                player_move = "X"
            else:
                player_move = "O"
            update_grid(coordinates, player_move)
            moves += 1
            print_grid(a)
            if a[0][0] == "X" and a[0][1] == "X" and a[0][2] == "X":
                print("X wins")
                break
            elif a[1][0] == "X" and a[1][1] == "X" and a[1][2] == "X":
                print("X wins")
                break
            elif a[2][0] == "X" and a[2][1] == "X" and a[2][2] == "X":
                print("X wins")
                break
            elif a[0][0] == "X" and a[1][1] == "X" and a[2][2] == "X":
                print("X wins")
                break
            elif a[0][2] == "X" and a[1][1] == "X" and a[2][0] == "X":
                print("X wins")
                break
            elif a[0][0] == "O" and a[0][1] == "O" and a[0][2] == "O":
                print("O wins")
                break
            elif a[1][0] == "O" and a[1][1] == "O" and a[1][2] == "O":
                print("O wins")
                break
            elif a[2][0] == "O" and a[2][1] == "O" and a[2][2] == "O":
                print("O wins")
                break
            elif a[0][0] == "O" and a[1][1] == "O" and a[2][2] == "O":
                print("O wins")
                break
            elif a[0][2] == "O" and a[1][1] == "O" and a[2][0] == "O":
                print("O wins")
                break
            elif moves >= 9:
                print("Draw")
                break
            continue
