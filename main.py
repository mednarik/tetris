bg_symbol = "#"
figure_symbol = "%"

class Figure():
    def __init__(self):
        self.size = 2
        self.x = 4
        self.y = 2

class Board():
    def __init__(self):
        self.width = 10
        self.height = 16
    def draw_board(self, figures):
        for i in range(self.height): #for every row
            figs_x_positions = [] #list for every occupied x position in this row
            for figure in figures: #check for every figure
                if figure.y == i or figure.y + 1 == i: #if it is on that row
                    for i in range(figure.size): #add its x positions to the list
                        figs_x_positions.append(figure.x + i)
            
            for i in range(self.width):
                if i in figs_x_positions:
                    print(figure_symbol, end="")
                else:
                    print(bg_symbol, end="")
            print() # go to a new row


placed_figures = []
board = Board()

figure1 = Figure()
placed_figures.append(figure1)

board.draw_board(placed_figures)

