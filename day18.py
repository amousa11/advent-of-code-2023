import collections
# Part 1

dir = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0)
}

def getTrenchVolume(digPlan):
    x, y = 0, 0
    points = [] 
    perimeter = 0
    hexToDir = ['R', 'D', 'L', 'U']
    for row in digPlan:
        [_, _, instruction] = row.split()
        distance, direction = instruction[2:7], instruction[7]
        direction = dir[hexToDir[int(direction)]]
        distance = int(distance, base=16)
        x, y = (a + b * distance for a,b in zip((x,y),direction)) 
        perimeter += distance
        points.append((x,y))

    shoelace = 0
    for i in range(len(points)):
        shoelace += points[i][0]*points[i-1][1] - points[i][1]*points[i-1][0]


    return (shoelace + perimeter) // 2 + 1 
            


test = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

print(getTrenchVolume(test.splitlines()))
print(getTrenchVolume(open("inputs/day18.txt","r").readlines()))
