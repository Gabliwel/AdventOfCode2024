array1 = []
array2 = []

with open("input.txt", "r") as file:
    for line in file:
        values = line.split()
        array1.append(int(values[0]))
        array2.append(int(values[1]))

array1.sort()
array2.sort()
total = 0

for i in range(1000):
    total += abs(array1[i] - array2[i])

print("Result:", total)