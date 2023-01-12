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
    #domain = {1,2,3,4,5,6,7,8,9}

    return avail_domain

def MRV(variables, board):
    #domains = {}
    #target_var = ''
    min_domain = 100

    for key in variables:
        print(key)
        avail_domain = get_domain(key, board)
        print(avail_domain)
        if len(avail_domain) < min_domain:
            target_var = key
            domains = avail_domain.copy()
            min_domain = len(avail_domain)
    print(target_var)
    print(domains)
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
        return board_to_string(board)

    solved_board = board
    return solved_board


if __name__ == '__main__':
    if len(sys.argv) > 1:

        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}

        print_board(board)
        # domain1 = get_domain('A1', board)
        # print(domain1)
        # domain1 = get_domain('H5', board)
        # print(domain1)
        # domain2 = get_domain('E7', board)
        # print(domain2)
        variables = ['A1','H5', 'E7', 'A9','F5']
        MRV = MRV(variables, board)
        print(MRV)
