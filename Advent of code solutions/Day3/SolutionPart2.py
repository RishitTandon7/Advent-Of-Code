import re

with open("Day3/input.txt", "r") as file:
    memory = file.read()

on = True
total = 0

pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

for match in re.findall(pattern, memory):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False
    elif on and match.startswith("mul("):
        x, y = map(int, match[4:-1].split(","))
        total += x * y

print(total)
