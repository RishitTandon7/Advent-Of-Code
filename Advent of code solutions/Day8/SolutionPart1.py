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

    # Calculate antinodes for each antenna
    antinodes = set()
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(len(array)):
                if i == j:
                    continue
                r1, c1 = array[i]
                r2, c2 = array[j]
                
                # Calculate the new antinode positions
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))

    # Check valid antinodes within grid boundaries
    valid_antinodes = [ (r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols ]
    
    # Return the total number of unique valid antinodes
    return len(valid_antinodes)

# Main function to solve the puzzle
def solve_puzzle(input_file):
    grid = parse_input(input_file)
    return calculate_antinodes(grid)

# Run the solution
input_file = 'Day8/input.txt'
result = solve_puzzle(input_file)
print(f"\nTotal number of unique antinodes: {result}")
