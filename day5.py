
# Part 1
def mapToNext(seeds, ranges):
    for i, cur in enumerate(seeds):
        for [destStart, sourceStart, n] in ranges:
            if sourceStart <= cur < sourceStart + n:
                seeds[i] = destStart + (cur - sourceStart)
                break


def getLowestLocationSeed(input):
    seeds = [int(x) for x in input.pop(0).split(" ")[1:]]
    ranges = []
    buildRanges = False
    for line in input:
        if len(line.strip()) == 0:
            mapToNext(seeds, ranges)
            buildRanges = False
            ranges = []
            continue
        if buildRanges:
            [destStart, sourceStart, n] = line.strip().split(" ")
            ranges.append([int(destStart), int(sourceStart), int(n)])
        if '-' in line:
            buildRanges = True

    mapToNext(seeds, ranges)
    return min(seeds) 
test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# print(getLowestLocationSeed(test.splitlines()))
# print(getLowestLocationSeed(open("inputs/day5.txt", "r").readlines()))
# Part 2

def mapToNextRange(seedRanges, mapRanges):
    newSeedRanges = {}
    i = 0
    while i < len(seedRanges):
        seedStart, seedLength = seedRanges[i]
        intersections = 0
        for [destStart, sourceStart, n] in mapRanges:
            if sourceStart <= seedStart < sourceStart + n:
                intersections += 1
                newLength = min(sourceStart + n - seedStart, seedLength) 
                newSeedRanges[destStart + (seedStart - sourceStart)] = newLength
                if n < seedLength:
                    seedRanges.append((seedStart + newLength, seedLength - newLength))
            elif seedStart <= sourceStart < seedStart + seedLength:
                intersections += 1
                if seedStart < sourceStart:
                    seedRanges.append((seedStart, sourceStart - seedStart))
                if sourceStart + n < seedStart + seedLength:
                    seedRanges.append((sourceStart + n, seedStart + seedLength - sourceStart - n))
                newSeedRanges[destStart] = min(n, seedStart + seedLength - sourceStart) 
 
        if intersections == 0:
            newSeedRanges[seedStart] = seedLength
        i += 1
    return list(newSeedRanges.items())

def getLowestLocationSeedWithRanges(input):
    seeds = [int(x) for x in input.pop(0).split(" ")[1:]]
    seeds = list(zip(seeds[::2], seeds[1::2]))
    seeds.sort(key=lambda x:x[0])
    ranges = []
    buildRanges = False
    for line in input:
        if len(line.strip()) == 0:
            seeds = mapToNextRange(seeds, ranges)
            buildRanges = False
            ranges = []
            continue
        if buildRanges:
            [destStart, sourceStart, n] = line.strip().split(" ")
            ranges.append([int(destStart), int(sourceStart), int(n)])
        if '-' in line:
            buildRanges = True

    seeds = mapToNextRange(seeds, ranges)
    return min(seeds, key=lambda x: x[0]) 

print(getLowestLocationSeedWithRanges(test.splitlines()))
print(getLowestLocationSeedWithRanges(open("inputs/day5.txt", "r").readlines()))
