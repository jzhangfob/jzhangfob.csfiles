#  File: ExpresionTree.py
#  Description: Create a binary tree that represents different "Fix" 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E
#  Unique Number: 51325
#  Date Created: 11/29/2016
#  Date Last Modified: 12/1/2016

import operator

class BinaryTree(object):
	def __init__(self, initVal, parent=None):
		self.data = initVal
		self.left = None
		self.right = None
		self.parent = parent

	def createTree (self, expr):
		current = self

		for pos in range(0, len(expr)):

			if (expr[pos] == ')'):

				if (current.parent != None):
					current = current.getParent()
				else:
					current = self

			elif (expr[pos] == '('):

				current.insertLeftTree('tempValL')
				current = current.getLeftTree()

			elif (expr[pos] == '+' or expr[pos] == '-' or expr[pos] == '*' or expr[pos] == '/'):

				current.setRootVal(expr[pos])
				current.insertRightTree('tempValR')
				current = current.getRightTree()

			else:

				current.setRootVal(expr[pos])
				current = current.getParent()

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

	def insertLeftTree(self, val):
		if self.left == None:
			self.left = BinaryTree(val, self)
		else:
			t = BinaryTree(val, self)
			t.left = self.left
			self.left = t 
			t.left.setParent(t)

	def insertRightTree(self, val):
		if self.right == None:
			self.right = BinaryTree(val, self)
		else:
			t = BinaryTree(val, self)
			t.right = self.right	
			self.right = t 
			t.right.setParent(t)

	def getLeftTree(self):
		return self.left

	def getRightTree(self):
		return self.right

	def setRootVal(self,value):
		self.data = value

	def getRootVal(self):
		return self.data

	def evaluate (self):
		opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
		left = self.getLeftTree()
		right = self.getRightTree()
		if type(self.getRootVal()) == int or type(self.getRootVal()) == float:
			return self.getRootVal()
		else:
			fn = opers[self.getRootVal()]
			return fn(left.evaluate(),right.evaluate())



	def preOrder (self, tree):
		list_order = []
		if tree != None: 
			preOrder(tree.getLeftTree())
			preOrder(tree.getRightTree())
			list_order.append(str(tree.getRootVal()))
		return list_order


def main():

	in_file = open('treedata.txt', 'r')
	for line in in_file:
		print('Infix expression:  ' + line)
		expr_tree = BinaryTree('PlaceHolder')
		line = line.split()
		expr_tree.createTree(line)

		print('   Value:  ' + str(evaluateExpr(expr_tree))) 
		print('   Prefix expression:   ', end="")
		preOrder(expr_tree)
		print('\n' + '   Postfix expression:   ', end="")
		postOrder(expr_tree)
		print('\n')

def inOrder(tree):
	if tree != None:
		inOrder(tree.getLeftTree())
		print(tree.getRootVal(), end=" ")
		inOrder(tree.getRightTree())

def postOrder(tree):
   	if tree != None: 
   		postOrder(tree.getLeftTree())
   		postOrder(tree.getRightTree())
   		print(tree.getRootVal(), end=" ")

def preOrder(tree):
	if tree != None:
		print(tree.getRootVal(), end=" ")
		preOrder(tree.getLeftTree())
		preOrder(tree.getRightTree())

def evaluateExpr(parseTree):
	opers_list = ['+','-','*','/']
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

	leftC = parseTree.getLeftTree()
	rightC = parseTree.getRightTree()

	if any(parseTree.getRootVal() in s for s in opers_list): #or type(eval(parseTree.getRootVal())) == float:
		fn = opers[parseTree.getRootVal()]
		# if type(evaluateExpr(leftC)) == str or type(evaluateExpr(rightC)) == str:
		# 	#print(float(evaluateExpr(leftC)), float(evaluateExpr(rightC)))
		# 	return fn(float(evaluateExpr(leftC)), float(evaluateExpr(rightC)))
		# else:
		return fn(float(evaluateExpr(leftC)), float(evaluateExpr(rightC)))

	else:
		return parseTree.getRootVal()

main()
