'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

import ctypes

class XORNode:
	def __init__(self, val = None):
		self.val = val
		self.both = None

class XORDoubleLinkedList:
	def __init__(self, head = None):
		self.head = head

	def add(self, n):
		if self.head is None:
			self.head = n
		else:
			c, p = self.head, None
			while self.nextNode(c, p) is not None:
				nxt = self.nextNode(c, p)
				p = c
				c = nxt
			
			if p is None:		# if head is adding a node.
				c.both = id(n)
			else:
				c.both = id(p) ^ id(n)

			n.both = id(c)		# new node's both is current node id.

	def print(self):
		c,p = self.head, None
		print(c.val)
		while self.nextNode(c,p) is not None:
			n = self.nextNode(c,p)
			print(n.val)
			p = c
			c = n

	def nextNode(self, c,p):
		onlyHeadNode = c.both is None
		lastNode = ((id(p) == c.both) and p is not None)
		if onlyHeadNode or lastNode:
			return None
		else:
			if p is None:	# head (if head.next not None)
				return _get_obj(c.both)
			else:
				next_id = id(p) ^ c.both
				return _get_obj(next_id)

def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value

def main():
	ll = XORDoubleLinkedList()

	one = XORNode(1)
	ll.add(one)

	two = XORNode(2)
	ll.add(two)

	three = XORNode(3)
	ll.add(three)
	
	ll.print()

if __name__ == '__main__':
	main()

