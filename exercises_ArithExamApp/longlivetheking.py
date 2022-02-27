#The chess king can stand on any square and can move one step horizontally, vertically, or diagonally in any direction within the board.

#The input will contain the coordinates on which the king is located. You should figure out and print how many moves the figure can make: for example, from the position (1, 8), the king can make only 3 moves (right, down, diagonally).

x, y = int(input()), int(input())
if x >= 2 and x <= 7 and y >= 2 and y <= 7:
    print('8')
if x == 1 or x == 8 or y == 8 or y == 1:
    if (x == 1 or x == 8) and (y == 1 or y == 8):
        print('3')
    elif (1 < x < 8) or (1 < y < 8):
        print('5')
    else:
        print('4')