#!/usr/bin/env python3

#---My own implementation of linkedList in Python---#

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
        self.length += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("The list is empty!")
        else:
            temp = self.head
            while temp.next.next: # Get to the second last node
                temp = temp.next
            temp.next = None
            self.length -= 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

def main():
    myList = LinkedList()
    myList.insert(3)
    myList.insert(4)
    myList.insert("hello")
    myList.pop()
    myList.insert([123,2])
    myList.print_list()
    print("List size =", myList.length)

if __name__ == "__main__":
    main()