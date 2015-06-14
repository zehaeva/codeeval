'''
    The game of life
'''
import sys

size = 0

def iterate(my_grid, size):
    new_grid = [[0 for i in range(size)] for i in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            live_neighbors = 0

            try:
                if ((i-1) >= 0):
                    check_up = True
                else:
                    check_up = False
                if ((i+1) < size):
                    check_down = True
                else:
                    check_down = False
                if ((j+1) < size):
                    check_right = True
                else:
                    check_right = False
                if ((j-1) >= 0):
                    check_left = True
                else:
                    check_left = False

                if check_left:
                    if my_grid[i][j-1] == 1:#left
                        live_neighbors += 1
                    if check_down:
                        if my_grid[i-1][j-1] == 1:#left down
                            live_neighbors += 1
                    if check_up:
                        if my_grid[i+1][j-1] == 1:#left up
                            live_neighbors += 1
                if check_right:
                    if my_grid[i][j+1] == 1:#right
                        live_neighbors += 1
                    if check_down:
                        if my_grid[i-1][j+1] == 1:#right down
                            live_neighbors += 1
                    if check_up:
                        if my_grid[i+1][j+1] == 1:#right up
                            live_neighbors += 1
                if check_up:
                    if my_grid[i-1][j] == 1:#up
                        live_neighbors += 1
                if check_down:
                    if my_grid[i+1][j] == 1:#down
                        live_neighbors += 1
            except:
                print ('size: {} i: {} j: {}'.format(size, i, j))

            if live_neighbors < 2 or live_neighbors > 3:
                new_grid[i][j] = 0
            if live_neighbors == 3:
                new_grid[i][j] = 1
            if live_neighbors == 2:
                new_grid[i][j] = my_grid[i][j]

    return new_grid

def print_grid(grid):
    for x in grid:
        for y in x:
            if y == 0:
                sys.stdout.write('.')
            else:
                sys.stdout.write('*')
        print('')

test_cases = open(sys.argv[1], 'r')

grid = []
for test in test_cases:
    row = []
    for x in test:
        if x == '.':
            row.append(0)
        else:
            row.append(1)
    grid.append(row)

test_cases.close()

size = len(grid[0])

for i in range(3):
    grid = iterate(grid, size)
print_grid(grid)
