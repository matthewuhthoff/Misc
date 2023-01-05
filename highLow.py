import random

runLength = 0
rightCount = 0
wrongCount = 0



for i in range(1000000):
    weights = [
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4
    ]
    cards = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13
    ]

    index = random.choices(cards, weights)
    index = index[0]
    weights[index - 1] = weights[index - 1] - 1
    prevCard = index
    
    for j in range(51):
        index = random.choices(cards, weights)
        index = index[0]
        
        lower = 0
        higher = 0
        for k in range(1, 13):
            if k <= prevCard:
                lower = lower + weights[k]
            else:
                higher = higher + weights[k]
        if lower > higher and prevCard > index:
            rightCount = rightCount + 1
        elif higher > lower and index > prevCard:
            rightCount = rightCount + 1
        else:
            wrongCount = wrongCount + 1
        
        weights[index - 1] = weights[index - 1] - 1

        # if prevCard > 7 and index < prevCard:
        #    rightCount = rightCount + 1
        # elif prevCard < 7 and index > prevCard:
        #    rightCount = rightCount + 1
        # else:
        #    wrongCount = wrongCount + 1




rightCount = rightCount / 1000000
wrongCount = wrongCount / 1000000
print("right: " + str(rightCount))
print("wrong: " + str(wrongCount))