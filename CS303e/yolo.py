for a in range(3):
	for b in range(a + 1): 
		print ("*", end = '')
	print ()
for c in range(2, -1, -1):
	for d in range(c):
		print ("*", end = '')
	print ()

list = [1,1,1,1,2]

for i in range(len(list) -1, -1, -1):
	if list[i] == 1:
		print (i)
		break 

list2 = [1,2,3,4]
while len(list2) > 0:
	j = 0
	while j < 5:
		print (list2[0], end = ' ')
		list2.remove(list2[0])
		if len(list2) == 0:
			break
		j += 1
	print()
