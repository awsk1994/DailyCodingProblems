'''
Good morning!

Here's a solution to yesterday's problem.

This is your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
'''

'''
Brute Force: Run: O(2^n)
'''
def brute(lst, sum=0):
	if len(lst) == 0:
		return sum
	elif len(lst) == 1:
		return sum + lst[0]

	sum_take_first, sum_take_second = 0,0
	if len(lst) >= 1:
		sum_take_first = brute(lst[2:], sum+lst[0])
	if len(lst) >=2:
		sum_take_second = brute(lst[3:], sum+lst[1])
	return max(sum_take_first, sum_take_second)

def brute_better(lst):
	if not lst:
		return 0

	# brute_better(lst[1:]) shifts to the next one. lst[0] + brute_better(lst[2:]) adds current and shifts 2.
	return max(brute_better(lst[1:]), lst[0] + brute_better(lst[2:]))	

''' 
Run: O(n), Space: O(0) [used original]
'''
def sum_2(lst):
	if len(lst) == 0:
		return 0
	elif len(lst) <= 2:
		return max(lst)
	elif len(lst) == 2:
		return max(lst[0], lst[1])
	'''
		Above can be replaced by:
		if len(lst) <= 2:
			return max(0, max(lst))
	'''

	for i in reversed(range(len(lst)-2)):
		if i == len(lst)-3:
			lst[i] += lst[i+2]
		else:
			lst[i] += max(lst[i+2], lst[i+3])
	return lst[0]

''' 
Run: O(n), Space: O(3)
'''
def sum_1(lst):
	if len(lst) <= 2:
		return max(0, max(lst))

	max_last = lst[len(lst)-1]
	max_second_last = lst[len(lst)-2]
	max_third_last = (lst[len(lst)-3] + lst[len(lst)-1])

	for i in reversed(range(len(lst)-3)):
		m = lst[i] + max(max_second_last, max_last)
		max_last = max_second_last
		max_second_last = max_third_last
		max_third_last = m
	return max_third_last

def sol(lst):
	print("lst={}".format(lst))
	print("\tbrute={}".format(brute(lst)))
	print("\tbrute_better={}".format(brute_better(lst)))
	print("\tsum_1={}".format(sum_1(lst)))
	print("\tsum_2={}\n".format(sum_2(lst)))

def main():
	sol([2,4,6,2,5])
	sol([5,1,1,5])

if __name__ == '__main__':
	main()
