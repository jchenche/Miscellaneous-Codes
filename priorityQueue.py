#!/usr/bin/env python3

class MinPriorityQueue:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        assert(type(value) == int)
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size)

    def insert_all(self, array):
        assert(type(array) == list)
        for value in array:
            self.insert(value)

    def peek(self):
        return self.heap[1]

    def pop(self):
        self.swap(1, self.size)
        popped = self.heap.pop()
        self.size -= 1
        self.bubble_down(1)
        return popped

    def heapsort(self):
        sorted_array = []
        while self.size > 0:
            sorted_array.append(self.pop())
        return sorted_array

    def print(self):
        print(self.heap)

    def bubble_down(self, propagating_index):
        last = self.size
        left = propagating_index * 2
        right = propagating_index * 2 + 1
        if left > last: # No children, it's a leaf
            return

        min_child = left
        if right <= last: # Make sure there's a right child
            if self.heap[left] > self.heap[right]:
                min_child = right

        if self.heap[propagating_index] > self.heap[min_child]:
            self.swap(propagating_index, min_child)
            self.bubble_down(min_child)

    def bubble_up(self, propagating_index):
        parent = int(propagating_index / 2)
        if self.heap[propagating_index] >= self.heap[parent]:
            return
        self.swap(propagating_index, parent)
        self.bubble_up(parent)

    def swap(self, index_a, index_b):
        temp = self.heap[index_a]
        self.heap[index_a] = self.heap[index_b]
        self.heap[index_b] = temp

def main():
    pq = MinPriorityQueue()
    pq.insert_all([1,2,5,3,7,6,6,2,5,9,12,3])
    pq.print()
    print(pq.heapsort())

if __name__ == '__main__':
    main()