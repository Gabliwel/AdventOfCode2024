array1 = []
array2 = []

with open("input.txt", "r") as file:
    for line in file:
        values = line.split()
        array1.append(int(values[0]))
        array2.append(int(values[1]))

total = 0

for value in array1:
    count = array2.count(value)
    total += count * value

print("Result:", total)