
# Part 1

inputs = open("./inputs/day1.txt", 'r')


def getCalibrationValue(lines):    
    sum = 0
    
    for line in lines:
        i = 0
        j = len(line) - 1
        while i < len(line) and not line[i].isdigit():
            i+=1
        while j >= 0 and not line[j].isdigit():
            j-=1

        calibrationValue = int(line[i]) * 10 + int(line[j])
        sum += calibrationValue
    
    return sum

testCase = """1abc2
                    pqr3stu8vwx
                    a1b2c3d4e5f
                    treb7uchet"""

# print(getCalibrationValue(testCase.splitlines()))
# print(getCalibrationValue(inputs.readlines()))

# Part 2

class TrieNode:
    def __init__(self, char, terminus):
        self.terminus = terminus 
        self.char = char
        self.children = [None for _ in range(26)]
    
    def getNext(self, char):
        i = ord(char) - ord('a')
        if i < 0 or i >= 26:
            return None
        return self.children[i]

class Trie: 
    def __init__(self):
       self.root = TrieNode('#', False)

    def add_word(self, word):
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
               node.children[i] = TrieNode(c, False) 
            node = node.children[i]
        node.terminus = True
   
wordToNumber = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}



def getCalibrationValuePart2(lines):
    sum = 0
    t = Trie()

    for key in wordToNumber.keys():
        t.add_word(key)
    
    root = t.root
    for line in lines:
        first = 0
        last = 0
        for i in range(len(line)):
            number = -1
            c = line[i]
            if c.isdigit():
                number = int(c)
            else:
                node = root
                j = i
                while j < len(line) and node and not node.terminus:
                    node = node.getNext(line[j])
                    j += 1
                if node and node.terminus:
                    number = wordToNumber[line[i:j]]
            if number > 0:
                if not first:
                    first = number
                else:
                    last = number
        if last == 0:
            last = first
        sum += first * 10 + last
    return sum

test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
print(getCalibrationValuePart2(test.splitlines()))
print(getCalibrationValuePart2(inputs.readlines()))
