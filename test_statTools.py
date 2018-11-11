from statTools import *
import pytest


# Test 1: Sorted:
intList1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
# Variance Should be: 8.0165289256198

# Test 2: Sorted W negatives:
intList2 = [-100, -69, -34, -10, -10, -1, 2, 10, 11, 100]
# Variance should be: 2532.29

# Test 3: Non-sorted list:
intList3 = [9, 1, 3, 8, 0, 5, 2, 2, 6, 2, 2]
# Variance Should be: 7.8677685950413

# Test 4: Non-sorted W negatives:
intList4 = [5, 5, -5, 5, -5, 10, -9, 7, 8, 1, 3]
# Variance Should be: 33.834710743802

# Corner 1: Empty list:
cornerList1 = []
# Variance should be: "This is an empty list"

# Corner 2: Multiple mode:
cornerList2 = [-1, 0, 1, 3, 5, 6, 8, 9]
# Variance should be: 12.109375

# Corner 3: No lower/upper quartile:
cornerList3 = [0]
# Variance should be: 0

# Completed Tests
'''
# Mean Tests:
def test_meanB1():
    assert (63/11 == mean(intList1))

def test_meanB2():
    assert (-10.1 == mean(intList2))

def test_meanB3():
    assert (40/11 == mean(intList3))

def test_meanB4():
    assert (25/11 == mean(intList4))

def test_meanC1():
    assert (0 == mean(cornerList1))

def test_meanC2():
    assert (31/8 == mean(cornerList2))

def test_meanC3():
    assert (0 == mean(cornerList3))

# Mode Tests:
def test_modeB1():
    assert ([8] == mode(intList1))

def test_modeB2():
    assert ([-10] == mode(intList2))

def test_modeB3():
    assert ([2] == mode(intList3))

def test_modeB4():
    assert ([5] == mode(intList4))

def test_modeC1():
    assert (None == mode(cornerList1))

def test_modeC2():
    assert ([-1, 0, 1, 3, 5, 6, 8, 9] == mode(cornerList2))

def test_modeC3():
    assert ([0] == mode(cornerList3))
# Median Tests:
def test_medianB1():
    assert (6 == median(intList1))

def test_medianB2():
    assert (-11/2 == median(intList2))

def test_medianB3():
    assert (2 == median(intList3))

def test_medianB4():
    assert (5 == median(intList4))

def test_medianC1():
    assert ("This is an empty list" == median(cornerList1))

def test_medianC2():
    assert (4 == median(cornerList2))

def test_medianC3():
    assert (0 == median(cornerList3))
# Range Tests:
def test_rangeB1():
    assert (9 == range(intList1))

def test_rangeB2():
    assert (200 == range(intList2))

def test_rangeB3():
    assert (9 == range(intList3))

def test_rangeB4():
    assert (19 == range(intList4))

def test_rangeC1():
    assert ("This is an empty list" == range(cornerList1))

def test_rangeC2():
    assert (10 == range(cornerList2))

def test_rangeC3():
    assert (0 == range(cornerList3))

# Lower Quartile Tests:
def test_lwrQuartileB1():
    assert (3 == lwrQuartile(intList1))

def test_lwrQuartileB2():
    assert (-69 == lwrQuartile(intList2))

def test_lwrQuartileB3():
    assert (2 == lwrQuartile(intList3))

def test_lwrQuartileB4():
    assert (-5 == lwrQuartile(intList4))

def test_lwrQuartileC1():
    assert ("This is an empty list" == lwrQuartile(cornerList1))

def test_lwrQuartileC2():
    assert (0 == lwrQuartile(cornerList2))

def test_lwrQuartileC3():
    assert (0 == lwrQuartile(cornerList3))
# Upper Quartile Tests:
def test_uprQuartileB1():
    assert (8 == uprQuartile(intList1))

def test_uprQuartileB2():
    assert (10 == uprQuartile(intList2))

def test_uprQuartileB3():
    assert (6 == uprQuartile(intList3))

def test_uprQuartileB4():
    assert (7 == uprQuartile(intList4))

def test_uprQuartileC1():
    assert ('This is an empty list' == uprQuartile(cornerList1))

def test_uprQuartileC2():
    assert (7 == uprQuartile(cornerList2))

def test_uprQuartileC3():
    assert ('This is an empty list' == uprQuartile(cornerList3))


# Variance Tests:
def test_varianceB1():
    assert (8.016528925619836 == variance(intList1))

def test_varianceB2():
    assert (2532.29 == variance(intList2))

def test_varianceB3():
    assert (7.86776859504132 == variance(intList3))

def test_varianceB4():
    assert (33.83471074380165 == variance(intList4))

def test_varianceC1():
    assert ("This is an empty list" == variance(cornerList1))

def test_varianceC2():
    assert (12.109375 == variance(cornerList2))

def test_varianceC3():
    assert (0 == variance(cornerList3))
'''

# Standard Deviation Tests:
def test_stdDeviationB1():
    assert (2.831347545890443 == stdDeviation(intList1))

def test_stdDeviationB2():
    assert (50.321864035426984 == stdDeviation(intList2))

def test_stdDeviationB3():
    assert (math.sqrt(7.86776859504132) == stdDeviation(intList3))

