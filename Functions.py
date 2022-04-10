import random
global fullgrid
fullgrid = [[]]


#def is_valid(fullgrid, row, col, candidate):
#    while fullgrid:



def shuffle_row(row):
    temp_row = [1,2,3,4,5,6,7,8,9]
    i=0
    while i<9:
        temp = random.randrange(1, 10)
        while temp not in temp_row:
            temp = random.randrange(1, 10)
        temp_row.remove(temp)
        row[i] = temp
        i+=1
    return row


def make_full_sudoku():
    candidate = [1,2,3,4,5,6,7,8,9]
    i = 0
    candidate = shuffle_row(candidate)
    print(candidate)


make_full_sudoku()
