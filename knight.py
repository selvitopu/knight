
/*!
 * Copyright (c) Hllboy 2016. All Rights Reserved.
 */
__author__ = 'US'
import sys

def main(argv = sys.argv):
    sys.setrecursionlimit(500)
    move = 1
    main_list = [[0 for z in range(9)] for z in range(9)]
    for a in range(1, 8):
        for b in range(1, 8):
            main_list[a][b] = 0
    m = raw_input()
    m.split()
    x = f2(m[0])
    y = int(m[1])

    print 'Position of Knight: %s ' %m
    print 'Movement of the knight to visit all squares:'
    recursiveSolution(main_list, x, y)

def recursiveSolution(main_table, x, y):

    zz = checker(main_table)

    if zz == 1:
        for e in range(1, 9):
            for f in range(1, 9):
                print main_table[e][f],
            print("\n")
        sys.exit()
    if main_table[x][y] == 0:
        main_table[x][y] = 1
        print "%s%d" %(f1(x), y)
        recursiveSolution(main_table, x, y)
    else:
        xx = moveDeterminer(main_table, x, y)
        if xx == 0:
            x -= 2
            y += 1
        if xx == 1:
            x -= 1
            y += 2
        if xx == 2:
            x += 1
            y += 2
        if xx == 3:
            x += 2
            y += 1
        if xx == 4:
            x += 2
            y -= 1
        if xx == 5:
            x += 1
            y -= 2
        if xx == 6:
            x -= 1
            y -= 2
        if xx == 7:
            x -= 2
            y -= 1
        if xx == 9:
            for e in range(1, 9):
                for f in range(1, 9):
                    print main_table[e][f],
                print("\n")
            sys.exit()
        recursiveSolution(main_table, x, y)
def moveDeterminer(chess_table, e, f):
    smallest = 20
    smallest1 = 9
    if 0 < e-2 < 9 and 0 < f+1 < 9:
        if moveChecker(chess_table, e-2, f+1) < smallest and chess_table[e-2][f+1] == 0:
            smallest = moveChecker(chess_table, e-2, f+1)
            smallest1 = 0
    if 0 < e-1 < 9 and 0 < f+2 < 9:
        if moveChecker(chess_table, e-1, f+2) < smallest and chess_table[e-1][f+2] == 0:
            smallest = moveChecker(chess_table, e-1, f+2)
            smallest1 = 1
    if 0 < e+1 < 9 and 0 < f+2 < 9:
        if moveChecker(chess_table, e+1, f+2) < smallest and chess_table[e+1][f+2] == 0:
            smallest = moveChecker(chess_table,  e+1, f+2)
            smallest1 = 2
    if 0 < e+2 < 9 and 0 < f+1 < 9:
        if moveChecker(chess_table, e+2, f+1) < smallest and chess_table[e+2][f+1] == 0:
            smallest = moveChecker(chess_table, e+2, f+1)
            smallest1 = 3
    if 0 < e+2 < 9 and 0 < f-1 < 9:
        if moveChecker(chess_table, e+2, f-1) < smallest and chess_table[e+2][f-1] == 0:
            smallest = moveChecker(chess_table, e+2, f-1)
            smallest1 = 4
    if 0 < e+1 < 9 and 0 < f-2 < 9:
        if moveChecker(chess_table, e+1, f-2) < smallest and chess_table[e+1][f-2] == 0:
            smallest = moveChecker(chess_table, e+1, f-2)
            smallest1 = 5
    if 0 < e-1 < 9 and 0 < f-2 < 9:
        if moveChecker(chess_table, e-1, f-2) < smallest and chess_table[e-1][f-2] == 0:
            smallest = moveChecker(chess_table, e-1, f-2)
            smallest1 = 6
    if 0 < e-2 < 9 and 0 < f-1 < 9:
        if moveChecker(chess_table, e-2, f-1) < smallest and chess_table[e-2][f-1] == 0:
            smallest = moveChecker(chess_table, e-2, f-1)
            smallest1 = 7
    return smallest1
def moveChecker(maintable, c, d):
    result = 0
    if 0 < c-2 < 9 and 0 < d+1 < 9 and maintable[c-2][d+1] == 0:
        result += 1
    if 0 < c-1 < 9 and 0 < d+2 < 9 and maintable[c-1][d+2] == 0:
        result += 1
    if 0 < c+1 < 9 and 0 < d+2 < 9 and maintable[c+1][d+2] == 0:
        result += 1
    if 0 < c+2 < 9 and 0 < d+1 < 9 and maintable[c+2][d+1] == 0:
        result += 1
    if 0 < c+2 < 9 and 0 < d-1 < 9 and maintable[c+2][d-1] == 0:
        result += 1
    if 0 < c+1 < 9 and 0 < d-2 < 9 and maintable[c+1][d-2] == 0:
        result += 1
    if 0 < c-1 < 9 and 0 < d-2 < 9 and maintable[c-1][d-2] == 0:
        result += 1
    if 0 < c-2 < 9 and 0 < d-1 < 9 and maintable[c-2][d-1] == 0:
        result += 1

    return result
def checker(chess_table):
    checker1 = 1
    for c in range(1, 9):
        for d in range(1, 9):
            if chess_table[c][d] == 0:
                checker1 = 0
    return checker1
def f1(t):
    return {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
    }[t]
def f2(t):
    return {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
    }[t]

if __name__ == '__main__':
    main()
