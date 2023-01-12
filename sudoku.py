#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"
domain = {1,2,3,4,5,6,7,8,9}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

row_1 = {"A", "B", "C"}
row_2 = {"D", "E", "F"}
row_3 = {"G", "H", "I"}

col_1 = {1, 2, 3}
col_2 = {4, 5, 6}
col_3 = {7, 8, 9}

def goal_check(board):
    if 0 in board.values():
        return False
    else:
        return True

def get_domain(key, board):
    global domain, letters, row_1, row_2, row_3, col_1, col_2, col_3

    row, col = key[0], key[1]
    used = set()

    #column check
    for c in domain:
        temp = row
        temp += str(c)
        if board[temp] != 0:
            used.add(board[temp])

    #row check
    for r in letters:
        temp = r
        temp += col
        if board[temp] != 0:
            used.add(board[temp])
    #print(used)

    if row in row_1:
        g_r = row_1
    elif row in row_2:
        g_r = row_2
    else:
        g_r = row_3

    if int(col) in col_1:
        g_c = col_1
    elif int(col) in col_2:
        g_c = col_2
    else:
        g_c = col_3

    temp = ''
    for r in g_r:
        temp += r
        for c in g_c:
            temp += str(c)
            if board[temp] != 0:
                used.add(board[temp])
            temp = temp[:-1]
        temp = ''
    # print("used")
    # print(used)
    # print("domain")
    # print(domain)

    avail_domain = domain.difference(used)

    return avail_domain

def MRV(variables, board):

    min_domain = 100

    for key in variables:
        avail_domain = get_domain(key, board)
        if len(avail_domain) < min_domain:
            target_var = key
            domains = avail_domain.copy()
            min_domain = len(avail_domain)

    return target_var, domains

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    if goal_check(board):
        return board

    #select unassigned variables
    variables = []
    for key in board:
        if board[key] == 0:
            variables.append(key)

    target_var, domains = MRV(variables, board)

    #forward checking
    if len(domains) == 0:
        return False

    for value in domains:
        #print("I make it in")
        board[target_var] = value
        result = backtracking(board)
        if result != False:
            return result
        else:
            board[target_var] = 0

    return False


if __name__ == '__main__':
    if len(sys.argv) > 1:

        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}

        solved_board = backtracking(board)

        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")
