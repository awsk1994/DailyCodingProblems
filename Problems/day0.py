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

# My Initial Answer (recursion)
def climbStairs(n):
	return climbStairsRec(n, [], [])

def climbStairsRec(n, curr_combo, combos):
	if n == 0:
		combos.append(curr_combo)
	else:
		if n >= 1:
			climbStairsRec(n-1, curr_combo + [1], combos)
		if n >= 2:
			climbStairsRec(n-2, curr_combo + [2], combos)
	return combos

def main():
	n = 4
	print(climbStairs(n))

if __name__ == '__main__':
	main()
