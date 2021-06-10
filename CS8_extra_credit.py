#Rachel Ki, CS 8 (S21)

import copy

def seize_cure(grid):
    '''
    input param: 2D grid of city.
    return: True if the healer is surrounded by the vampires on all four sides. Otherwise False.
    Turn the healer into a vampire if all four sides were surrounded by vampires.
    '''

    surrounded = False  # default surrounded value.
    return_val = False  # default return value.
    new_grid = copy.deepcopy(grid)  # make a copy of the provided grid for updates

    # check the healer is surrounded by vampires.
    for r in range(len(new_grid)):
        for c in range(len(new_grid[r])):
            if (new_grid[r][c] == 3): # healer ; need to check up/down/left/right
                surrounded = True
                if ((r - 1) >= 0) and (new_grid[r-1][c] != 1):            #up
                    surrounded = False
                if ((r + 1) < len(new_grid)) and (new_grid[r + 1][c] != 1):    #down
                    surrounded = False
                if ((c - 1) >= 0) and (new_grid[r][c-1] != 1):            #left
                    surrounded = False
                if ((c + 1) < len(new_grid[0])) and (new_grid[r][c+1] != 1):  #right
                    surrounded = False
                if (surrounded == True): # surrounded by vamp. Need to update input grid.
                    new_grid[r][c] = 1
                    return_val = True
    print("new_grid---")
    print_list(new_grid)  # print the new grid for debug
    return return_val


def get_count(new_grid, cnt_item, position, diag=False):
    '''
    input param: 2D grid of city, count item, position as a tuple, default value False for diag.
    return: count of the provided count item in the grid around the position.
    '''

    count = 0  # starting count.
    r = position[0]  # row.
    c = position[1]  # column.

    # check all cells around the position for the item count.
    if ((r - 1) >= 0) and (new_grid[r-1][c] == cnt_item):            #up
        count += 1
    if ((r + 1) < len(new_grid)) and (new_grid[r + 1][c] == cnt_item):    #down
        count += 1
    if ((c - 1) >= 0) and (new_grid[r][c-1] == cnt_item):            #left
        count += 1
    if ((c + 1) < len(new_grid[0])) and (new_grid[r][c+1] == cnt_item):  #right
        count += 1
    if (diag == True):
        if ((r - 1) >= 0) and ((c - 1) >= 0) and (new_grid[r - 1][c - 1] == cnt_item): #upper left
            count += 1
        if ((r - 1) >= 0) and ((c + 1) < len(new_grid[0])) and (new_grid[r - 1][c + 1] == cnt_item):  # upper right
            count += 1
        if ((r + 1) < len(new_grid)) and ((c - 1) >= 0) and (new_grid[r + 1][c - 1] == cnt_item): #lower left
            count += 1
        if ((r + 1) < len(new_grid)) and ((c + 1) < len(new_grid[0])) and (new_grid[r + 1][c + 1] == cnt_item): #lower right
            count += 1
    return count


def get_hotspots(new_grid, cnt_item, diag=False):
    '''
    input param: 2D grid of city, count item, position as a tuple, default value False for diag.
    return: position of max concentration of human/vampires.
    '''

    count = 0  # starting count.
    max_count = 0  # starting max count for the hotspot
    position = (0, 0)  # location of hotspot

    for r in range(len(new_grid)):
        for c in range(len(new_grid[r])):
            if ((r - 1) >= 0) and (new_grid[r-1][c] == cnt_item):            #up
                count += 1
            if ((r + 1) < len(new_grid)) and (new_grid[r + 1][c] == cnt_item):    #down
                count += 1
            if ((c - 1) >= 0) and (new_grid[r][c-1] == cnt_item):            #left
                count += 1
            if ((c + 1) < len(new_grid[0])) and (new_grid[r][c+1] == cnt_item):  #right
                count += 1
            if diag == True:
                if ((r - 1) >= 0) and ((c - 1) >= 0) and (new_grid[r - 1][c - 1] == cnt_item): #upper left
                    count += 1
                if ((r - 1) >= 0) and ((c + 1) < len(new_grid[r])) and (new_grid[r - 1][c + 1] == cnt_item):  # upper right
                    count += 1
                if ((r + 1) < len(new_grid)) and ((c - 1) >= 0) and (new_grid[r + 1][c - 1] == cnt_item): #lower left
                    count += 1
                if ((r + 1) < len(new_grid)) and ((c + 1) < len(new_grid[r])) and (new_grid[r + 1][c + 1] == cnt_item): #lower right
                    count += 1
            if count >= max_count:  # found a new hotspot
                position = (r, c)
                max_count = count
                # print("newMax:" + str(max_count))  # for debug
                # print(position)  # for debug
            count = 0
    return position

