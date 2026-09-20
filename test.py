class Figure():
    def __init__(self, pos: tuple):
        self.size = 2
        self.x = pos[0]
        self.y = pos[1]

figures_x_positions = []
figures_y_positions = [] 

for figure in figures: #get all occupied positions
    for i in range(figure.size):
        figures_x_positions.append(figure.x + i)
        figures_y_positions.append(figure.y + i)