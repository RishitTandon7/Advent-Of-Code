grid = open("Day4/input.txt").read().splitlines()

count = 0
for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] != "A":
            continue
        
        corners = [
            grid[r - 1][c - 1],  # Top-left
            grid[r - 1][c + 1],  # Top-right
            grid[r + 1][c + 1],  # Bottom-right
            grid[r + 1][c - 1]   # Bottom-left
        ]
        
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            count += 1
print(count)