'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

import copy

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def add(self, val):
		if self.head is None:
			self.head = Node(val)
		else:
			p = self.head
			while p.next is not None:
				p = p.next
			p.next = Node(val)

	def length(self):
		counter = 0
		c = self.head
		while c is not None:
			c = c.next
			counter += 1
		return counter

	def print(self):
		arr = []
		p = self.head
		while p is not None:
			arr.append(str(p.val))
			p = p.next
		print("->".join(arr))

def bf(lla, llb):
	a_nodes = []
	a = lla.head
	while a is not None:
		a_nodes.append(a)
		a = a.next

	b = llb.head
	while b is not None:
		for a_node in a_nodes:
			if a_node == b:
				return a_node
		b = b.next
	return None

def reverse_ll(ll):
	c = ll.head
	p = None

	while c is not None:
		n = c.next
		c.next = p
		p = c
		c = n

	return p

def fail_opt(lla, llb):
	bc = copy.deepcopy(llb)
	reverse_ll(lla)		# TODO: This becomes a permanent change!!

	cb = llb.head
	cbc = bc.head
	pcb = None
	pcbc = None
	while cb.val == cbc.val:
		pcb = cb
		pcbc = cbc
		cb = cb.next
		cbc = cbc.next
	return pcb

def opt2(lla, llb):
	len_a = lla.length()
	len_b = llb.length()

	a_offset = len_a - len_b
	ac = lla.head
	bc = llb.head

	if a_offset >= 0:
		while a_offset != 0:
			ac = ac.next
			a_offset -= 1
	else:
		b_offset = a_offset * -1
		while b_offset != 0:
			bc = bc.next
			b_offset += 1

	while ac != bc:
		ac = ac.next
		bc = bc.next

	return ac

def main():
	a1 = Node('a1')
	a2 = Node('a2')
	b1 = Node('b1')
	b2 = Node('b2')
	c1 = Node('c1')
	c2 = Node('c2')
	a1.next = a2
	a2.next = c1
	b1.next = b2
	b2.next = c1
	c1.next = c2
	lla = LinkedList(a1)
	llb = LinkedList(b1)

	print("Brute Force: common node ={}".format(bf(lla, llb).val))
	print("Optimized: common_node={}".format(opt2(lla, llb).val))
	print("Failed Opt Attempt: common_node={}".format(fail_opt(lla, llb).val))

if __name__ == "__main__":
	main()
