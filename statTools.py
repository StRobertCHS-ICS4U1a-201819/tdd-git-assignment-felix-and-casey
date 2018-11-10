# Central Tendency Functions

# Sum of all terms / # of terms
def mean(intList):
    sum = 0
    for i in intList:
        sum += i
    if (len(intList) == 0): return 0
    return sum / len(intList)

# Number that appears the most
def mode(intList):
    if intList == []: return []
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

# Middle number of the sorted list
def median(intList):
    intList.sort()
    if len(intList) == 0:
        return "This is an empty list"
    elif len(intList) == 1:
        return intList[0]
    elif len(intList) % 2 == 0:
        return intList[int(len(intList)/2 - 1)]
    else:
        return intList[int((len(intList)+1)/2)-1]

# Spread Functions

# Largest - Smallest
def range(intList):
    return 1

# Median of the numbers below the median
def lwrQuartile(intList):
    return 1

# Median of the numbers above the median
def uprQuartile(intList):
    return 1

# Average of the squares of the differences of each number from the mean
def variance(intList):
    return 1

# Square root of the variance
def stdDeviation(intList):
    return 1
