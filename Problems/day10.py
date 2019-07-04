'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

''' Easy Example '''
import sched, time

def f():
	print("{} | This is function f.".format(time.time()))

def delay_call_func(fnc, delay):
	s = sched.scheduler(time.time, time.sleep)
	print("{}".format(time.time()))
	s.enter(delay, 1, fnc)
	s.run()

''' More complicated custom scheduler '''
import threading

class Scheduler:
	def __init__(self):
		self.schedules = []
		t = threading.Thread(target=self.poll)
		t.start()

	def poll(self):
		while True:
			now = time.time() * 1000
			for fn, due in self.schedules:
				if now >= due:
					fn()
			self.schedules = [(fn, due) for (fn, due) in self.schedules if due > now]
			time.sleep(0.01)

	def delay(self, fnc, n):
		self.schedules.append((fnc, time.time() * 1000 + n))

def start_custom_scheduler(fnc, n):
	print("{}".format(time.time()* 1000))
	s = Scheduler()
	s.delay(fnc, n)

''''''

def main():
	delay_call_func(f, 2)
	start_custom_scheduler(f, 2)

if __name__ == "__main__":
	main()
