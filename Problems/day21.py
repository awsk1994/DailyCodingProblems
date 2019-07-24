'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def bf(times):
	max_overlap = 0
	for i in range(len(times)):
		overlap = 0
		for j in range(len(times)):
			a_start, a_end = times[i]
			b_start, b_end = times[j]
			if i != j and not(a_end < b_start or b_end < a_start):
				overlap += 1
		max_overlap = max(max_overlap, overlap)
	return max_overlap

def opt(times):
	start = sorted([t[0] for t in times])
	end = sorted([t[1] for t in times])

	max_overlap, overlap = 0, 0
	i, j = 0, 0
	while i < len(start) and j < len(end):
		if start[i] < end[j]:
			overlap += 1
			max_overlap = max(max_overlap, overlap)
			i += 1
		else:
			overlap -= 1
			j += 1
	return max_overlap

def main():
	times = [(30, 75), (0, 50), (60, 150), (40, 65)]
	print("Input = {}".format(times))
	print("Brute force | max_overlap = {}".format(bf(times)))
	print("Optimized | max_overlap = {}".format(opt(times)))

if __name__ == "__main__":
	main()

