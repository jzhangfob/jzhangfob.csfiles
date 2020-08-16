#  File: Blackjack.py
#  Description: Create a program that will stimulate one round of blackjack between the player and the dealer 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 9/21/2016
#  Date Last Modified: 9/23/2016 

import random 

#Class for card 
class Card:
	
	#Initialize the default method of the class that runs every time an object is created 
	def __init__(self, suit, pip):
		#A suit will be either Heart, Clover, Spade, or Diamond (H, C, S, D)
		self.suit = suit  
		#A pip will be either a number 2-10 or J, Q, K, A
		self.pip = pip 
		#Initialize the value 
		self.value = 0
			
		if self.pip == "A":
			self.value = 11 
		elif pip.isalpha():
			self.value = 10 
		else:
			number = int(pip)
			self.value = number 
		
	def __str__(self):
		return (self.pip + self.suit)
		
#Class for deck 	
class Deck:

	suits = ['C', 'D', 'H', 'S']
	pips = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	
	#Constructor method 
	def __init__(self):
		#Initialize the instance variable cardList
		self.cardList = []
		
		for i in range(len(Deck.suits)):
			for j in range(len(Deck.pips)):
				aCard = Card(Deck.suits[i], Deck.pips[j])
				self.cardList.append(aCard)
	
	#Method to shuffle the deck
	def shuffle(self):
		random.shuffle(self.cardList)
	
	#Deal card method 
	def dealOne(self, player):
		#Add the top card to the player's hand and simultaneously delete the card 
		firstCard = self.cardList[0]
		player.hand.append(firstCard)
		player.handTotal += firstCard.value 
		self.cardList.remove(firstCard)
		
	#Print method 
	def __str__(self):
		return_string = ''
		for i in range(len(self.cardList))	:
			return_string += str(self.cardList[i]).rjust(4)
			if (i == 12 or i == 25 or i == 38 or i == 51):
				return_string += "\n"
		return return_string
				
#Class for players 			
class Player:
	
	def __init__(self):
		self.hand = []
		self.handTotal = 0
		self.blackJack = False 
	
	def __str__(self):
		return_string = ''
		for i in range(len(self.hand)):
			return_string += str(self.hand[i]).ljust(4)	
		return return_string
			
#Function for show hands 	
def showHands(dealer, player):
	
	print ("Dealer shows" + " " + str(dealer.hand[1]) + " faceup")
	print ("You show" + " " + str(player.hand[1]) + " faceup")
	print ()

#Function for the player's turn 
def playerTurn(cardDeck, player, dealer):

	print ("You go first")
	
	totalValue = player.handTotal 
	dealtAce = False 
	blackJack = False 
	flag = False 
	#print (totalValue) -- worked 
	
	for obj in player.hand:
		if "A" in str(obj):
			print ("Assuming 11 points for an ace you were dealt for now")
			dealtAce = True 
			
	print ("You hold " + str(player.hand[0]) + " " + str(player.hand[1]) + \
	" for a total of " + str(totalValue))
	
	if totalValue == 21:
		player.blackJack = True 
		print ("Blackjack!")
		print ("Dealer's turn")
		return 
	
	choice = int(input("1 (hit) or 2 (stay)? "))
	print ()
	
	#Input validation
	while choice != 1 and choice != 2:
		choice = int(input("1 (hit) or 2 (stay)? "))
		print()
	
	if choice == 1:
		while choice != 2:
			nextCard = cardDeck.cardList[0]
			
			if "A" in str(nextCard):
				dealtAce = True 
			player.hand.append(nextCard)
			print ("Card dealt: " + str(nextCard))
			totalValue += nextCard.value 
			player.handTotal += nextCard.value 
			
			#If player busts with an ace 
			if totalValue > 21 and dealtAce:
				print ("Over 21. Switching an ace from 11 points to 1")
				totalValue -= 10 
				player.handTotal -= 10 
				print ("New total: " + str(totalValue))
				print()
				
			#If player busts without an ace 
			elif totalValue > 21 and dealtAce == False:
				print ("You bust!")
				print ("Dealer wins!")
				print()
				return 
				
			#If player gets 21 
			elif totalValue == 21:
				print ("21!")
				cardDeck.cardList.remove(nextCard)
				print()
				break
				
			#If everything is normal and still under 21 
			else:
				print ("New total: " + str(totalValue))
				print()
				
			print ("You hold ", end = '')
			for obj in player.hand:
				print (str(obj), end = ' ')
			print ("for a total of " + str(totalValue))
			cardDeck.cardList.remove(nextCard)
			choice = int(input("1 (hit) or 2 (stay)? "))
			dealtAce = False
			print()
		
		#If player chooses to stay after the first deal 
		if choice == 2:
			print ("You choose to stay. Now it's the dealer's turn")
			flag = True 
	
	#If player chooses to stay after the initial hand 
	if choice == 2 and flag == False :
		print ("You choose to stay. Now it's the dealer's turn")
		
	print ("Dealer's turn")
	print ("Your hand: ", end = '')
	for obj in player.hand:
			print (str(obj), end = ' ')
	print ("for a total of " + str(totalValue))

#Function for the dealer's turn 
def dealerTurn(cardDeck, player, dealer):
	
	totalValue = dealer.handTotal 
	dealtAce = False 
	
	if player.handTotal > 21:
		return
		
	print ("\nDealer's hand: ", end = '')
	for obj in dealer.hand:
		print (str(obj), end = ' ')
	print ("for a total of " + str(totalValue))
	
	#If player got a blackjack
	if player.blackJack == True: 
		if totalValue != 21:
			print ("Dealer didn't get a blackjack. Dealer loses!")
			print ("You win!")
			print ()
			return 
			 
		elif totalValue == 21:
			print ("Dealer also got a blackjack")
			print ("Dealer wins!")
			print ()
			return 
			
	#If not 21, dealer hits until ties or beats player's value 
	if player.blackJack == False:
		#If dealer dealt an ace to himself 
		for obj in dealer.hand:
			if "A" in str(obj):
				print ("Assuming 11 points for an ace you were dealt for now")
				dealtAce = True 
	
		#If dealer surpasses the player 
		if totalValue > player.handTotal:
			print ("Dealer's hand beats yours")
			print ("Dealer wins!")
			print ()
			return 
			
		#If tied with player 	
		elif totalValue == player.handTotal:
			print ("Dealer ties with you")
			print ("Dealer wins!")
			print ()
			return 
				
		while totalValue < player.handTotal:
			#Deal the next card 
			nextCard = cardDeck.cardList[0]
			
			#If ace in the next card that's dealt 
			if "A" in str(nextCard):
				dealtAce = True 
			dealer.hand.append(nextCard)
			#print ("Card dealt: " + str(nextCard))
			totalValue += nextCard.value
			dealer.handTotal += nextCard.value 
			
			print ("Dealer hits: ", end = '')
			print (str(nextCard))
			print ("New total: " + str(totalValue))
			print()	
			
			#If dealer busts with an ace, change the ace to 1 
			if totalValue > 21 and dealtAce == True:
				print ("Over 21. Switching an ace from 11 points to 1")
				totalValue -= 10 
				dealer.handTotal -= 10 
				print ("New total: " + str(totalValue))
				print()
			
			#If dealer busts 
			if totalValue > 21 and dealtAce == False:
				print ("Dealer busts!")
				print ("You win!")
				print ()
				return
			
			#If dealer surpasses the player 
			elif totalValue > player.handTotal:
				print ("Dealer's hand beats yours")
				print ("Dealer wins!")
				print ()
				return 
			
			#If tied with player 	
			elif totalValue == player.handTotal:
				print ("Dealer ties with you")
				print ("Dealer wins!")
				print ()
				return 
				
			cardDeck.cardList.remove(nextCard)
			dealtAce = False 
			
def main():
	
	testCard = Card("H", "A")
	testDeck = Deck()
	print ("Initial deck:\n")
	print (testDeck)
	
	random.seed(24)
	testDeck.shuffle()
	print ("Shuffled deck: \n")
	print (testDeck)
	
	player = Player()
	dealer = Player()
	
	testDeck.dealOne(player)
	testDeck.dealOne(dealer)
	testDeck.dealOne(player)
	testDeck.dealOne(dealer)
	
	print ("Deck after dealing two cards each:\n")
	print (testDeck)
	print ()
	
	showHands(dealer, player)
	
	playerTurn(testDeck, player, dealer)
	dealerTurn(testDeck, player, dealer)
	
	print ("Game over.")
	print ("Final hands: ")
	print ("  Dealer:    ", end = '')
	print (dealer)
	print ("  Opponent:  ", end = '')
	print (player)
	
main()