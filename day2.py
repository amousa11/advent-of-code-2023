# Part 1

def getSumOfPossibleGameIds(games):
    sum = 0
    for game in games:
        [gameN, rounds] = game.split(':')
        gameId = int(gameN[5:])
        validGame = True

        for round in rounds.split(';'):
            cubesRemaining = { "red": 12, "green": 13, "blue": 14 }
            cubes = round.split(',') 
            for cube in cubes:
                [count, color] = cube.strip().split(' ')
                cubesRemaining[color] -= int(count)
                if cubesRemaining[color] < 0:
                    validGame = False
                    break
            if not validGame:
                break
        if validGame:
            sum += gameId
    return sum

print(getSumOfPossibleGameIds("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()))
print(getSumOfPossibleGameIds(open("inputs/day2.txt").readlines()))

# Part 2 

def getSumOfPowers(games):
    total = 0
    for game in games:
        [gameN, rounds] = game.split(':')
        gameId = int(gameN[5:])
        minCubes = { "red": 0, "green": 0, "blue": 0}

        for round in rounds.split(';'):
            cubes = round.split(',') 
            for cube in cubes:
                [count, color] = cube.strip().split(' ')
                minCubes[color] = max(minCubes[color], int(count))
        total += minCubes['red'] * minCubes['blue'] * minCubes['green']
    return total 

print(getSumOfPowers("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()))
print(getSumOfPowers(open("inputs/day2.txt").readlines()))
