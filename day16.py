# Part 1

def step(p, v):
    x = p[0] + v[0]
    y = p[1] + v[1]
    return ((x,y), v)

def debugTiles(energized, r, c):
    debug = [['.' for _ in range(c)] for _ in range(r)]
    for x, y in energized:
        debug[x][y] = '#'
    [print("".join(row)) for row in debug]


def countEnergized(tiles, p0, v0):
    energized = set()
    seen = set()
    r = len(tiles)
    c = len(tiles[0])
    inBounds = lambda p: 0 <= p[0] < r and 0 <= p[1] < c
    p = (0,-1)
    v = (0,1)
    stack = [(p0,v0)]
    while stack:
        p, v = stack.pop()
        if (p,v) in seen:
            continue
        seen.add((p,v))
        p, v = step(p, v)
        if not inBounds(p):
            continue
        space = tiles[p[0]][p[1]]
        if space == '.' or (space == '-' and v[1] != 0) or (space == '|' and v[0] != 0):
            stack.append((p,v))
        elif space == '/':
            p, v = p, (-v[1], -v[0])
            stack.append((p,v))
        elif space == "\\":
            p, v = p, (v[1], v[0])
            stack.append((p,v))
        elif space == '-':
            v1 = (0, -1)
            v2 = (0, 1)
            stack.append((p,v1))
            stack.append((p,v2))
        elif space == '|':
            v1 = (1,0)
            v2 = (-1,0)
            stack.append((p,v1))
            stack.append((p,v2))
    return len({x[0] for x in seen}) - 1

test = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

print(countEnergized(test.splitlines(), (0,-1), (0,1)))
print(countEnergized(open("inputs/day16.txt", "r").readlines(), (0,-1), (0,1)))

# Part 2 

def getMaxEnergized(tiles):
   energized = 0
   r = len(tiles)
   c = len(tiles[0])
   for i in range(r):
       energized = max(energized, countEnergized(tiles, (i,-1), (0,1)))
       energized = max(energized, countEnergized(tiles, (i,r), (0,-1)))
   for j in range(c):
       energized = max(energized, countEnergized(tiles, (-1,j), (1,0)))
       energized = max(energized, countEnergized(tiles, (c,j), (-1,0)))
   return energized


print(getMaxEnergized(test.splitlines()))
print(getMaxEnergized(open("inputs/day16.txt", "r").readlines()))

