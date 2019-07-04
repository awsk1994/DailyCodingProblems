'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

# Run: O(n^2), Space: O(k)
def brute_longest_substring(k, s):
	longest = 0
	for i in range(0, len(s)):
		count, store = 0, set()
		for j in range(i, len(s)):
			store.add(s[j])
			if len(store) > k:
				break
			count += 1
		longest = max(longest, count)
	return longest

# Run: O(n), Space: O(k + 2)
def moving_longest_substring(k, s):
	h, bound, longest = {}, [0,0], 0
	for i, c in enumerate(s):
		h[c] = i
		bound[1] = i 	# Shift highest bound 1 to the right.
		if len(h.keys()) > k:
			key_to_pop = min(h, key=h.get)		# Find smallest i-th position, but return the key of it.
			bound[0] = h.pop(key_to_pop) + 1	# Lowest bound = key_to_pop's next element.
		longest = max(longest, (bound[1] - bound[0] + 1))
	return longest

def main():
	print("Brute | {}".format(brute_longest_substring(2, "abcba")))
	print("Brute | {}".format(brute_longest_substring(2, "aabbccbbaa")))
	print("Brute | {}".format(brute_longest_substring(3, "abcdcba")))

	print("Moving Window | {}".format(moving_longest_substring(2, "abcba")))
	print("Moving Window | {}".format(moving_longest_substring(2, "aabbccbbaa")))
	print("Moving Window | {}".format(moving_longest_substring(3, "abcdcba")))

if __name__ == "__main__":
	main()
