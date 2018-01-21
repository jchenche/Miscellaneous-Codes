#!/usr/bin/env python3

import random
import argparse as ap
import os
import re
import math

def fib(n, memoization):
    if memoization[n] != None:
        return memoization[n]
    if n == 0:
        value = 0
        memoization[0] = 0
    elif n == 1:
        value = 1
        memoization[1] = 1
    else:
        value = fib(n-1, memoization) + fib(n-2, memoization)
        memoization[n] = value
    return value

def main():
    n = int(input("Enter the nth fibonacci (starting from the 0th): "))
    memoization = [None]*(n+1)
    print("nth fibbonacci =", fib(n, memoization))
    print(memoization)

if __name__ == "__main__":
    main()
