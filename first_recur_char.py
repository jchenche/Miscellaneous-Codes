#!/usr/bin/env python3


def first_recur(string):
    '''This program returns the first recurring character'''
    hashmap = {}
    for i in range(len(string)):
        if string[i] in hashmap:
            return string[i]
        else:
            hashmap[string[i]] = i
    return None

if __name__ == "__main__":
    print(first_recur("BCABA"))