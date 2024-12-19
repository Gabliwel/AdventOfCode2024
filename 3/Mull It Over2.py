import re

total = 0
content = ""
with open("input.txt", "r") as file:
    content = file.read().strip()

found = re.findall(r"(:?mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", content)

enabled = True
for mul in found:
    #print(mul)
    if mul[0] != "" and enabled:
        total += int(mul[1]) * int(mul[2])
    else:
        if mul[3] == "do()":
            enabled = True
        elif mul [4] == "don't()":
            enabled = False


print("Result:", total)
