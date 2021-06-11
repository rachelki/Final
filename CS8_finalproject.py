#Rachel Ki, CS 8 (S21)
import copy


def read_configuration(filename):
    '''
    input param: a file with a grid
    return: a nested list (2D grid) on the input of a file
    For the provided file, it returns a nested list
    '''

    file = open(filename, 'r')

    listname = []
    fileline = file.readline()

    while fileline:
        filerow = fileline.split()
        listname.append(filerow)
        fileline = file.readline()

    return listname


def vampirize(grid, position):
    '''
    input param: grid and position as a tuple.
    return: a new grid based on the input grid and position
    For the provided position, it updates all adjacent cells (up,down,left,right) in the grid to be 1.
    '''

    new_grid = copy.deepcopy(grid)  # make a copy of the provided grid for updates
    r = position[0]  # row
    c = position[1]  # column

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return grid
    if (r < 0) or (r >= len(grid)) or (c < 0) or (c >= len(grid[0])):  # handle position coordinates(U,D,L,R)
        return None

    # changing human into vampire from the entered position (up/down/left/right)
    if ((r - 1) >= 0) and (new_grid[r - 1][c] == 0):  # up
        new_grid[r - 1][c] = 1
    if ((r + 1) < len(grid)) and (new_grid[r + 1][c] == 0):  # down
        new_grid[r + 1][c] = 1
    if ((c - 1) >= 0) and (new_grid[r][c - 1] == 0):  # left
        new_grid[r][c - 1] = 1
    if ((c + 1) < len(grid[0])) and (new_grid[r][c + 1] == 0):  # right
        new_grid[r][c + 1] = 1
    return new_grid

def next_day(grid):
    '''
    input param: 2D grid of city.
    return: a new 2D grid representing the state of the city next day.
    '''

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return grid
    new_grid = copy.deepcopy(grid)  # make a copy of the provided grid for updates
    # vampirization done by cells with vampires.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):  # cells with vampires.
                p = (i, j)
                new_grid = vampirize(new_grid, p)  # doing the vampirization
    return new_grid

def show_city_each_day(grid, num_day):
    '''
    input param: 2D grid of city, and number of day.
    return: number of day or -1 for the empty grid.
    Display H:human, V:vampire, W:wall, P:healer
    '''

    if (len(grid) < 1):  # handle empty grid
        return -1
    print("Day " + str(num_day) + ":")  # print number of day
    for r in range(len(grid)):
        print("")
        # display in chars.
        for c in range(len(grid[r])):
            if (grid[r][c]) == 0:  # human
                print("H", end=' ')
            elif (grid[r][c]) == 1:  # vampire
                print("V", end=' ')
            elif (grid[r][c]) == 2:  # wall
                print("W", end=' ')
            elif (grid[r][c]) == 3:  # healer
                print("P", end=' ')
    print("")  # for displaying correct format
    print("")  # for displaying correct format
    return num_day

def cure(grid, position):
    '''
    input param: 2D grid of city, and position as a tuple.
    return: a new grid or -1 for the empty grid or -1 for single list or None for outside.
    Updates all adjacent cells as well as diagonals in the grid to be 0.
    '''

    new_grid = copy.deepcopy(grid)  # make a copy of the provided grid for updates
    r = position[0]  # row
    c = position[1]  # column

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return -1
    if (r < 0) or (r >= len(grid)) or (c < 0) or (c >= len(grid[0])):  # handle position coordinates(U,D,L,R)
        return None
    if ((r - 1) >= 0) and (new_grid[r - 1][c] == 1):  # up
        new_grid[r - 1][c] = 0
    if ((r + 1) < len(grid)) and (new_grid[r + 1][c] == 1):  # down
        new_grid[r + 1][c] = 0
    if ((c - 1) >= 0) and (new_grid[r][c - 1] == 1):  # left
        new_grid[r][c - 1] = 0
    if ((c + 1) < len(grid[0])) and (new_grid[r][c + 1] == 1):  # right
        new_grid[r][c + 1] = 0
    if ((r - 1) >= 0) and ((c - 1) >= 0) and (new_grid[r - 1][c - 1] == 1):  # upper left
        new_grid[r - 1][c - 1] = 0
    if ((r - 1) >= 0) and ((c + 1) < len(grid)) and (new_grid[r - 1][c + 1] == 1):  # upper right
        new_grid[r - 1][c + 1] = 0
    if ((r + 1) < len(grid)) and ((c - 1) >= 0) and (new_grid[r + 1][c - 1] == 1):  # lower left
        new_grid[r + 1][c - 1] = 0
    if ((r + 1) < len(grid)) and ((c + 1) < len(grid[0])) and (new_grid[r + 1][c + 1] == 1):  # lower right
        new_grid[r + 1][c + 1] = 0
    return new_grid

def days_remaining_1(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    '''

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return -1
    num_day = 0  # the starting day
    show_city_each_day(grid, num_day)  # show the city on day 0

    # make a copy of the original city
    original_grid = copy.deepcopy(grid)
    next_grid = next_day(grid)  # get the city on the next day

    while next_grid != original_grid:
        # keep looping while next day's city is different from today's
        num_day += 1
        show_city_each_day(next_grid, num_day)
        original_grid = copy.deepcopy(next_grid)
        next_grid = next_day(next_grid)
    return num_day

def days_remaining_2(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    The input grid may include 2(Walls) along with 0(Human) and 1(Vampire)
    Otherwise, return -1 (NOT all humans were converted to vampires.)
    '''

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return -1  # return -1 when empty list
    num_day = 0  # the starting day
    all_vampire = True  # default value for No human in the grid.
    show_city_each_day(grid, num_day)  # show the city on day 0

    # make a copy of the original city
    original_grid = copy.deepcopy(grid)
    next_grid = next_day(grid)  # get the city on the next day

    while next_grid != original_grid:
        # keep looping while next day's city is different from today's
        num_day += 1
        show_city_each_day(next_grid, num_day)  # show the city on the next day
        original_grid = copy.deepcopy(next_grid)
        next_grid = next_day(next_grid)  # get the city on the next day

    # checking any human left in the grid
    for r in range(len(next_grid)):
        for c in range(len(next_grid[r])):
            if next_grid[r][c] == 0:
                all_vampire = False

    if all_vampire == True:
        return num_day
    else:
        return -1  # NOT all vampires in the grid

def days_remaining_3(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    The grid may include 3(Healer) along with 2(Walls), 0(Human), and 1(Vampire)
    Otherwise, return -1 (NOT all humans were converted to vampires.)
    '''

    if (len(grid) < 1) or (len(grid[0]) and len(grid) < 2):  # handle empty and single list
        return -1  # return -1 when empty list
    num_day = 0  # the starting day
    all_vampire = True  # default value for No human in the grid.
    show_city_each_day(grid, num_day)  # show the city on day 0

    # make a copy of the original city
    original_grid = copy.deepcopy(grid)
    next_grid = next_day(grid)  # get the city on the next day

    while next_grid != original_grid:
        # keep looping while next day's city is different from today's
        num_day += 1
        show_city_each_day(next_grid, num_day)  # show the city on the next day
        original_grid = copy.deepcopy(next_grid)
        next_grid = next_day(next_grid)  # get the city on the next day
        # calling 'cure' function after the vampirization
        for r in range(len(next_grid)):
            for c in range(len(next_grid[r])):
                if next_grid[r][c] == 3:  # healer position
                    next_grid = cure(next_grid, (r, c))
        # stop after 30 days
        if num_day >= 30:
            return -1  # NOT all vampires in the grid.

    # checking any human left in the grid
    for r in range(len(next_grid)):
        for c in range(len(next_grid[r])):
            if next_grid[r][c] == 0:  # cell with human
                all_vampire = False

    if all_vampire == True:
        return num_day
    else:
        return -1  # NOT all vampires in the grid.
