def check_pawn(board, row, col):
    # Pawn โจมตีทแยงขึ้น 2 ด้าน
    if row - 1 >= 0:
        #ทแยงขึ้นซ้าย
        if col - 1 >= 0 and board[row - 1][col - 1] == 'K':
            return True
        #ทแยงขึ้นขวา
        if col + 1 < len(board[row]) and board[row - 1][col + 1] == 'K':
            return True

    return False


def check_rook(board, row, col):
    directions = [
        (-1, 0),  # ขึ้น
        (1, 0),   # ลง
        (0, -1),  # ซ้าย
        (0, 1)    # ขวา
    ]

    for row_change, col_change in directions:

        new_row = row + row_change
        new_col = col + col_change

        while (0 <= new_row < len(board) and
               0 <= new_col < len(board[new_row])):

            piece = board[new_row][new_col]

            if piece == 'K':
                return True

            # เจอหมากตัวอื่น -> เดินทะลุไม่ได้
            if piece in 'PRBQ':
                break

            new_row += row_change
            new_col += col_change

    return False


def check_bishop(board, row, col):
    directions = [
        (-1, -1),  # ↖
        (-1, 1),   # ↗
        (1, -1),   # ↙
        (1, 1)     # ↘
    ]

    for row_change, col_change in directions:

        new_row = row + row_change
        new_col = col + col_change

        while (0 <= new_row < len(board) and
               0 <= new_col < len(board[new_row])):

            piece = board[new_row][new_col]

            if piece == 'K':
                return True

            # เจอหมากตัวอื่น -> เดินทะลุไม่ได้
            if piece in 'PRBQ':
                break

            new_row += row_change
            new_col += col_change

    return False


def check_queen(board, row, col):
    # Queen เดินได้เหมือน Rook และ Bishop
    if check_rook(board, row, col):
        return True

    if check_bishop(board, row, col):
        return True

    return False


def checkmate(board):
    board = board.splitlines()
    # ตรวจหมากทุกตัว
    for row in range(len(board)):
        for col in range(len(board[row])):

            piece = board[row][col]

            if piece == 'P':
                if check_pawn(board, row, col):
                    print("Success")
                    return

            elif piece == 'R':
                if check_rook(board, row, col):
                    print("Success")
                    return

            elif piece == 'B':
                if check_bishop(board, row, col):
                    print("Success")
                    return

            elif piece == 'Q':
                if check_queen(board, row, col):
                    print("Success")
                    return

    print("Fail")