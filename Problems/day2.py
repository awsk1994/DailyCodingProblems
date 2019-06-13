'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def get_prefix_prod(lst):
	products = [0] * len(lst)
	for i in range(len(lst)):
		if i == 0:
			products[i] = lst[i]
		else:
			products[i] = products[i-1] * lst[i]
	return products

def get_suffix_prod(lst):
	products = [0] * len(lst)
	for i in reversed(range(len(lst))):
		if i == len(lst)-1:
			products[i] = lst[i]
		else:
			products[i] = products[i+1] * lst[i]
	return products

# O(n)
def products(lst):
	LR = get_prefix_prod(lst)
	RL = get_suffix_prod(lst)

	ans = []
	for i in range(len(lst)):
		if i == 0:				# head
			ans.append(RL[i+1])
		elif i == len(lst) - 1:	# tail
			ans.append(LR[i-1])
		else:					# middle elems
			ans.append(LR[i-1] * RL[i+1])
	return ans

def main():
	lst = [1,2,3,4,5]
	ans = [120, 60, 40, 30, 24]

	my_ans = products(lst)
	print("my_ans: {}\t| Same as ans? {}".format(my_ans, my_ans == ans))

if __name__ == '__main__':
	main()
