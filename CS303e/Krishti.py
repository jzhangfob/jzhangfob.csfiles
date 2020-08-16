def firstLast(u):
	return u[0] == 6 or u[-1] == 6

#function to create a new list in ascending order 
def ascending(list, new_list):
	min_n = list[0]
	while len(list) != 0:
		min_n = list[0]
		for i in range(len(list)):
			if list[i] <= min_n:
				min_n = list[i]
		new_list.append(min_n)
		list.remove(min_n)
	return new_list

#unlucky 13: sum up all numbers in list except for 13 and number preceding 13 	
def sum13(nums):
	sum = 0
	for i in range(len(nums)):
		sum += nums[i]
	for i in range(len(nums)):
		if nums[i] == 13 and i == len(nums) - 1:
			sum -= 13
		elif nums[i] == 13:
			sum -= 13
			if nums[i+1] != 13:
				sum -= nums[i+1]
	return sum 
 
def sum13(nums):
	sum = 0
	for i in range(0, nums.count(13)):
	if nums.count(13):
		after = nums.index(13)
		nums.remove(13)
		if after < len(nums):
			nums.pop(after) #pop removes and returns last object or (obj) index from the list 
	for i in nums:
		sum += i
	return sum

#Sum up all the numbers except every 6 to the next 7 
def sum67(nums):
	sum = 0
	add = 'yes'
	for i in range(len(nums)):
		if add == 'yes':
			if nums[i] == 6:
				add = 'no'
			else:
				sum += nums[i]
		else:
			if nums[i] == 7:
				add = 'yes'
	return sum 
	
def main():
	list = [1,2,3,4,5,6]
	a = firstLast(list)
	print (a)
	
	new_list = []
	list = [9,8,7,6,5,4]
	
	b = ascending(list, new_list)
	print (b)
	
	
	

main()