'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

class Node:
	def __init__(self, val):
		self.next_char = {}
		self.val = val

	def add_next_node(self, n):
		if not self.has_val(n.val):
			self.next_char[n.val] = n

	def has_val(self, n_val):
		return n_val in self.next_char

	def print(self):
		print("Node | val = {}".format(self.val))

class Tree:
	def __init__(self):
		self.head = None

	def add(self, word):
		if self.head is None:
			self.head = Node("")
		curr = self.head
		for c in word:
			if curr.has_val(c):
				curr = curr.next_char[c]
			else:
				curr.add_next_node(Node(c))
				curr = curr.next_char[c]
			curr.print()

	def prefix_get(self, prefix):
		curr = self.head
		for c in prefix:
			if c in curr.next_char:
				curr = curr.next_char[c]
			else:
				return None

		self.print_rest_of_tree(curr)

	def print_rest_of_tree(self, node):
		for [n_char, n_node] in node.next_char.items():
			print(n_char)
			self.print_rest_of_tree(n_node)

		None # TODO

	def print_tree(self):
		self.print(self.head)

	def print(self, node):
		if node is None:
			self.print(self.head)
		else:
			for [n_char, n_node] in node.next_char.items():
				print(n_char)
				self.print(n_node)

def main():
	tree = Tree()
	tree.add("dog")
	tree.add("deer")
	tree.add("dear")
	tree.print_tree()
	print("PREFIX_GET:")
	tree.prefix_get("de")

if __name__ == "__main__":
	main()
