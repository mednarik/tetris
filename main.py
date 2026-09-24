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
                pos = [pos[0], pos[1] + 1]
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
        self.spawnpos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.draw_direction = "right" #the figure is being drawn from left to right

    def gravity(self, board_height, placed_squares):
        way_blocked = False
        for square in self.get_occupied_squares():
            if squares_will_overlap(square, "down", placed_squares):
                way_blocked = True
                break
            if square[1] + 1 >= board_height:
                way_blocked = True
                break
        if way_blocked:
            return False #it wasn't able to fall
        self.y += 1
        return True #it was able to fall
    
    def move(self, direction: str, board_width: int, placed_squares: list):
        if direction == "a":
            direction = "left"
            for square in self.get_occupied_squares():
                if squares_will_overlap(square, direction, placed_squares):
                    return False
                if square[0] <= 0:
                    return False
            self.x -= 1

        elif direction == "d":
            direction = "right"
            
            for square in self.get_occupied_squares():
                if squares_will_overlap(square, direction, placed_squares):
                    return False #it didn't move  
                if square[0] + 1 >= board_width:
                    
                    return False #it didn't move
            self.x += 1        

        return True  #it moved

    def rotate(self):
        directions = ["up", "right", "down", "left"]

        current_idx = directions.index(self.draw_direction)
        if current_idx < len(directions) - 1:
            self.draw_direction = directions[current_idx + 1]
        else:
            self.draw_direction = directions[0]
        
        
        

    def reset(self):
        self.x = self.spawnpos[0]
        self.y = self.spawnpos[1]

class Square(Figure):
    def __init__(self, pos):
        super().__init__(pos)
        self.size = 2

    def get_occupied_squares(self):
        occupied_squares = []
        if self.draw_direction == "right":
            for i in range(self.size):
                for j in range(self.size):
                    occupied_squares.append((self.x + i, self.y + j))
class Line(Figure):
    def __init__(self, pos):
        super().__init__(pos)
        self.length = 4
        self.rotation = 0 #degrees

    def get_occupied_squares(self):
        occupied_squares = []

        if self.draw_direction in ["right", "left"]:
            for i in range(self.length):
                occupied_squares.append((self.x + i, self.y))
        else:
            for i in range(self.length):
                occupied_squares.append((self.x, self.y + i))
        return occupied_squares

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
    fig1 = Line((4, 0))

    while True:
        
        alive = True
        while alive:

            os.system("cls")
            board.draw_board(join_two_lists(placed_positions, fig1.get_occupied_squares()))
    
            
            print("(a) to go left/(d) to go right/(r) to rotate/() to not move")
            user_input = input("What do you want to do?: ")
            if user_input == "r":
                fig1.rotate()
            else:
                fig1.move(user_input, board.width, placed_positions)

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