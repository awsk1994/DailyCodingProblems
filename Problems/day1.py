'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# O(n^2)
def brute_f_two_sum(l, target):
	for i in range(len(l)):
		for j in range(len(l)):
			if i != j and l[i] + l[j] == target:
				return True
	return False

# O(nlogn)
def two_pointer_two_sum(l, target):
	l.sort()
	lower = 0
	upper = len(l) - 1
	res = None

	while lower < upper:
		res = l[lower] + l[upper]
		if res > target:
			upper -= 1
		elif res < target:
			lower += 1
		else:
			return True
	return False

# O(n)
def seen_two_sum(lst, target):
	seen = set()
	for num in lst:
		if (target - num) in seen:	# set look up is O(1)
			return True
		seen.add(num)
	return False

# O(nlogn)
def bin_search_two_sum(lst, target):
	for i in range(len(lst)):
		idx = binary_search(lst, target - lst[i]) # O(log n)
		
		if idx == -1:
			continue
		elif idx != i:
			return True
		# if idx is same as i, then check if there is the same number before or after idx.
		elif (idx + 1 < len(lst) and lst[idx] == target) or (idx - 1 >= 0 and lst[idx-1] == target):
			return True
	return False

from bisect import bisect_left
def binary_search(lst, target):
	lo = 0
	hi = len(lst)
	ind = bisect_left(lst, target, lo, hi)

	if 0 <= ind < hi and lst[ind] == target:
		return ind
	else:
		return -1

def main():
	l = [10, 15, 3, 7]
	target = 17
	print(brute_f_two_sum(l, target))
	print(two_pointer_two_sum(l, target))
	print(seen_two_sum(l, target))
	print(bin_search_two_sum(l, target))

if __name__ == '__main__':
	main()
