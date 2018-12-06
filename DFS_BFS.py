#!/usr/bin/env python3

import random
import argparse as ap
import os
import re
import math
import sys

class Queue:
    def __init__(self, list = []):
        self.list = list[:]

    def enqueue(self, el):
        self.list.append(el)

    def dequeue(self):
        if not self.is_empty():
            return self.list.pop(0)
        else:
            print("The queue is empty")

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False


def print_matrix(G):
    for row in G:
        for col in row:
            print(col, end=" ")
        print()


def DFS(G, marked, edgeTo, postOrder, i):
    marked[i] = True
    for j in range(len(G[i])):
        if not marked[j] and G[i][j] != 0:
            edgeTo[j] = i
            DFS(G, marked, edgeTo, postOrder, j)
    postOrder.append(i)


def BFS(G, marked, edgeTo, queue):
    i = queue.dequeue()
    for j in range(len(G[i])):
        if not marked[j] and G[i][j] != 0:
            edgeTo[j] = i
            marked[j] = True
            queue.enqueue(j)
    if not queue.is_empty():
        BFS(G, marked, edgeTo, queue)


def main():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as file:
                data = file.read().split("\n") # Turns source into list of rows
                n = int(data[0]) # Takes number of vertices
                G = [[] for row in range(n)] # Initialize a list of n empty lists
                [G[x-1].extend(map(int, data[x].split())) for x in range(1, n+1)]
        else:
            print(sys.argv[1], 'does not exist')
            exit(1)

    else:
        n = int(input("Enter the size of the graph: "))
        G = [None for row in range(n)]
        count = 0
        while count < n:
            matrix = input().strip()
            G[count] = list(map(int, matrix.split()))
            if len(G[count]) != n:
                print("There must be {} elements in each row".format(n))
                exit(1)
            count += 1

    print_matrix(G)
    postOrder = []
    marked = [False for x in range(n)]
    edgeTo = [-1 for x in range(n)]
    queue = Queue()
    queue.enqueue(0)
    marked[0] = True
    # DFS(G, marked, edgeTo, postOrder, 0)
    BFS(G, marked, edgeTo, queue)
    # edgeTo = list(map(lambda x: x+1, edgeTo))
    print(edgeTo)


if __name__ == "__main__":
    main()
