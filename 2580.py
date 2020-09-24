"""
    2580. 스도쿠
"""
is_found = False

def do(empty_cells):
    global board, board_3x3, board_flipped, is_found
    if is_found: return
    if not empty_cells: 
        print('\n'.join([' '.join([str(cell) for cell in line]) for line in board]))
        is_found = True
        return

    x, y = empty_cells[0]    

    for candidate in range(1, 10):
        if is_valid(x, y, candidate):
            board[y][x] = candidate
            board_flipped[x][y] = candidate
            board_3x3[y // 3 * 3 + x // 3][y % 3 * 3 + x % 3] = candidate
            
            do(empty_cells[1:])

            board[y][x] = 0
            board_flipped[x][y] = 0
            board_3x3[y // 3 * 3 + x // 3][y % 3 * 3 + x % 3] = 0


def is_valid(x, y, candidate):
    if not candidate in board[y]:
        if not candidate in board_flipped[x]:
            if not candidate in board_3x3[y // 3 * 3 + x // 3]:
                return True
    return False

def get_3x3(board):
    board_3x3, i = [[] for _ in range(9)], 0

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            for y in range(row, row + 3):
                for x in range(col, col + 3):
                    board_3x3[i].append(board[y][x])                    
            i += 1

    return board_3x3

def get_empty_cells(board):
    return [[x, y] for y in range(9) for x in range(9) if board[y][x] == 0]

board = [list(map(int, input().split())) for _ in range(9)]
board_flipped = list(map(list, zip(*board)))
board_3x3 = get_3x3(board)
empty_cells = get_empty_cells(board)

do(empty_cells)