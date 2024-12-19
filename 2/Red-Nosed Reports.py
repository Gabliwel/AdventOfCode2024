def isSafe(array):
    increasing = True
    decreasing = True

    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]

        if(diff > 0 and increasing == True):
            decreasing = False
        elif(diff < 0 and decreasing == True):
            increasing = False 
        else:
            return False

        if not (1 <= abs(diff) <= 3):
            return False
    return True
     
count = 0

with open("input.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            print(levels)

            if(isSafe(levels)):
                count += 1
                  



print("Result:", count)