'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
	def __init__(self, val=None):
		self.val = val
		self.L = None
		self.R = None
	
class Tree:
	def __init__(self, head=None):
		self.head = head

def get_universal_tree_count(p):
	if p is None:
		return 0,0
	elif p.L is None and p.R is None:
		return 1, 1	# uni_depth, total
	
	uni_depth = 0
	left_uni_depth, left_total = get_universal_tree_count(p.L)
	right_uni_depth, right_total = get_universal_tree_count(p.R)
	total = left_total + right_total

	if p.L is not None and p.R is not None and (p.val == p.L.val and p.val == p.R.val):
		uni_depth = min(left_uni_depth, right_uni_depth) + 1
		total += (1 + min(left_uni_depth, right_uni_depth) - 1)

	return uni_depth, total

def main():
	# head = Node(0)
	# L = Node(1)
	# R = Node(0)
	# RL = Node(1)
	# RR = Node(0)
	# RLL = Node(1)
	# RLR = Node(1)
	# head.L = L
	# head.R = R
	# R.L = RL
	# R.R = RR
	# RL.L = RLL
	# RL.R = RLR
	# _, count = get_universal_tree_count(head)
	# print(count)

	# head = Node(0)
	# L = Node(1)
	# R = Node(1)
	# RL = Node(1)
	# RR = Node(1)
	# RRL = Node(1)
	# RRR = Node(1)
	# RLL = Node(1)
	# RLR = Node(1)
	# head.L = L
	# head.R = R
	# R.L = RL
	# R.R = RR
	# RL.L = RLL
	# RL.R = RLR
	# RR.L = RRL
	# RR.R = RRR
	# _, count = get_universal_tree_count(head)
	# print(count)

	head = Node(1)
	L = Node(1)
	LL = Node(1)
	LLL = Node(1)
	LLR = Node(1)
	LR = Node(1)
	LRL = Node(1)
	LRR = Node(1)

	R = Node(1)
	RL = Node(1)
	RLL = Node(1)
	RLR = Node(1)
	RR = Node(1)
	RRL = Node(1)
	RRR = Node(1)

	head.L = L
	head.R = R

	L.L = LL
	LL.L = LLL
	LL.R = LLR
	L.R = LR
	LR.L = LRL
	LR.R = LRR

	R.L = RL
	RL.L = RLL
	RL.R = RLR
	R.R = RR
	RR.L = RRL
	RR.R = RRR

	_, count = get_universal_tree_count(head)
	print(count)


if __name__ == '__main__':
	main()

