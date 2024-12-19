import re

total = 0
content = ""
with open("input.txt", "r") as file:
    content = file.read().strip()

found = re.findall(r"mul\((\d+),(\d+)\)", content)


for mul in found:
    #print(mul)
    total += int(mul[0]) * int(mul[1])

print("Result:", total)
