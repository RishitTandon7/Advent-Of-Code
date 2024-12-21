# Define movement directions for the guard: Up, Right, Down, Left
direction_map = {
    '^': (-1, 0),  # Up
    '>': (0, 1),   # Right
    'v': (1, 0),   # Down
    '<': (0, -1),  # Left
}

# Right turn sequence: Up -> Right -> Down -> Left -> Up -> ...
turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

# Read the input map from the file
def read_map(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

# Find the starting position and direction
def find_starting_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in '^v<>':
                return r, c, grid[r][c]

# Simulate the movement of the guard and count distinct positions visited
def simulate_guard(grid):
    visited = set()
    r, c, direction = find_starting_position(grid)
    rows, cols = len(grid), len(grid[0])

    # Mark the initial position as visited
    visited.add((r, c))

    while True:
        # Move the guard
        dr, dc = direction_map[direction]
        nr, nc = r + dr, c + dc

        # Check if the guard has left the area
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            break

        # If the guard encounters an obstacle, turn right
        if grid[nr][nc] == '#':
            direction = turn_right[direction]
        else:
            # Otherwise, move to the next position
            r, c = nr, nc
            visited.add((r, c))

    return len(visited)

# Main execution
if __name__ == "__main__":
    grid = read_map("Day6/input.txt")  # Path to the input file
    distinct_positions = simulate_guard(grid)
    print("Distinct positions visited:", distinct_positions)
