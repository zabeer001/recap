
board = input()
board = board.split(' ')
board_area = int(board[0]) * int(board[1])
number_of_dominos = board_area // 2
print(number_of_dominos)
