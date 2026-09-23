import os, time

bg_char = '.'
figure_char = '#'
########################################################
def is_row_full(placed_positions, board_width, board_height):

    example = [i for i in range(0, board_width, 2)]
    y_positions = [pos[0] for pos in placed_positions]
    if y_positions == example:
        return True
    return False

def remove_full_line(figure_positions, board_height):
    lst = [(pos[0], pos[1] + 1) for pos in figure_positions if pos[1] + 1 < board_height]
    return lst
##################################################


def join_two_lists(lst1, lst2):
    lst = []
    for item in lst1:
        lst.append(item)
    for item in lst2:
        lst.append(item)
    return lst

def squares_will_overlap(alpha_sigma_lone_wolf_ahh_square, direction, squares): #check if a square overlaps with any other square in a given list
    
    if direction == "right":
        x_modifier = 1
        y_modifier = 0
    elif direction == "left":
        x_modifier = -1
        y_modifier = 0
    else:
        x_modifier = 0
        y_modifier = 1

    for square in squares:
        if (alpha_sigma_lone_wolf_ahh_square[0] + x_modifier, alpha_sigma_lone_wolf_ahh_square[1] + y_modifier) == square:
            return True
    return False


class Figure():
    def __init__(self, pos: tuple):
        self.size = 2
        self.spawnpos = pos
        self.x = pos[0]
        self.y = pos[1]

    def gravity(self, board_height, placed_squares):
        way_blocked = False
        for square in self.get_occupied_squares():
            if squares_will_overlap(square, "down", placed_squares):
                way_blocked = True
                break        
        if self.y + self.size < board_height and not way_blocked:
            self.y += 1
            if self.y + self.size == board_height:
                return False #it was able to fall but now its on the bottom
            else:
                return True #it was able to fall
        return False #it wasn't able to fall
    
    def move(self, direction: str, board_width: int, placed_squares: list):
        if direction == "a":
            direction = "left"
            way_blocked = False
            for square in self.get_occupied_squares():
                if squares_will_overlap(square, direction, placed_squares):
                    way_blocked = True
                    break
            if self.x > 0 and not way_blocked:
                self.x -= 1
                return True #it moved
        elif direction == "d":
            direction = "right"
            way_blocked = False
            for square in self.get_occupied_squares():
                if squares_will_overlap(square, direction, placed_squares):
                    way_blocked = True
                    break
            if self.x + self.size < board_width and not way_blocked:
                self.x += 1
                return True #it moved
        return False #it didn't move
    
    def get_occupied_squares(self):
        occupied_squares = []
        for i in range(self.size):
            for j in range(self.size):
                occupied_squares.append((self.x + i, self.y + j))
        return occupied_squares

    def reset(self):
        self.x = self.spawnpos[0]
        self.y = self.spawnpos[1]
        
class Board():
    def __init__(self):
        self.width = 10
        self.height = 16
    def draw_board(self, positions):

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in positions:
                    print(figure_char, end="")
                else:
                    print(bg_char, end="")
            print()


def main():
    board = Board()
    placed_positions = []
    fig1 = Figure((4, 0))

    while True:
        
        alive = True
        while alive:

            os.system("cls")
            board.draw_board(join_two_lists(placed_positions, fig1.get_occupied_squares()))
    
            

            fig1.move(input("Where do you want to go? (a/d): "), board.width, placed_positions)

            os.system("cls")
            board.draw_board(join_two_lists(placed_positions, fig1.get_occupied_squares()))

        

            alive = fig1.gravity(board.height, placed_positions)

            if not alive:
                for square in fig1.get_occupied_squares():
                    placed_positions.append(square)
                fig1.reset()

            #if is_row_full(placed_positions, board.width, board.height):
                #placed_positions = remove_full_line(placed_positions, board.height)

def test():
    fig1 = Figure((1, 1))
    print(fig1.get_occupied_squares())
main()