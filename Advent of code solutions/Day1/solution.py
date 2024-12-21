with open('Day1/input.txt') as f: #Change the data file data
    lines = f.read().splitlines()
    if not lines:
        print("The file is empty.")
    else:
        data = [list(map(int, line.split())) for line in lines]
        left_list = [item[0] for item in data]
        right_list = [item[1] for item in data]
        left_list.sort()
        right_list.sort()
        total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
        print(f"Total distance: {total_distance}")
