# Part 1

north = [-1, 0]
south = [1, 0]
east = [0, 1]
west = [0, -1]

pipes = {
    "|": [north, south],
    "-": [east, west],
    "L": [north, east],
    "J": [north, west],
    "7": [south, west],
    "F": [south, east],
    "S": [north, south, east, west]
}

def getDistanceFromStart(tiles):
    rows = len(tiles)
    cols = len(tiles[0])
    startI, startJ = None, None
    for i in range(rows):
        if startI != None and startJ != None:
            break
        for j in range(cols):
            if tiles[i][j] == 'S':
                startI, startJ = i, j
                break

    stack = [(startI, startJ)]    
    visited = set()
    while stack:
        i, j = stack.pop()
        visited.add((i, j))
        #[[print(tiles[a][b] if a != i or b != j else '#', end=' ' if b < cols-1 else '\n') for b in range(cols)] for a in range(rows)]
        #print()

        for [r, c] in pipes[tiles[i][j]]:
            x, y = i+r, j+c
            if 0 <= x < rows and 0 <= y < cols and (tiles[x][y] in pipes) and (x, y) not in visited:
                stack.append((x, y))
    return len(visited) // 2 

test = """.....
.S-7.
.|.|.
.L-J.
....."""

test2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

print(getDistanceFromStart(test.splitlines()))
print(getDistanceFromStart(test2.splitlines()))
print(getDistanceFromStart(open("inputs/day10.txt", "r").readlines()))

# Part 2

def getInteriorTileCount(tiles):
    rows = len(tiles)
    cols = len(tiles[0])

    # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    # I couldn't figure this one out on my own. I turned to the internet and cheated!
    def isInside(x, y, points):
        inside = False
        j = len(points) - 1 
        for i in range(len(points)):
            assert not (x == points[i][0] and y == points[i][1]) 
            if (points[i][1] > y) != (points[j][1] > y):
                xMinusX1 = x - points[i][0]
                yMinusY1 = y - points[i][1]
                dy = points[j][1] - points[i][1]
                slope = xMinusX1 * dy - (points[j][0] - points[i][0]) * yMinusY1 
                if slope == 0:
                    return False
                if (slope < 0) != (points[j][1] < points[i][1]):
                    inside = not inside
            j = i
        return inside
            

    startI, startJ = None, None
    for i in range(rows):
        if startI != None and startJ != None:
            break
        for j in range(cols):
            if tiles[i][j] == 'S':
                startI, startJ = i, j
                break

    stack = [(startI, startJ)]    
    visited = set()
    while stack:
        i, j = stack.pop()
        visited.add((i, j))

       #[[print(tiles[a][b] if a != i or b != j else '#', end=' ' if b < cols-1 else '\n') for b in range(cols)] for a in range(rows)]
        #print()

        for [r, c] in pipes[tiles[i][j]]:
            x, y = i+r, j+c
            if 0 <= x < rows and 0 <= y < cols and (tiles[x][y] in pipes) and (x, y) not in visited:
                stack.append((x, y))

    pointsInside = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and isInside(i, j, list(visited)):
                pointsInside += 1

    return pointsInside 

test3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

print(getInteriorTileCount(test.splitlines()))
print(getInteriorTileCount(test2.splitlines()))
print(getInteriorTileCount(test3.splitlines()))
print(getInteriorTileCount(test4.splitlines()))
print(getInteriorTileCount(open("inputs/day10.txt", "r").readlines()))
