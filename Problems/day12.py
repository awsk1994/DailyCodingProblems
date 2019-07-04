'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

# O(2^n)
def brute_uniq_steps(n):
	if n <= 1:
		return 1
	return brute_uniq_steps(n-1) + brute_uniq_steps(n-2)

# Run: O(n), Space: O(n)
def dyn_uniq_steps(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	arr = [None] * (n + 1)
	arr[n] = 1	# N = 0
	arr[n-1] = 1 # N = 1
	for i in reversed(range(0,n-1)):
		arr[i] = arr[i+1] + arr[i+2]
	return arr[0]

# Run: O(n), Space: O(2)
def dyn_uniq_steps_2(n):
	if n == 1:
		return 1
	a, b = 1, 2	# N = 1 and N = 2
	for _ in range(0, n - 2):
		a, b = b, a + b
	return b

# Run: O(n), Space: O(n)
def dyn_uniq_steps_multi_step(X, n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	cache = [0] * (n + 1)
	cache[n] = 1
	for i in reversed(range(0, n)):
		cache[i] = sum(cache[i+x] for x in X if i+x <= n)
	return cache[0]

def main():
	print("brute | n = {}, output: {}".format(5, brute_uniq_steps(5)))
	print("brute | n = {}, output: {}".format(4, brute_uniq_steps(4)))
	print("brute | n = {}, output: {}".format(3, brute_uniq_steps(3)))
	print("brute | n = {}, output: {}".format(2, brute_uniq_steps(2)))
	print("brute | n = {}, output: {}".format(1, brute_uniq_steps(1)))

	print("dyn | n = {}, output: {}".format(5, dyn_uniq_steps(5)))
	print("dyn | n = {}, output: {}".format(4, dyn_uniq_steps(4)))
	print("dyn | n = {}, output: {}".format(3, dyn_uniq_steps(3)))
	print("dyn | n = {}, output: {}".format(2, dyn_uniq_steps(2)))
	print("dyn | n = {}, output: {}".format(1, dyn_uniq_steps(1)))

	print("dyn 2 | n = {}, output: {}".format(5, dyn_uniq_steps_2(5)))
	print("dyn 2 | n = {}, output: {}".format(4, dyn_uniq_steps_2(4)))
	print("dyn 2 | n = {}, output: {}".format(3, dyn_uniq_steps_2(3)))
	print("dyn 2 | n = {}, output: {}".format(2, dyn_uniq_steps_2(2)))
	print("dyn 2 | n = {}, output: {}".format(1, dyn_uniq_steps_2(1)))

	print("dyn multi | n = {}, output: {}".format(5, dyn_uniq_steps_multi_step([1,2], 5)))
	print("dyn multi | n = {}, output: {}".format(4, dyn_uniq_steps_multi_step([1,2], 4)))
	print("dyn multi | n = {}, output: {}".format(3, dyn_uniq_steps_multi_step([1,2], 3)))
	print("dyn multi | n = {}, output: {}".format(2, dyn_uniq_steps_multi_step([1,2], 2)))
	print("dyn multi | n = {}, output: {}".format(1, dyn_uniq_steps_multi_step([1,2], 1)))

if __name__ == "__main__":
	main()

