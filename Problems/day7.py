'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def num_encoding_brute(a, new_items):
	if len(a) == 0:
		if len(new_items) == 0:
			return []
		elif len(new_items) == 1:
			return [new_items[0]]
		else:
			return num_encoding_brute([new_items[0]], new_items[1:])
	elif a[0] == 0:
		return None
	elif len(new_items) == 0:
		return [a]

	res = []

	a1 = a.copy()
	a1.append(new_items[0])
	res += (num_encoding_brute(a1, new_items[1:]))

	a2 = a.copy()
	a2[-1] = int(str(a2[-1]) + str(new_items[0]))
	if 1 <= a2[-1] <= 26:
		res += (num_encoding_brute(a2, new_items[1:]))

	return res

''' 
Better is to calculate only the num of occurance.
'''
def num_encodings_better(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:				# if we take the first 2 digits, then we need to compute num_coding for the rest.
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])		# if we take the first 1 digit, then we need to compute num_coding for the rest.
    return total

from collections import defaultdict
def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
    	if s[i].startswith('0'):
    		cache[i] = 0
    	elif i == len(s) - 1:
    		cache[i] = 1
    	else:
    		if int(s[i:i+2]) <= 26:		# if current position's first 2 digits can be encoded, then we will do that and sum up with the count after the 2 digits.
    			cache[i] += cache[i+2]
    		cache[i] += cache[i+1]		# if we take current position's digit, then need to sum with the next digit's count.

    return cache[0]

def main():
	print(num_encoding_brute([], [1,1,1]))
	print(num_encoding_brute([], [0,2,3]))
	print(num_encoding_brute([], [1,2,3,4]))
	print(num_encoding_brute([], [1,2,3,4,5]))

	print(num_encodings_better('123'))
	print(num_encodings_better('023'))
	print(num_encodings_better('1234'))
	print(num_encodings_better('12345'))
	print(num_encodings_better('012'))

	print(num_encodings('123'))
	print(num_encodings('023'))
	print(num_encodings('1234'))
	print(num_encodings('12345'))
	print(num_encodings('012'))

if __name__ == '__main__':
	main()