data = open("2023-1-1.txt", "r").readlines()
calibrationValues = []

for line in data: # read each string in the list
    lineReverse = line[::-1]
    number = ""
    for char in line: # read each character in the line
        if char.isnumeric():
            number += char
            break
    for char in lineReverse: # read each character in the line
        if char.isnumeric():
            number += char
            break
    calibrationValues.append(int(number))

print(sum(calibrationValues))