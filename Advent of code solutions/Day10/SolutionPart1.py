from collections import deque

# Function to check if a position is within bounds of the map
def in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

# Directions for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS to explore the trail from a trailhead
def bfs(start_x, start_y, grid):
    # Queue for BFS
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    reachable_9s = 0
    
    # Perform BFS
    while queue:
        x, y = queue.popleft()
        
        # If we reach a 9, count it
        if grid[x][y] == 9:
            reachable_9s += 1
        
        # Check all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny, grid) and (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return reachable_9s

# Main function to solve the puzzle
def solve_puzzle(grid):
    total_score = 0
    
    # Iterate over all positions to find trailheads (height 0)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                # For each trailhead, perform BFS to calculate the score
                score = bfs(x, y, grid)
                total_score += score
    
    return total_score

# Function to read the map from the input file
def read_map_from_file(filename):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            grid.append([int(char) for char in line.strip()])
    return grid

# Main execution
if __name__ == "__main__":
    # Read the map from the input file
    grid = read_map_from_file("Day10/input.txt")
    
    # Solve the puzzle and print the result
    result = solve_puzzle(grid)
    print(f"Sum of the scores of all trailheads: {result}")
