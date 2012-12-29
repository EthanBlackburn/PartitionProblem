import random
import math

numbers = []
left = []
right = []
balance = 0 #negative value if left sum is higher, positive value if right sum is higher and 0 if sums are equal

def farthestVal(num):
	largest_delta = 0 
	large_key = 0
	for key in numbers:
		if(math.fabs(num-key) > largest_delta):
			largest_delta = math.fabs(num-key)
			large_key = key
			
	return large_key


for i in range(1000): #generates 1000 numbers to partition
	numbers.append(random.randrange(1,1000,1))

for j in range(1000):
	if(balance != 0):
		if(balance < 0):
			far_val = farthestVal(balance)
			right.append(far_val)
			numbers.remove(far_val)
			balance += far_val
		else:
			far_val = farthestVal(balance)
			left.append(far_val)
			numbers.remove(far_val)
			balance -= far_val
	else:
		far_val = farthestVal(balance)
		left.append(far_val)
		numbers.remove(far_val)
		balance -= far_val
			
print 'left: '	
print left
print 'right: '
print right

print 'balance: '
print balance
		


	
