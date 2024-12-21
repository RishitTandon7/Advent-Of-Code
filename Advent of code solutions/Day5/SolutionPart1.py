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

def middle_page(update):
    return update[len(update) // 2]

def main(file_path):
    with open(file_path, 'r') as f:
        input_data = f.read()
    rules, updates = parse_input(input_data)
    
    total = 0
    for update in updates:
        if is_update_valid(update, rules):

            total += middle_page(update)
    
    return total


file_path = "Day5/input.txt"

result = main(file_path)
print(result)
