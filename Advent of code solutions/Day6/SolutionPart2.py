def get_start():
    # Find the starting position of the guard
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)

def check_for_loop():
    # Function to check if adding an obstruction causes a loop
    r, c = start_r, start_c
    dr, dc = -1, 0  # Initial direction is up
    visited = set()

    while True:
        # If the current position with the direction has already been visited, it's a loop
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        
        # Check if the next move would be out of bounds
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            return False
        
        # If the next cell is an obstacle, turn right (90 degrees)
        if grid[r + dr][c + dc] == "#":
            dr, dc = dc, -dr  # Right turn: (dx, dy) -> (dy, -dx)
        else:
            # Move to the next position
            r += dr
            c += dc

# Read the grid from the input file
file_path = "Day6/input.txt"  # Ensure correct path
with open(file_path, "r") as f:
    grid = list(map(list, map(str.strip, f.readlines())))

# Grid dimensions
num_rows = len(grid)
num_cols = len(grid[0])

# Get the starting position of the guard
start_r, start_c = get_start()

# Part 2: Count the valid positions where placing an obstruction causes a loop
part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if grid[ro][co] != ".":  # Skip non-empty cells
            continue
        # Temporarily place an obstruction
        grid[ro][co] = "#"
        
        # Check if this leads to a loop
        if check_for_loop():
            part2 += 1
        
        # Remove the obstruction after checking
        grid[ro][co] = "."

# Output the result for Part 2
print(f"Part 2: {part2}")
