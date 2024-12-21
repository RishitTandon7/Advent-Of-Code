def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(word_len):
                    nr, nc = r + i * dr, c + i * dc
                    if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count
with open("Day4/input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]
result = count_xmas(grid)
print("Total XMAS occurrences:", result)
