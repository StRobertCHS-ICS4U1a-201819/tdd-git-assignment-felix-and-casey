"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:		
This program contains the central tendency functions.

Authors:		Yang.F, Li. C

Created:		11/11/2018
------------------------------------------------------------------------------
"""

def mean(intList):
    ''' Finds the sum of all the terms / # of terms

        :param intList: The list of integers to find the mean from
        :return: The mean
    '''
    try:
        return sum(intList) / len(intList)
    except: return 0

def mode(intList):
    ''' Finds the number that appears the most in a list of numbers

        :param intList: The list of integers to find the mode from
        :return: The mode
    '''
    try:
        # Initializing a dictionary to store values
        counter = {}
        # Counts the occurrences of each number in intList
        for i in intList:
            if (i in counter.keys()): counter[i] = counter.get(i) + 1
            else: counter[i] = 1
        maxOcc = counter.get(intList[0])
        # Checks for the maximum number of occurrences
        for i in counter:
            if (counter.get(i) > maxOcc): maxOcc = counter.get(i)
        returnList = []
        # Appends the keys with the max occurrences into a return list
        for i in counter:
            if (counter.get(i) == maxOcc): returnList.append(i)
        return returnList
    except: return None

def median(intList):
    ''' Finds the middle number of a sorted list

        :param intList: The list of integers to find the median from
        :return: The median
    '''
    intList.sort()
    if len(intList) == 0:
        return "This is an empty list"
    elif len(intList) % 2 == 0:
        return (intList[int(len(intList) / 2)] + intList[int(len(intList) / 2 - 1)]) / 2
    else:
        return intList[int((len(intList) + 1) / 2) - 1]

def range(intList):
    ''' Finds the difference between the largest and smallest number in a list

        :param intList: The list of integers to find the range from
        :return: The range
    '''
    intList.sort()
    if len(intList) == 0:
        return "This is an empty list"
    else:
        return intList[len(intList) - 1] - intList[0]

def lwrQuartile(intList):
    ''' Finds the median of the set of numbers below the median

        :param intList: The list of integers to find the lower quartile from
        :return: The lower quartile
    '''
    intList.sort()
    median = 0
    if len(intList) == 0:
        return "This is an empty list"
    elif len(intList) == 1:
        return intList[0]
    elif len(intList) % 2 == 0:
        median += len(intList) / 2 - 1
        if len(intList[:int(median)]) % 2 == 0:
            return intList[int(len(intList[:int(median)]) / 2 - 1)]
        else:
            return intList[int(len(intList[:int(median)]) / 2)]
    else:
        median += (len(intList) + 1) / 2 - 1
        if len(intList[:int(len(intList) / 2 - 1)]) % 2 == 0:
            return intList[int(len(intList[:int(len(intList) / 2 - 1)]) / 2)]

def uprQuartile(intList):
    ''' Finds the median of the set of numbers above the median

        :param intList: The list of integers to find the upper quartile from
        :return: The upper quartile
    '''
    try:
        intList.sort()
        return median(intList[(len(intList) - 1) // 2 + 1:])
    except: return 'This is an empty list'

def variance(intList):
    ''' Finds the average of the squares of the differences of each number from the mean

        :param intList: The list of integers to find the variance from
        :return: The variance
    '''
    try:
        sum = 0
        # Adding the difference of each number to the mean squared
        for i in intList:
            sum += (i - mean(intList)) ** 2
        # Averaging the sum variable
        return (sum / len(intList))
    except: return "This is an empty list"

def stdDeviation(intList):
    ''' Finds the square root of the variance

        :param intList: The list of integers to find the standard deviation from
        :return: The standard deviation
    '''
    try:
        return variance(intList) ** 0.5
    except: return 'This is an empty list'
