placed_positions = [(1, 4), (5, 3), (2, 1)]
full_row = 4
new_positions = []

for pos in placed_positions:
    if pos[1] < full_row:
        new_positions.append((pos[0], pos[1] + 1))
print(new_positions)