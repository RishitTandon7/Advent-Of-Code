import re
with open('Day3/input.txt', 'r') as file:
    memory = file.read()
valid_instructions = re.findall(r'mul\((\d+),(\d+)\)', memory)
total_sum = 0
for instruction in valid_instructions:
    x, y = map(int, instruction)
    total_sum += x * y
print(total_sum)