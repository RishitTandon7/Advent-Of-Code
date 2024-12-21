def solve_puzzle(disk_map):
    # Step 1: Parse the disk map into files and free spaces
    disk = []
    fid = 0  # File ID counter
    i = 0  # Pointer for the current position in the disk_map
    
    # Parse the disk_map
    while i < len(disk_map):
        if disk_map[i] == '.':
            # Found free space ('.') in the map
            disk.append(-1)
            i += 1
        else:
            # Found a file block (digit) in the map
            blocks = int(disk_map[i])
            disk.extend([fid] * blocks)
            fid += 1
            i += 1

    print(f"Initial disk state: {disk}")

    # Step 2: Try to move files (from highest ID to lowest)
    for file_id in range(fid - 1, -1, -1):
        file_positions = [i for i, x in enumerate(disk) if x == file_id]
        file_length = len(file_positions)  # The length of the file
        
        # Try to find a contiguous block of free space large enough for the file
        print(f"Moving file {file_id} with length {file_length}...")
        for i in range(len(disk) - file_length + 1):
            if all(disk[i + j] == -1 for j in range(file_length)):
                print(f"Found space for file {file_id} starting at position {i}")
                # If we find a space large enough, move the file to that location
                for j in range(file_length):
                    disk[i + j] = file_id
                break  # Once the file is moved, break out of the loop

    print(f"Disk state after moving files: {disk}")

    # Step 3: Calculate the checksum
    checksum = sum(i * x for i, x in enumerate(disk) if x != -1)
    return checksum

# Example usage with the provided input (assuming you are reading from a file)
input_file = "Day9/input.txt"
with open(input_file, "r") as f:
    disk_map = f.read().strip()

result = solve_puzzle(disk_map)
print(f"Filesystem checksum: {result}")
