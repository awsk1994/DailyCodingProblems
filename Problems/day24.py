'''
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''

class Node:
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.locked = False
		self.locked_descendents = 0
		self.left = None
		self.right = None

	def is_locked(self):
		return self.locked

	def can_lock_or_unlock(self):
		if self.locked_descendents > 0:
			return False

		c = self.parent
		while c is not None:
			if c.is_locked():
				return False
			c = c.parent
		return True

	def lock(self):
		if self.can_lock_or_unlock():
			self.locked = True
			c = self.parent
			while c is not None:
				c.locked_descendents += 1
				c = c.parent
			return True
		return False

	def unlock(self):
		if self.can_lock_or_unlock():
			self.locked = False
			c = self.parent
			while c is not None:
				c.locked_descendents -= 1
				c = c.parent
			return True
		return False

	def print(self):
		print("val={}, locked={}, locked_descendents={}".format(self.val, self.locked, self.locked_descendents))
		if self.left is not None:
			self.left.print()
		if self.right is not None:
			self.right.print()

def main():
	one = Node(1)
	two = Node(2)
	three = Node(3)
	four = Node(4)
	five = Node(5)
	six = Node(6)
	seven = Node(7)
	one.left = two
	two.parent = one
	two.left = three
	three.parent = two
	two.right = four
	four.parent = two
	one.right = five
	five.parent = one
	five.left = six
	six.parent = five
	five.right = seven
	seven.parent = five
	
	one.print()
	print("\nlock five | res={}".format(five.lock()))
	one.print()
	four.print()
	print("\nlock four | res={}".format(four.lock()))
	one.print()
	print("\nlock two | res={}".format(two.lock()))
	print("\nlock four | res={}".format(four.unlock()))
	one.print()

if __name__ == "__main__":
	main()

