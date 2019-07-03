#!/usr/bin/env python

def all_subsets(given_array):
    subset = [None] * len(given_array)
    helper(given_array, subset, 0)

def helper(given_array, subset, index):
    if index == len(given_array):
        print subset
    else:
        subset[index] = None
        helper(given_array, subset, index + 1)
        subset[index] = given_array[index]
        helper(given_array, subset, index + 1)

if __name__ == "__main__":
    array = range(1, 5)
    all_subsets(array)
