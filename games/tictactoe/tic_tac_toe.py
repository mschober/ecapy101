


class TicTacToe():


    def init_row(self):
        return ['','','']

    def __init__(self):
        self.grid = [
            self.init_row(),
            self.init_row(),
            self.init_row()
        ]

    def display_board(self):
        for row in self.grid:
            print row

    def update_grid(self,spot, player):
        (row,column) = spot.split(',')
        (row,column) = (int(row),int(column))
        self.grid[row][column] = player

def new_game():
    g = TicTacToe()
    players = ["X","O"]
    player = 0
    while True:
        player_token = players[player]
        print "Its player {0}'s turn.".format(player_token)
        g.display_board()
        spot = raw_input("Select your play: ")
        g.update_grid(spot, player_token)
        player += 1
        player = player % 2

