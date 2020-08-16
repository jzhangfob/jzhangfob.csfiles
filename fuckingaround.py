#Fib base program 

#[1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
def convert_fib_base(num):
	fib_sequence = [0, 1]

	sum = fib_sequence[-1] + fib_sequence[-2]
	
	while num >= sum:
		fib_sequence.append(sum) 
		sum = fib_sequence[-1] + fib_sequence[-2]
	
	fib_sequence.remove(fib_sequence[0])
	fib_sequence.remove(fib_sequence[0])
	
	fib_sequence.reverse()
	
	fib = []
	
	for i in range(len(fib_sequence)):
		fib.append('0')
	fib[0] = '1'
	
	sum = fib_sequence[0]
	
	
	for i in range(2, len(fib_sequence)):
		if sum + fib_sequence[i] == num:
			fib[i] = '1'
			break
		elif sum + fib_sequence[i] < num:
			fib[i] = '1'
			sum = sum + fib_sequence[i]
	
	output = ''
	for i in range(len(fib)):
		output = output + fib[i]
	
	return output 
			
	

def main():
	
	number = eval(input("Enter a number: "))
	print()
	
	
	yo = convert_fib_base(number)
	
	print (number, '=', yo + ' (fib)')

	
	
main()
'''
'''
def main():

	#open the file for reading 
	infile = open('Census_2009.txt', 'r')
	
	#create dictionary, populate dictionary
	dict = {}
	
	dict['0'] = 0
	dict['1'] = 0
	dict['2'] = 0
	dict['3'] = 0
	dict['4'] = 0
	dict['5'] = 0
	dict['6'] = 0
	dict['7'] = 0
	dict['8'] = 0
	dict['9'] = 0
	
	#manipulate infile data
	for line in infile:
		line = line.strip()
		pop_data = line.split()
		
		pop_num = pop_data[-1] 
		pop_digit = pop_num[0]
		
		dict[pop_digit] += 1 
	
	for key in dict:
		print (dict[key])
	
	
main()
'''

string = 'Kitten'
new = ''
for i in range(1, len(string) + 1):
	new += string[:i]
	print (new, i)
print (string[:0])


	

