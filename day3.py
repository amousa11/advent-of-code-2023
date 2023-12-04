test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Part 1

def getSumOfPartNumbers(schematic):
   sum = 0
   numbers = []
   symbolPositions = []
   number = 0
   
   matrix = [['.' for _ in range(len(schematic[0]))] for _ in range(len(schematic))]
   for i in range(len(schematic)):
       matrix[i] = list(schematic[i])[:-1]
       for j in range(len(matrix[i])):
           if matrix[i][j].isdigit():
               number *= 10
               number += int(matrix[i][j])
               matrix[i][j] = len(numbers)
           else:
               if matrix[i][j] != '.':
                   symbolPositions.append((i, j))
               if number != 0:
                   numbers.append(number)
                   number = 0

   while symbolPositions:
        i, j = symbolPositions.pop()
        for r in [-1,0,1]:
            for c in [-1,0,1]:
               x, y = i+r, j+c
               if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]) and type(matrix[x][y]) == int:
                   sum += numbers[matrix[x][y]]
                   numbers[matrix[x][y]] = 0
   return sum

print(getSumOfPartNumbers(test.splitlines()))
print(getSumOfPartNumbers(open("inputs/day3.txt", "r").readlines()))

# Part 2

def getSumOfGearRatios(schematic):
   sum = 0
   numbers = []
   symbolPositions = []
   number = 0
   
   matrix = [['.' for _ in range(len(schematic[0]))] for _ in range(len(schematic))]
   for i in range(len(schematic)):
       matrix[i] = list(schematic[i])[:-1]
       for j in range(len(matrix[i])):
           if matrix[i][j].isdigit():
               number *= 10
               number += int(matrix[i][j])
               matrix[i][j] = len(numbers)
           else:
               if matrix[i][j] == '*':
                   symbolPositions.append((i, j))
               if number != 0:
                   numbers.append(number)
                   number = 0

   while symbolPositions:
        i, j = symbolPositions.pop()
        gearNumberIndexes = set()
        for r in [-1,0,1]:
            for c in [-1,0,1]:
               x, y = i+r, j+c
               if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]) and type(matrix[x][y]) == int:
                   gearNumberIndexes.add(matrix[x][y])
               if len(gearNumberIndexes) > 2:
                   break
        if len(gearNumberIndexes) == 2:
            sum += numbers[gearNumberIndexes.pop()] * numbers[gearNumberIndexes.pop()]
   return sum

print(getSumOfGearRatios(test.splitlines()))
print(getSumOfGearRatios(open("inputs/day3.txt", "r").readlines()))
