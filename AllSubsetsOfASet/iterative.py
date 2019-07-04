#!/usr/bin/python

import itertools

def all_subsets(given_array):
    for i in range(len(given_array) + 1):
        print list(itertools.combinations(given_array, i))

if __name__ == "__main__":
    array = range(1, 5)
    all_subsets(array)
    
