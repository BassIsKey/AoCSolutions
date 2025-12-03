
list = []
with open(r"file.txt") as file:
  for data in file.readlines():
    list.append(data.strip())

print(list)

dial = 50
zeroCounter = 0

for x in list:
    if x[0] == "L":
        turns = int(x[1:])

        while turns > 0:
            dial = dial - 1
            turns = turns - 1

            if dial < 0:
                dial = 99
    
        print(dial)

    if x[0] == "R":
        turns = int(x[1:])

        while turns > 0:
            dial = dial + 1
            turns = turns - 1
            
            if dial > 99:
                dial = 0

        print(dial)
    
    if dial == 0:
        zeroCounter += 1


print(f"number of 0s = {zeroCounter}")
print("END")