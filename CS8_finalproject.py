def read_configuration(filename):
    file = open(filename, 'r')
        
    listname = []
    fileline = file.readline()
    
    while fileline:
        filerow = fileline.split()
        listname.append(filerow)
        fileline = file.readline()
        
    return listname

print(read_configuration('board1.txt'))

def next_day(grid):
    if len(grid) == 0:
        return -1
    elif len(grid) ==1:
        return -1
    else:
        return 0

def days_remaining_1(grid):
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.
    '''
    num_day = 0  # the starting day
    show_city_each_day(grid, num_day)  # show the city on day 0

    # make a copy of the original city
    original_grid = copy.deepcopy(grid)
    next_grid = next_day(grid)  # get the city on the next day

    while next_grid != original_grid:
        # keep looping while next day's city is different from today's
        num_day += 1 

        # TODO: fill-in the rest of processing
    return num_day
