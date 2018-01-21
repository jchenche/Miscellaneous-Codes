#!/usr/bin/env python3

#---My own implementation of linkedList in Python---#

class Node():
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList():
	def __init__(self, head):
		self.head = head
		self.length = 0

	def insert(self, val):
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
			while temp.next.next:
				temp = temp.next
			temp.next = None
			self.length -= 1

	def print_list(self):
		temp = self.head.next
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
	head = Node(-1)
	myList = LinkedList(head)
	myList.insert(3)
	myList.insert(4)
	myList.insert("hello")
	myList.pop()
	myList.insert([123,2])
	myList.print_list()
	print(myList.length)

if __name__ == "__main__":
	main()