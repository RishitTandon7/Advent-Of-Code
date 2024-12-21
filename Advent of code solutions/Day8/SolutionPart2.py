def parse_input(input_file):
    """Read the grid and return it as a list of strings."""
    with open(input_file, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def calculate_antinodes(grid):
    """Calculate the number of unique antinode positions in the grid."""
    rows = len(grid)
    cols = len(grid[0])

    # Find all antennas and their positions
    antennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))

    # Set to hold all antinode positions
    antinodes = set()

    # For each frequency, calculate antinode positions
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                
                # Calculate direction vector from antenna 1 to antenna 2
                dr = r2 - r1
                dc = c2 - c1

                # Trace antinode positions in the direction of the vector
                r, c = r1, c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes.add((r, c))
                    r += dr
                    c += dc

                # Trace in the opposite direction
                r, c = r1, c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes.add((r, c))
                    r -= dr
                    c -= dc

    # Filter out invalid antinode positions (out of bounds)
    valid_antinodes = [(r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols]

    # Return the total number of unique valid antinodes
    return len(valid_antinodes)

# Main function to solve the puzzle
def solve_puzzle(input_file):
    grid = parse_input(input_file)
    return calculate_antinodes(grid)

# Run the solution
input_file = 'Day8/input.txt'  # Replace with your file path
result = solve_puzzle(input_file)
print(f"\nTotal number of unique antinodes: {result}")
