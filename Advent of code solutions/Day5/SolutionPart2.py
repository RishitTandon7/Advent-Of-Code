from collections import defaultdict, deque

def parse_input(input_data):

    rules_section, updates_section = input_data.strip().split("\n\n")

    rules = []
    for rule in rules_section.splitlines():
        x, y = map(int, rule.split("|"))
        rules.append((x, y))

    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):

    position = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:

        if x in position and y in position:
            if position[x] > position[y]:
                return False
    return True

def correct_order(update, rules):

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    

    pages = set(update)
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)

    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def middle_page(update):    
    return update[len(update) // 2]

def main(file_path):
\
    with open(file_path, 'r') as f:
        input_data = f.read()

    rules, updates = parse_input(input_data)
    
    total = 0
    for update in updates:
        if not is_update_valid(update, rules):

            corrected_update = correct_order(update, rules)
            total += middle_page(corrected_update)
    
    return total

file_path = "Day5/input.txt"

result = main(file_path)
print(result)
