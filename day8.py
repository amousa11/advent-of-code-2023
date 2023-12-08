import collections
import math
# Part 1

def getStepsToZ(input):
    path = list(map(lambda x: 0 if x == 'L' else 1, input[0].strip()))

    step = {}
    for line in input[2:]:
        [node, edges] = line.split(" = ")
        i = edges.find("(") + 1
        j = edges.find(")")
        edges = edges[i: j].split(", ")
        assert len(edges) == 2
        assert len(edges[0]) == 3
        assert len(edges[1]) == 3
        assert len(node) == 3
        step[node] = edges

    stack = ["AAA"]
    steps = -1
    i = 0
    while stack:
       node = stack.pop()
       steps += 1

       if node == "ZZZ":
           return steps

       currentStep = path[i]
       i = (i+1) % len(path)

       stack.append(step[node][currentStep]) 

    return -1


test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

print(getStepsToZ(test.splitlines()))
print(getStepsToZ(test2.splitlines()))
print(getStepsToZ(open("inputs/day8.txt", "r").readlines()))

# Part 2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def getStepsToAllZ(input):
    path = list(map(lambda x: 0 if x == 'L' else 1, input[0].strip()))

    step = {}
    nodes = [] 
    for line in input[2:]:
        [node, edges] = line.split(" = ")
        i = edges.find("(") + 1
        j = edges.find(")")
        edges = edges[i: j].split(", ")
        assert len(edges) == 2
        assert len(edges[0]) == 3
        assert len(edges[1]) == 3
        assert len(node) == 3
        step[node] = edges

        if node[2] == 'A':
            nodes.append(node)
   
    def nextStep(node, i):
        currentStep = path[i]
        node = step[node][currentStep] 
        return node, (i+1) % len(path) 

    steps = 0 
    i = 0
    distances = []
    for node in nodes:
        distance = 1
        node, i = nextStep(node, i)
        while node[2] != 'Z':
            distance += 1
            node, i = nextStep(node, i)
        distances.append(distance)
    return math.lcm(*distances) 

test3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

print(getStepsToAllZ(test3.splitlines()))
print(getStepsToAllZ(open("inputs/day8.txt", "r").readlines()))
