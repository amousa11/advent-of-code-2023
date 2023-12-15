# Part 1

def hashStr(string):
    stringHash = 0
    for c in string:
        stringHash += ord(c)
        stringHash *= 17
        stringHash = stringHash % 256
    return stringHash


def hashSeq(strs):
    strs = strs.split(',') 
    total = 0
    for string in strs:
        total += hashStr(string) 
    return total

test = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

print(hashSeq(test))
print(hashSeq(open("inputs/day15.txt", "r").read().strip()))

# Part 2

def part2(strs):
    strs = strs.split(',') 
    boxes = [[] for _ in range(256)]
    labels = [[] for _ in range(256)]
    for string in strs:
        if '=' in string:
            [label, lens] = string.split('=')
            ind = hashStr(label)
            if label in labels[ind]:
                replaceIndex = labels[ind].index(label)
                boxes[ind][replaceIndex] = lens
            else:
                boxes[ind].append(lens)
                labels[ind].append(label)
        else:
            label = string[:-1]
            ind = hashStr(label)
            if label in labels[ind]:
                removeInd = labels[ind].index(label)
                boxes[ind].pop(removeInd)
                labels[ind].pop(removeInd)
    total = 0
    for i in range(256):
        box = boxes[i]
        for j, lens in enumerate(box):
            total += (i+1) * int(box[j]) * (j+1)
    return total


print(part2(test))
print(part2(open("inputs/day15.txt").read()))
