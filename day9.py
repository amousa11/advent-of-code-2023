# Part 1

def getDiffSequence(arr):
    return [arr[i] - arr[i-1] for i in range(1, len(arr))]

def extrapolateOasis(reports):
    totalExtrapolations = 0
    for report in reports:
        values = list(map(int, report.split()))

        stack = [values[-1]]
        diff = getDiffSequence(values)
        while sum(diff) != 0:
            stack.append(diff[-1])
            diff = getDiffSequence(diff)
        totalExtrapolations += sum(stack)
    return totalExtrapolations 

test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

print(extrapolateOasis(test.splitlines()))
print(extrapolateOasis(open("inputs/day9.txt", "r").readlines()))

# Part 2
def backwardsExtrapolateOasis(reports):
    totalExtrapolations = 0
    for report in reports:
        values = list(map(int, reversed(report.split())))

        stack = [values[-1]]
        diff = getDiffSequence(values)
        while sum(diff) != 0:
            stack.append(diff[-1])
            diff = getDiffSequence(diff)
        totalExtrapolations += sum(stack)
    return totalExtrapolations 

print(backwardsExtrapolateOasis(test.splitlines()))
print(backwardsExtrapolateOasis(open("inputs/day9.txt", "r").readlines()))
