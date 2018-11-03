from statTools import *
import pytest

# Test 1: Sorted:
intList1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# Test 2: Sorted W negatives:
intList2 = [-100, -69, -34, -10, -10, -1, 2, 10, 11, 100]

# Test 3: Non-sorted list:
intList3 = [9,1,3, 8, 0, 5, 2, 2, 6, 2, 2]

# Test 4: Non-sorted W negatives:
intList4 = [5, 5, -5, 5, -5, 10, -9, 7, 8, 1, 3]

# Corner 1: Empty list:
cornerList1 = []

# Corner 2: Multiple mode:
cornerList2 = [-1, 0, 1, 3, 5, 6, 8, 9]

# Corner 3: No lower/upper quartile:
cornerList3 = [0]

# Testing Methods:
def test_meanB1():
    assert (5.5 == mean(intList1))

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