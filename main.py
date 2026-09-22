import os, time

bg_symbol = "#"
figure_symbol = "%"

def figures_will_overlap(fig1, direction, figures): #check if a figure overlaps with any figure in a given list
    figures_x_positions = []
    figures_y_positions = []
    if direction == "right":
        x_modifier = 1
        y_modifier = 0
    elif direction == "left":
        x_modifier = -1
        y_modifier = 0
    elif direction == "down":
        x_modifier = 0
        y_modifier = 1
    
    for figure in figures: #get all occupied positions
        for i in range(figure.size):
            figures_x_positions.append(figure.x + i)
            figures_y_positions.append(figure.y + i)
    for i in range(fig1.size):  #for every size part
         if fig1.x + i + x_modifier in figures_x_positions and fig1.y + y_modifier + i in figures_y_positions:
            return True
    return False


class Figure():
    def __init__(self, pos: tuple):
        self.size = 2
        self.x = pos[0]
        self.y = pos[1]

    def gravity(self, board_height, figures):
        if self.y + self.size < board_height and not figures_will_overlap(self, "down", figures):
            self.y += 1
            return True #it was able to fall
        return False #it wasn't able to fall
    
    def move(self, direction: str, board_width: int, figures: list):
        if direction == "a":
            direction = "left"
        elif direction == "d":
            direction = "right"

        if self.x + self.size < board_width and not figures_will_overlap(self, direction, figures):
            self.x += 1 if direction == "right" else -1
            return True #it was able to fall
        return False #it wasn't able to fall


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


def main():
    board = Board()
    placed_figures = []
    figures = []

    while True:
        fig1 = Figure((4, 0))
        figures.append(fig1)
        alive = True
        while alive:
            
            board.draw_board(figures)

            alive = fig1.gravity(board.height, placed_figures)
            if not alive:
                placed_figures.append(fig1)

            fig1.move(input("Where do you want to go? (a/d): "), board.width, placed_figures)
            os.system("cls")
def test():
    fig1 = Figure((4, 0))
    fig2 = Figure((6, 1))
    print(figures_will_overlap(fig1, "right", [fig2]))
    
main()