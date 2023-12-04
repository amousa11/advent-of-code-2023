# Part 1
def getSumOfPoints(cards):
    sum = 0
    for card in cards:
        [leftCard, numbers] = card.split("|")
        [_, winningNumbers] = leftCard.split(":")
        winningNumbers = set([x for x in winningNumbers.strip().split(" ") if len(x) > 0])
        numbers = [x for x in numbers.strip().split(" ") if len(x) > 0]
        matches = 0
        for number in numbers:
            if number in winningNumbers:
               matches += 1
               winningNumbers.remove(number)
        points = 2 ** (matches - 1) if matches > 0 else 0
        sum += points
    return sum

print(getSumOfPoints("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()))
print(getSumOfPoints(open("inputs/day4.txt", "r").readlines()))

# Part 2
def getMatches(card):
    [leftCard, numbers] = card.split("|")
    [_, winningNumbers] = leftCard.split(":")
    winningNumbers = set([x for x in winningNumbers.strip().split(" ") if len(x) > 0])
    numbers = [x for x in numbers.strip().split(" ") if len(x) > 0]
    matches = 0
    for number in numbers:
        if number in winningNumbers:
           matches += 1
           winningNumbers.remove(number)
    return matches

def getSumOfScratchcards(cards):
    cardCounts = {}
    scratchcards = 0
    for i, card in enumerate(cards):
        cardId = i+1
        if cardId not in cardCounts:
            cardCounts[cardId] = 1
        else:
            cardCounts[cardId] += 1
        matches = getMatches(card) 
        for j in range(1, matches+1):
            if cardId+j not in cardCounts:
                cardCounts[cardId+j] = 0
            cardCounts[cardId+j] += cardCounts[cardId]
        scratchcards += cardCounts[cardId]
        del cardCounts[cardId]
    return scratchcards 

print(getSumOfScratchcards("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()))
print(getSumOfScratchcards(open("inputs/day4.txt", "r").readlines()))



