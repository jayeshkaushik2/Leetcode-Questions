class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printLinkedList(self):
		'''
		This function will print all the node's value
		'''
		curNode = self.head
		
		while curNode:
			print(curNode.val, end=" ")
			curNode = curNode.next

	def appendNodeAtEnd(self, value):
		'''
		This function will append the Node to the end of the Linked List
		'''
		tail = self.head

		while tail:
			if tail.next == None:
				tail.next = Node(value)
				tail = tail.next
				break
			tail = tail.next

	def appendNodeAtStart(self, value):
		'''
		This function will append the Node at the start of the Linked List
		'''
		temp = self.head
		self.head = Node(value)
		self.head.next = temp

	def insertNode(self, k, value):
		'''
		This function will insert elements at a position
		'''
		cnt = 1
		curNode = self.head

		while curNode:
			if cnt == k-1:
				temp = curNode.next
				curNode.next = Node(value)
				curNode = curNode.next

				curNode.next = temp
				curNode = curNode.next
				break
			cnt += 1
			curNode = curNode.next


if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,9,10,11,12]
	
	# intializing the linked list
	# dummy = LinkedList()
	# tail  = dummy

	# for i in range(len(arr)):
	# 	tail.next = Node(arr[i])
	# 	tail = tail.next

	# head = dummy.next
	# while head:
	# 	print(head.val)
	# 	head = head.next


	listIs = LinkedList()
	listIs.head = Node(arr[0])

	first  = Node(arr[1])
	second = Node(arr[2])
	third  = Node(arr[3])

	listIs.head.next = first
	first.next = second
	second.next = third

	# printing the Linked List
	listIs.printLinkedList()

	# appending the elements at the end of the linked list
	listIs.appendNodeAtEnd(arr[4])
	listIs.appendNodeAtEnd(arr[5])
	print()
	listIs.printLinkedList()

	# appending the elements at the start of the linked list
	listIs.appendNodeAtStart(arr[4])
	print()
	listIs.printLinkedList()

	# inserting the elements at the kth position of the linked list
	listIs.insertNode(7, 4343)
	listIs.insertNode(3, 8585858)
	print()
	listIs.printLinkedList()