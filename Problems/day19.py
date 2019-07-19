'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.
'''
from math import inf
import sys

# O(k^n)
class Brute:
	def __init__(self, N, K, cost):
		self.N = N
		self.K = K
		self.cost = cost

	def min_cost(self, n_left, pk):
		if n_left == None:
			n_left = self.N

		if n_left == 0:
			return 0

		lowest_cost = sys.maxsize
		n = self.N - n_left

		for k in range(self.K):
			if k == pk:
				continue
			cost = self.cost[n][k] + self.min_cost(n_left - 1, k)
			lowest_cost = min(lowest_cost, cost)
		return lowest_cost

# O (nxk)
def lowest_cost(cost):
	lowest_cost, lowest_cost_index, second_lowest_cost = 0, -1, 0
	for r, row in enumerate(cost):
		new_lowest_cost, new_lowest_cost_index, new_second_lowest_cost = inf, -1, inf

		for c, val in enumerate(row):
			# We already selected color c. Thus, the previous lowest cost is second_lost_cost if c is same as previous lowest cost. 
			previous_lowest_cost = second_lowest_cost if c == lowest_cost_index else lowest_cost
			cost = previous_lowest_cost + val

			# Update new_lowest_cost, new_second_lowest_cost and new_lowest_cost_index
			if cost < new_lowest_cost:
				new_second_lowest_cost = new_lowest_cost
				new_lowest_cost = cost
				new_lowest_cost_index = c
			elif cost < new_second_lowest_cost:
				new_second_lowest_cost = cost

		# Update lowest_cost, lowest_cost_index and second_lowest_cost.
		lowest_cost = new_lowest_cost
		lowest_cost_index = new_lowest_cost_index
		second_lowest_cost = new_second_lowest_cost

	return lowest_cost

def main():
	N = 5
	K = 3
	cost = [[10, 5, 1], [10, 5, 1], [10, 5, 1], [10, 5, 1], [10, 5, 1]]	# cost[y][x], cost[N][K]
	print("Brute sol={}".format(Brute(N, K, cost).min_cost(None, None)))
	print("Optimized sol={}".format(lowest_cost(cost)))

if __name__ == "__main__":
	main()
