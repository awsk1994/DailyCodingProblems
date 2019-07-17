'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

from collections import deque

def brute_max_sub_arr(lst, k):
	for i in range((k-1), len(lst)):
		print("\t" + str(max(lst[i-k+1:i+1])))

def opt_max_sub_arr(lst, k):
	q = deque()

	for i in range(k):
		while q and lst[i] > lst[q[-1]]:
			q.pop()
		q.append(i)
	
	print("\t" + str(lst[q[0]]))

	for i in range(k, len(lst)):
		if q[0] <= (i - k):
			q.popleft()
		while q and lst[i] > lst[q[-1]]:
			q.pop()
		q.append(i)
		print("\t" + str(lst[q[0]]))

def main():
	print("brute_max_sub_arr")
	brute_max_sub_arr([10,5,2,7,8,7], 3)

	print("optimized_solution")
	opt_max_sub_arr([10,5,2,7,8,7], 3)

if __name__ == "__main__":
	main()
