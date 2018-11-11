# Central Tendency Functions
import math
# Sum of all terms / # of terms
def mean(intList): # Refactor this one
    if (len(intList) == 0): return 0
    return sum(intList) / len(intList)

# Number that appears the most
def mode(intList):
    try:
        counter = {}
        for i in intList:
            if (i in counter.keys()): counter[i] = counter.get(i) + 1
            else: counter[i] = 1
        maxOcc = counter.get(intList[0])
        for i in counter:
            if (counter.get(i) > maxOcc): maxOcc = counter.get(i)
        returnList = []
        for i in counter:
            if (counter.get(i) == maxOcc): returnList.append(i)
        return returnList
    except: return None

# Middle number of the sorted list
def median(intList):
    intList.sort()
    if len(intList) == 0:
        return "This is an empty list"
    elif len(intList) % 2 == 0:
        return (intList[int(len(intList)/2)] + intList[int(len(intList)/2-1)]) / 2
    else:
        return intList[int((len(intList)+1)/2)-1]

# Spread Functions

# Largest - Smallest
def range(intList):
    intList.sort()
    if len(intList) == 0:
        return "This is an empty list"
    else:
        return intList[len(intList)-1] - intList[0]


# Median of the numbers below the median
def lwrQuartile(intList):
    intList.sort()
    median = 0
    if len(intList) == 0:
        return "This is an empty list"
    elif len(intList) == 1:
        return intList[0]
    elif len(intList) % 2 == 0:
        median += len(intList)/2 - 1
        if len(intList[:int(median)]) % 2 == 0:
            return intList[int(len(intList[:int(median)])/2 - 1)]
        else:
            return intList[int(len(intList[:int(median)]) / 2)]
    else:
        median += (len(intList)+1)/2 - 1
        if len(intList[:int(len(intList) / 2 - 1)]) % 2 == 0:
            return intList[int(len(intList[:int(len(intList) / 2 - 1)]) / 2)]

# Median of the numbers above the median
def uprQuartile(intList):
    try:
        intList.sort()
        return median(intList[(len(intList)-1)//2 + 1:])
    except: return 'This is an empty list'

# Average of the squares of the differences of each number from the mean
def variance(intList):
    try:
        sum = 0
        for i in intList:
            sum += (i - mean(intList))**2
        return (sum / len(intList))
    except: return "This is an empty list"

# Square root of the variance
def stdDeviation(intList):
    try:
        return math.sqrt(variance(intList))
    except: return 'This is an empty list'
