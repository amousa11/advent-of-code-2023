# Part 1

"""
Time:      7  15   30
Distance:  9  40  200

(T - x) * x = f(x, T) = Tx - x^2
f'(x, T) = T - 2x

T  Max Dist
0  0
1  6 = (7 - 1) * 1
2  10 = (7 - 2) * 2
3  12 = (7 - 3) * 3
4  12 = (7 - 4) * 4
5  10 = (7 - 5) * 5
6  6
7  0

T Max Dist
0  0
1  14 = (15 - 1) * 1
2  26 = (15 - 2) * 2
3  36 = (15 - 3) * 3
4  44 = (15 - 4) * 4
5  50 = (15 - 5) * 5
6  54 = (15 - 6) * 6
7  56 = (15 - 7) * 7
8  56 = (15 - 8) * 8
9  ... 
"""

def getProductOfNumWaysToWin(timeAndDistance):
    [time, distance] = timeAndDistance
    time = map(int, time.split(":")[1].strip().split())
    distance = map(int, distance.split(":")[1].strip().split())
    product = 1

    for t, d in zip(time, distance):
        i = t // 2
        ways = 0
        while i > 0:
            if i * (t-i) > d:
                ways += 1
            else:
                break
            i -= 1
        product *= ways * 2 - ((t+1) % 2)
    return product

test = """Time:      7  15   30
Distance:  9  40  200
"""

print(getProductOfNumWaysToWin(test.splitlines()))
print(getProductOfNumWaysToWin(open("inputs/day6.txt", "r").readlines()))

# Part 2


def getNumWaysToWin(timeAndDistance):
    [time, distance] = timeAndDistance
    t = int("".join(time.split(":")[1].strip().split()))
    d = int("".join(distance.split(":")[1].strip().split()))
    i = t // 2
    ways = 0
    while i > 0:
        if i * (t-i) > d:
            ways += 1
        else:
            break
        i -= 1
    return ways * 2 - ((t+1) % 2)

print(getNumWaysToWin(test.splitlines()))
print(getNumWaysToWin(open("inputs/day6.txt", "r").readlines()))


