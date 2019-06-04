'''
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
'''

# Naive Solution (recursion - O(2^n))
def solNaive(n, steps):
	return len(solNaiveChild(n, steps, [], []))

def solNaiveChild(n, steps, curr_combo, combos):
	if n < 0:
		none
	elif n == 0:
		combos.append(curr_combo)
	else:
		for step in range(1, steps + 1):
			added_combo = curr_combo + [step]
			combos = solNaiveChild(n - step, steps, added_combo, combos)

	return combos
'''
If you look at the solution, you will realize that it's basically fibonacci sequence:
N = 1 => [1]						=> 1
N = 2 => [1,2]						=> 2
N = 3 => [111, 12, 21]				=> 3
N = 4 => [1111, 112, 121, 211, 22] 	=> 5
N = 5 => [...] 						=> 8

Algorithm: f(n) = f(n-1) + f(n-2).
'''

# Recursion Solution (rescursion - O(2^n))
def solRecur(n, steps):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return sum([solRecur(n-step, steps) for step in range(1,steps + 1)])

# Optimal Answer (Iteration - O(n))
def solIter(n, steps):
	cache = [0 for _ in range(n + 1)]
	cache[0] = 1
	for i in range(1, n+1):
		if i == 1:
			cache[i] = cache[i-1]
		if i > 1:
			cache[i] = sum([cache[i-step] for step in range(1, steps + 1)])
	return cache[n]

def main():
	n = 5
	steps = 2
	print("Naive:\t\t{}\tO(2^n)".format(solNaive(n, steps)))
	print("Recursive:\t{}\tO(2^n)".format(solRecur(n, steps)))
	print("Iteration:\t{}\tO(n)".format(solIter(n, steps)))

if __name__ == '__main__':
	main()
