#!/usr/bin/env python3

def first_missing_integer(array):
    '''This program finds the first missing positive integer'''
    hashmap = {}
    for x in array:
        hashmap[x] = x
    first_missing = 1
    while first_missing in hashmap:
        first_missing += 1
    return first_missing

if __name__ == "__main__":
    print(first_missing_integer([1,2,3,6,8,9,11]))