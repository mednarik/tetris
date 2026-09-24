import os, time

bg_char = '.'
figure_char = '#'

def get_full_rows(placed_positions, board_width, board_height) -> list:
    full_rows = []
    example_row = [i for i in range(board_width)]
    for row in range(board_height):
        row_x_positions = []
        for pos in placed_positions:
            if pos[1] == row:
                row_x_positions.append(pos[0])
        if sorted(row_x_positions) == example_row:
            full_rows.append(row)
    return full_rows

def remove_full_rows(placed_positions, full_rows) -> list:
    placed_positions = [pos for pos in placed_positions if pos[1] not in full_rows]
    for full_row in full_rows:
        for pos in placed_positions:
            if pos[1] < full_row:
                pos[1] += 1
    return placed_positions

    
    


def join_two_lists(lst1, lst2):
    lst = []
    for item in lst1:
        lst.append(item)
    for item in lst2:
        lst.append(item)
    return lst

def squares_will_overlap(alpha_sigma_maincharacter_lone_wolf_ahh_square, direction, squares): #check if a square overlaps with any other square in a given list
    
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
        if (alpha_sigma_maincharacter_lone_wolf_ahh_square[0] + x_modifier, alpha_sigma_maincharacter_lone_wolf_ahh_square[1] + y_modifier) == square:
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
            placed_positions = remove_full_rows(placed_positions, get_full_rows(placed_positions, board.width, board.height))

def test():
    fig1 = Figure((1, 1))
    print(fig1.get_occupied_squares())
main()