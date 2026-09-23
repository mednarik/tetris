import os, time

bg_symbol = "."
figure_symbol = "#"
########################################################
def is_row_full(figure_positions, board_width, board_height):

    example = [i for i in range(0, board_width, 2)]
    y_positions = [pos[0] for pos in figure_positions if pos[1] == board_height - 2]
    if y_positions == example:
        return True
    return False

def remove_full_line(figure_positions, board_height):
    lst = [(pos[0], pos[1] + 1) for pos in figure_positions if pos[1] + 1 < board_height]
    return lst
##################################################
def figures_will_overlap(fig, direction, figures): #check if a figure overlaps with any figure in a given list
    
    if direction == "right":
        x_modifier = 1
        y_modifier = 0
    elif direction == "left":
        x_modifier = -1
        y_modifier = 0
    else:
        x_modifier = 0
        y_modifier = 1

    figures_positions = []
    for figure in figures:
        for i in range(2):
            for j in range(2):
                figures_positions.append((figure[0] + i, figure[1] + j)) #get occupied positions

    
    for i in range(2):  #for every size part
        for j in range(2):
            if (fig.x + x_modifier + i, fig.y + y_modifier + j) in figures_positions:
                return True
    return False


class Figure():
    def __init__(self, pos: tuple):
        self.size = 2
        self.spawnpos = pos
        self.x = pos[0]
        self.y = pos[1]

    def gravity(self, board_height, figures):
        if self.y + self.size < board_height and not figures_will_overlap(self, "down", figures):
            self.y += 1
            if self.y + self.size == board_height:
                return False #it was able to fall but now its on the bottom
            else:
                return True #it was able to fall
        return False #it wasn't able to fall
    
    def move(self, direction: str, board_width: int, figures: list):
        if direction == "a":
            direction = "left"
            if self.x > 0 and not figures_will_overlap(self, direction, figures):
                self.x -= 1
                return True #it moved
        elif direction == "d":
            direction = "right"
            if self.x + self.size < board_width and not figures_will_overlap(self, direction, figures):
                self.x += 1
                return True #it moved

        return False #it didn't move

    def reset(self):
        self.x = self.spawnpos[0]
        self.y = self.spawnpos[1]
        
class Board():
    def __init__(self):
        self.width = 10
        self.height = 16
    def draw_board(self, active, placed_positions):

        for i in range(self.height): #for every row
            figs_x_positions = [] #list for every occupied x position in this row
            if active.y == i or active.y + 1 == i: #if it is on that row
                for j in range(active.size): #add its x positions to the list
                    figs_x_positions.append(active.x + j )

            for pos in placed_positions:
                if pos[1] == i or pos[1] + 1 == i:
                    figs_x_positions.append(pos[0])
                    figs_x_positions.append(pos[0] + 1)
                
            for j in range(self.width):
                if j in figs_x_positions:
                    print(figure_symbol, end="")
                else:
                    print(bg_symbol, end="")
            print() # go to a new row


def main():
    board = Board()
    placed_positions = []
    fig1 = Figure((4, 0))

    while True:
        
        alive = True
        while alive:

            os.system("cls")
            board.draw_board(fig1, placed_positions)
    
            

            fig1.move(input("Where do you want to go? (a/d): "), board.width, placed_positions)

            os.system("cls")
            board.draw_board(fig1, placed_positions)
        

            alive = fig1.gravity(board.height, placed_positions)

            if not alive:
                placed_positions.append((fig1.x, fig1.y))
                fig1.reset()

            if is_row_full(placed_positions, board.width, board.height):
                placed_positions = remove_full_line(placed_positions, board.height)

def test():
    lst = [(i, 16) for i in range(10)]
    print(lst)
    print(is_row_full(lst, 10, 17))

main()