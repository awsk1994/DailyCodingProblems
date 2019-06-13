'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

import ast

# Node class definition
class Node:
	def __init__(self, val, left=None, right=None):
	    self.val = val
	    self.left = left
	    self.right = right

# serialize: O(n)
def serialize(n):
	return str(serialize_r(n))

def serialize_r(n):
	if n is None:
		return None
	return str([serialize_r(n.left), n.val, serialize_r(n.right)])
	
# deserialize: O(n)
def deserialize(string):
	arr = ast.literal_eval(string) # O(n)
	return deserialize_r(arr)

def deserialize_r(arr):
	if arr == None:
		return None
	[l, s, r] = arr
	return Node(s, deserialize_r(arr[0]), deserialize_r(arr[2]))

def main():
	n = Node('root', Node('L', Node('L.L')), Node('R'))
	print(serialize(n))
	print(deserialize(serialize(n)).left.left.val == 'L.L')

if __name__ == '__main__':
	main()

