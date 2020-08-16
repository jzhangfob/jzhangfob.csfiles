

def convert_fib_base(num):
		
	fib_sequence = []
	fib_sequence.append(0)
	fib_sequence.append(1)
	
	#Create the fibonacci sequence as long as needed 
	while num >= fib_sequence[-1] + fib_sequence[-2]:
		fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
	
	#Reverse the fib sequence list and remove the last two items 
	fib_sequence.reverse()
	del fib_sequence[-1]
	del fib_sequence[-2]
	
	#Intialize fibonacci base 
	fib_base = []
	sum = 0
	
	#First, create list of 0's as long as the fibonacci sequence
	for i in range(len(fib_sequence)):
		fib_base.append(0)
	
	i = 0		
	#Iterate through the length of the fibonacci sequence list 
	while i < len(fib_sequence):
		sum += fib_sequence[i] 
		
		#If the first term in the fib sequence is num, break out of the loop 
		if fib_sequence[0] == num:
			fib_base[0] = 1
			break
		
		#If sum is less than num, skip the next index and adjust fibonacci base 
		elif sum < num: 
			fib_base[i] = 1
			fib_base[i+1] = 0 
			i += 2 
		
		#If sum is greater than num, bring sum back down to what it was originally, go to next index, adjust fib base 
		elif sum > num:
			sum -= fib_sequence[i] 
			fib_base[i] = 0 
			i += 1 
		
		#If sum equals num, adjust fib base, break out of loop 
		elif sum == num:
			fib_base[i] = 1 
			break 
	
	#Print output 
	print (num, '= ', end = '')
	for ch in fib_base:
		print (ch, end = '')
	print (' (fib)')
		
		
def main():
	
	#Get user input 
	num = eval(input("Enter a number: "))
	convert_fib_base(num)
	
main()
