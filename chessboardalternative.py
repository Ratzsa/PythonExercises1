import termcolor

board = []
pawnW = u'\u265F'
pawnB = u'\u2659'

## Piece Class
class Piece:
    def __init__(self, text, player):
        self.text = text
        self.player = player
    def __str__(self):
        return f"{self.text}"
    def color(self):
        if(cell.player == 0):
            return 'white'
        return 'black'
    
## Set up Board
for i in range(8):
    row = [None for i in range(8)]
    board.append(row)

## Add pieces
for i in range(8):
    board[6][i] = Piece(pawnW, 0)
    board[1][i] = Piece(pawnB, 1)

## Render Board
square = 1
for row in board:
    for cell in row:
        content = cell.text + " " if cell else '  '
        color = cell.color() if cell else 'white'

        if square % 2 == 0:
            termcolor.cprint(content, color, 'on_dark_grey', end = '')
        else:
            termcolor.cprint(content, color, 'on_light_grey', end  = '')
        square += 1
    print('')
    square += 1