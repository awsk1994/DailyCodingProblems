'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def prod_lst(lst, reverse = False):
	r = range(len(lst))
	if reverse:
		r = reversed(r)	# or r = range(len(lst)-1, -1, -1)

	product = 1
	products = [0] * len(lst)

	for i in r:
		product *= lst[i]
		products[i] = product

	return products

# O(n)
def opt_sol(lst):
	LR = prod_lst(lst)
	RL = prod_lst(lst, True)

	ans = [None] * len(lst)
	for i in range(len(lst)):
		l, r = 1, 1
		if i - 1 >= 0:
			l = LR[i-1]
		if i + 1 < len(lst):
			r = RL[i+1]
		ans[i] = l * r
	return ans

def main():
	lst = [1,2,3,4,5]
	ans = [120, 60, 40, 30, 24]

	my_ans = opt_sol(lst)
	print("my_ans: {}\t| Same as ans? {}".format(my_ans, my_ans == ans))

if __name__ == '__main__':
	main()
	