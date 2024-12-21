with open('Day1/input.txt') as f:
    lines = f.read().splitlines()
    if not lines:
        print("The file is empty.")
    else:
        data = [list(map(int, line.split())) for line in lines]
        left_list = [item[0] for item in data]
        right_list = [item[1] for item in data]
        left_list.sort()
        right_list.sort()
        similarity_score = 0
        for left in left_list:
            similarity_score += left * right_list.count(left)
        print(f"Similarity score: {similarity_score}")