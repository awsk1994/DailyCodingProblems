'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
'''

class Brute:
	def __init__(self, n):
		self._log = []
		self.n = n

	def record(self, order_id):
		if len(self._log) == self.n:
			self._log.pop(0)
		self._log.append(order_id)

	def get_last(self, i):
		return self._log[-1 * i]

class CircularBuffer:
	def __init__(self, n):
		self._log = []
		self.n = n
		self.curr = 0

	def record(self, order_id):
		if len(self._log) == self.n:
			self._log[self.curr] = order_id
		else: 
			self._log.append(order_id)
		
		if self.curr == (self.n-1):
			self.curr = 0
		else:
			self.curr += 1

	def get_last(self, i):
		return self._log[self.curr - i]

def main():
	brute = Brute(3)
	circularBuffer = CircularBuffer(3)

	for i in range(5):
		brute.record(i)
		print("brute | _log={}, last_1={}".format(brute._log, brute.get_last(1)))

	for i in range(5):
		circularBuffer.record(i)
		print("circularBuffer | _log={}, last_1={}".format(circularBuffer._log, circularBuffer.get_last(1)))

if __name__ == "__main__":
	main()
