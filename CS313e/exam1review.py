#list1 = [1,2,3,4,5]
#list2 = [1,2,3,4,5]

#for i in range(len(list1)):
#	if list1[i] == list2[i]:
#		print ("True")
#	else:
#		print ("False")

class Fraction:
	#Constructor method to give the object a numerator and denominator
	def __init__(self, numerator, denominator):
		
		self.num = numerator 
		self.den = denominator 
	
	#Dunder equal method to check if two fractions are equal by cross multiplying
	def __eq__(self, other):
		
		first_num = self.num * other.den 
		second_num = other.num * self.den 
		
		return first_num == second_num 
	
#Function for greatest common denominator
def gcd(m,n):
	while m % n != 0:
		old_m = m
		old_n = n 
		
		m = old_n
		n = old_m % old_n 
	return n 
print (gcd(3,15))

object1 = Fraction(1,2)
object2 = Fraction(2,4)

print (object1 == object2)


if object1 is object2:
	print ("True!")
else:
	print ("False")

#Example of shallow equality: prints "True" because object2 references the same location in memory as object1 (object 2 points to object1)
#This statement just got overrided by the __eq__ method for equality!!!
if object1 == object2:
	print ("Truuuu")
else:
	print ("False")
