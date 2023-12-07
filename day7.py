import collections
import functools
# Part 1 

def classifyHand(hand):
    fiveOfAKind = (False, "")
    fourOfAKind = (False, "")
    fullHouse = (False, "", "")
    threeOfAKind = (False, "")
    twoPair = (False, "", "")
    onePair = (False, "")
    highCard = (False, "")

    count = collections.defaultdict(int)
    for card in hand:
       count[card] += 1
       highCard = (True, card)
       match count[card]:
           case 2:
               if onePair[0]:
                   twoPair = (True, onePair[1], card)
               else:
                   onePair = (True, card)

               if threeOfAKind[0]:
                   fullHouse = (True, threeOfAKind[1], card)
           case 3:
               if twoPair[0]:
                   a, b = twoPair[1] if twoPair[1] != card else twoPair[2], card
                   fullHouse = (True, a, b)
               threeOfAKind = (True, card)
           case 4:
               fourOfAKind = (True, card)
           case 5:
               fiveOfAKind = (True, card)
    
    if fiveOfAKind[0]:
        return 6
    if fourOfAKind[0]:
        return 5
    if fullHouse[0]:
        return 4
    if threeOfAKind[0]:
        return 3
    if twoPair[0]:
        return 2
    if onePair[0]:
        return 1
    if highCard[0]:
        return 0
    return -1

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
order = {card: len(cards) - i for i, card in enumerate(cards)}


def compareHands(a, b):
    a = a[0]
    b = b[0]
    aClass = classifyHand(a)
    bClass = classifyHand(b)

    if aClass == bClass:
        for aCard, bCard in zip(a, b):
            aOrd = order[aCard]
            bOrd = order[bCard]

            if aOrd == bOrd:
                continue
            return aOrd - bOrd
    return aClass - bClass
            

def getTotalWinnings(handsAndBids):
    handsAndBids = map(lambda x: x.split(), handsAndBids)
    handsAndBids = sorted(handsAndBids, key=functools.cmp_to_key(compareHands))
    
    totalWinnings = 0
    for i, (hand, bid) in enumerate(handsAndBids):
        totalWinnings += int(bid) * (i+1)
    return totalWinnings


test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

print(getTotalWinnings(test.splitlines()))
print(getTotalWinnings(open("inputs/day7.txt", "r").readlines()))

# Part 2

def classifyHandWithJoker(hand):
    fiveOfAKind = (False, "")
    fourOfAKind = (False, "")
    fullHouse = (False, "", "")
    threeOfAKind = (False, "")
    twoPair = (False, "", "")
    onePair = (False, "")
    highCard = (False, "")

    count = collections.defaultdict(int)
    for card in hand:
       count[card] += 1
       highCard = (True, card)
       if card == "J":
           continue
       match count[card]:
           case 2:
               if onePair[0]:
                   twoPair = (True, onePair[1], card)
               else:
                   onePair = (True, card)

               if threeOfAKind[0]:
                   fullHouse = (True, threeOfAKind[1], card)
           case 3:
               if twoPair[0]:
                   a, b = twoPair[1] if twoPair[1] != card else twoPair[2], card
                   fullHouse = (True, a, b)
               threeOfAKind = (True, card)
           case 4:
               fourOfAKind = (True, card)
           case 5:
               fiveOfAKind = (True, card)
   
    if fiveOfAKind[0]:
        return 6 
    if fourOfAKind[0]:
        if count["J"] == 1:
            return 6
        return 5 
    if fullHouse[0]:
        return 4
    if threeOfAKind[0]:
        if count["J"] == 1:
            return 5
        if count["J"] == 2:
            return 6
        return 3
    if twoPair[0]:
        if count["J"] == 1:
            return 4
        return 2
    if onePair[0]:
        if count["J"] == 1:
            return 3
        elif count["J"] == 2:
            return 5
        elif count["J"] == 3:
            return 6
        return 1
    if highCard[0]:
        if count["J"] == 1:
            return 1
        elif count["J"] == 2:
            return 3
        elif count["J"] == 3:
            return 5
        elif count["J"] == 4:
            return 6
        elif count["J"] == 5:
            return 6
        return 0
    return -1

cardsWithJoker = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
orderWithJoker = {card: len(cardsWithJoker) - i + 1 for i, card in enumerate(cardsWithJoker)}

def compareHandsWithJoker(a, b):
    a = a[0]
    b = b[0]
    aClass = classifyHandWithJoker(a)
    bClass = classifyHandWithJoker(b)

    if aClass == bClass:
        for aCard, bCard in zip(a, b):
            aOrd = orderWithJoker[aCard]
            bOrd = orderWithJoker[bCard]

            if aOrd == bOrd:
                continue
            return aOrd - bOrd
    return aClass - bClass
            

def getTotalWinningsWithJoker(handsAndBids):
    handsAndBids = map(lambda x: x.split(), handsAndBids)
    handsAndBids = sorted(handsAndBids, key=functools.cmp_to_key(compareHandsWithJoker))
    totalWinnings = 0
    for i, (hand, bid) in enumerate(handsAndBids):
        classification = classifyHandWithJoker(hand)
        totalWinnings += int(bid) * (i+1)
    return totalWinnings

print(getTotalWinningsWithJoker(test.splitlines()))
print(getTotalWinningsWithJoker(open("inputs/day7.txt", "r").readlines()))
