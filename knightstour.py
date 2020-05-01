__author__      = "Hllboy"
__copyright__   = "Copyright 2016, Knight python"

def main():
    global chessBoard
    for row in range(6):
        for col in range(6):
            chessBoard = [[None for i in range(6)] for j in range(6)]
            knightsTour(row, col, 1)
            print()

def knightsTour(row, col, move):
    if _inRange(row, col) and _isLegal(row, col):
        chessBoard[row][col] = move

        if _isFull(chessBoard):
            return True, _draw(chessBoard)    
 

        possibleOffsets = ((-2, -1), (-2, 1), (-1, 2), (1, 2), \
                           (2, 1), (2, -1), (1, -2), (-1, -2))
        for offset in possibleOffsets:
            if knightsTour(row + offset[0], col + offset[1], move + 1):
                return True

        chessBoard[row][col] = None
        return False
    else:
        return False

def _isLegal(row, col):
    if _inRange(row, col) and chessBoard[row][col] == None:
        return True
    else:
        return False

def _inRange(row, col):
    try:
        chessBoard[row][col]
        return True
    except IndexError:
        return False

def _isFull(chessBoard):
    for row in chessBoard:
        for col in row:
            if col is None:
                return False
    return True

def _draw(chessBoard):
    for row in chessBoard:
        for col in row:
            print("%4s" %col)
        print()

main()
