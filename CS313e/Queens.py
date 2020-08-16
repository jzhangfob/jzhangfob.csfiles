#  File: Queens.py
#  Description: Create a program that will place n queens on a board size of n so that none of the queens attack each other 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/09/2016
#  Date Last Modified: 11/12/2016 


#Create the class 
class QueensProblem(object):
	
	#Create a board that is empty 
    def __init__(self, size):
        self.board = ["*"]*size
        self.counter = 1
	
	#Validation method 
    def isValidPlace(self, size):
        for i in range(size):
            if (self.board[i] == self.board[size]):
                return False
            elif ((self.board[i] - self.board[size]) == (size - i)):
                return False
            elif ((self.board[size] - self.board[i]) == (size - i)):
                return False
        return True
	
	#Recursive solve method 
    def solve(self, q):
        n = len(self.board)
        if (q == n):
            print("Solution #", self.counter)
            self.counter += 1
            print (str(self))
        else:
            for i in range(n):
                self.board[q] = i
                if self.isValidPlace(q):
                    self.solve(q+1)
        
	#Print method 
    def __str__(self):

        new_string = ""
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if (self.board[i] == j):
                    new_string += "Q"
                else:
                    new_string += "*"
            new_string += "\n"
        new_string += "\n"
        return new_string

def main():
	#Ask the user for input 
    size = int(input("Enter the size of the board: "))
	#Print an error message for size < 4 
    while size < 4:
        print("Invalid input")
        size = int(input("Enter the size of the board: "))
    board = QueensProblem(size)
    board.solve(0)

main()
