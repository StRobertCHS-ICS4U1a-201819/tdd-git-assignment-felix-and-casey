from statTools import *
import pytest

# Test 1: Sorted:
intList1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# Test 2: Sorted W negatives:
intList2 = [-100, -69, -34, -10, -10, -1, 2, 10, 11, 100]

# Test 3: Non-sorted list:
intList3 = [9, 1, 3, 8, 0, 5, 2, 2, 6, 2, 2]
# sorted = [0, 1, 2, 2, 2, 2, 3, 5, 6, 8, 9]

# Test 4: Non-sorted W negatives:
intList4 = [5, 5, -5, 5, -5, 10, -9, 7, 8, 1, 3]
# sorted = [-9, -5, -5, 1, 3, 5, 5, 5, 7, 8, 10]

# Corner 1: Empty list:
cornerList1 = []

# Corner 2: Multiple mode:
cornerList2 = [-1, 0, 1, 3, 5, 6, 8, 9]

# Corner 3: No lower/upper quartile:
cornerList3 = [0]

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
    assert ([] == mode(cornerList1))

def test_modeC2():
    assert ([-1, 0, 1, 3, 5, 6, 8, 9] == mode(cornerList2))

def test_modeC3():
    assert ([0] == mode(cornerList3))

# Median Tests:
def test_medianB1():
    assert (6 == median(intList1))

def test_medianB2():
    assert (-10 == median(intList2))

def test_medianB3():
    assert (2 == median(intList3))

def test_medianB4():
    assert (5 == median(intList4))

def test_medianC1():
    assert ("This is an empty list" == median(cornerList1))

def test_meidanC2():
    assert (3 == median(cornerList2))
# Range Tests:
# Lower Quartile Tests:
# Upper Quartile Tests:
# Variance Tests:
# Standard Deviation Tests: