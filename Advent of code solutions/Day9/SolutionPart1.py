def solve_puzzle(disk_map):
    #print(f"Received input: {disk_map}")
    
    # Ensure the input contains only valid digits
    if not disk_map.isdigit():
        raise ValueError(f"Input contains invalid characters. Only digits are allowed. Found: {disk_map}")
    
    # Disk list to hold files and free space
    disk = []
    fid = 0  # File ID counter
    
    # Iterate through the disk map
    for i, char in enumerate(disk_map):
        x = int(char)  # Convert character to integer
        
        if i % 2 == 0:  # Even index = file
            disk += [fid] * x  # Add `x` blocks with file ID `fid`
            fid += 1  # Increment the file ID for the next file
        else:  # Odd index = free space
            disk += [-1] * x  # Add `x` free space blocks
    
    # Now remove extra free space (represented by -1)
    blanks = [i for i, x in enumerate(disk) if x == -1]

    # Compaction: Move files to the left, filling in the free space
    for i in blanks:
        # Remove trailing free space
        while len(disk) > 0 and disk[-1] == -1:
            disk.pop()
        if len(disk) <= i:
            break
        disk[i] = disk.pop()

    # Calculate the checksum by summing i * file_id for each block
    checksum = sum(i * x for i, x in enumerate(disk) if x != -1)  # Skip free space blocks

    return checksum


# Test with input file
if __name__ == "__main__":
    input_file_path = "c:/Users/Rishit Tandon/Desktop/Advent of code solutions/Day9/input.txt"  # Replace with your input file path

    try:
        # Read the input file
        with open(input_file_path, 'r') as f:
            disk_map = f.read().strip()  # Read the entire content and remove any trailing newline

        # Calculate and print the result
        result = solve_puzzle(disk_map)
        print(f"Filesystem checksum: {result}")
    
    except FileNotFoundError:
        print(f"Error: The file at {input_file_path} was not found.")
    except ValueError as e:
        print(e)
