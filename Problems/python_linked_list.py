class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def print(self):
		n = self.head
		while n is not None:
			print(n.val)
			n = n.next

	def insert_at_head(self, val):
		n = Node(val)
		n.next = self.head
		self.head = n

	def insert_at_tail(self, val):
		if self.head is None:
			self.head = Node(val)
		else:
			n = self.head
			while n.next:
				n = n.next

			n.next = Node(val)

	def delete(self, target):
		if self.head is not None:
			if self.head.val == target:
				self.head = self.head.next
			else:
				n = self.head
				while n.next:
					if n.next.val == target:
						n.next = n.next.next
						break
					n = n.next

	def delete2(self, target):
		if self.head is not None:
			if self.head.val == target:
				self.head = self.head.next
			else:
				p = self.head
				n = self.head.next
				while n is not None:
					if n.val == target:
						p.next = n.next
						break
					p = n
					n = n.next

def main():
	list1 = LinkedList()
	list1.insert_at_head(1)
	list1.insert_at_tail(2)
	list1.insert_at_tail(3)
	print("PRINT:")
	list1.print()

	list1.insert_at_head(0)
	print("INSERT 3 AT HEAD")
	list1.print()

	list1.insert_at_tail(4)
	print("INSERT 4 AT TAIL")
	list1.print()

	list1.delete2(4)
	print("DELETE 4 AT TAIL")
	list1.print()

	list1.delete2(2)
	print("DELETE 2 AT MID")
	list1.print()

	list1.delete2(0)
	print("DELETE 0 AT HEAD")
	list1.print()

if __name__ == "__main__":
	main()