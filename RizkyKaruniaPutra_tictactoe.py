# Rizky Karunia Putra
# Python 3.5

# import library to random number
import random

# Create a procedure to print Tic-Tac-Toe board with parameter board as list
def tictactoeBoard(board):
	# Alocatated list of board just to fit our Tic-Tac-Toe board 3 x 3 and print it to console
	print("   |   |  ")
	print(" "+board[7]+" | "+board[8]+" | "+board[9])
	print("___|___|___")
	print("   |   |  ")
	print(" "+board[4]+" | "+board[5]+" | "+board[6])
	print("___|___|___")
	print("   |   |  ")
	print(" "+board[1]+" | "+board[2]+" | "+board[3])
	print("   |   |  ")

# Create a function to check who's gonna be a winner with two parameter board and the letter
def checkWin(board, letter):
	# In this function we just create the posibility to win a game
	if (board[1] == letter and board[2] == letter and board[3] == letter) or \
	(board[4] == letter and board[5] == letter and board[6] == letter) or \
	(board[7] == letter and board[8] == letter and board[9] == letter) or \
	(board[1] == letter and board[4] == letter and board[7] == letter) or \
	(board[2] == letter and board[5] == letter and board[8] == letter) or \
	(board[3] == letter and board[6] == letter and board[9] == letter) or \
	(board[1] == letter and board[5] == letter and board[9] == letter) or \
	(board[3] == letter and board[5] == letter and board[7] == letter):
	# If this condition is fulfilled, and then return 1 just to show that our game has a winner
		return 1

# Create a function to check the game produce a tie or not
def isFull(board):
	# We need a looping to check is our board is occupied or not
	for i in range(1,10):
		if board[i] == " ":
			# If there a row that still empty then we return that our function is false
			return False
	return True

# Create a procedure to provide our player's movement
def playerMove(board):
	# The first thing that we must do, is check our input to ensure that inputs are validated
	# This one is to avoid a character being stored
	while True:
	    try:
	        x = int(input("Player's move: "))
	    except ValueError:
	        print("Sorry, Just input a number.")
	        continue
	    else:
	        break
	# This one is to avoid a integer higher than 9 and lower than 1 being stored
	while int(x) < 1 or int(x) > 9:
		print("Sorry, Try other move!!")
		x = int(input("Player's move: "))

	# This one is to make sure only allows empty spot to be selected
	while board[int(x)] != " ":
		print("Sorry, Try other move!!")
		x = int(input("Player's move: "))

	# And then we return the value
	return int(x)

# Create a function to provide our AI computer's movement
def comMove(board, player_letter, com_letter):
	# We need provide a knowledge to our AI that maybe the next step AI can win
	# Create a looping from 1 to 9 to simulate a possible movement
	for i in range(1,10):
		# The first step is make a copy of our board to help AI simulate a possible movement
		copy = board.copy()
		# And then make a possibility by inputing every rows from 1 to 9
		if copy[i] == " ":
			copy[i] = com_letter
			# Call the function to check is AI win or not
			if checkWin(copy, com_letter):
				# If AI win, we return the index
				return i
				break
	# If step one failed, we can make a movement by blocking player's movement
	for i in range(1,10):
		# The first step is make a copy of our board to help AI simulate a possible movement
		copy = board.copy()
		# And then make a possibility by inputing every rows from 1 to 9
		if copy[i] == " ":
			copy[i] = player_letter
			# Call the function to check is player win or not
			if checkWin(copy, player_letter):
				# If player win, we return the index
				return i
				break
	# If step one and two failed, we can just place our letter in the center
	if board[5] == " ":
		return 5
	# If step three failed to, we can random our movement
	while True:
		# With library random, we random number from 1 to 9
		x = random.randint(1, 9)
		if board[x] == " ":
			# And then, we return the index
			return x
			break

# Create function of player just to make our code little bit nicer
def player(board, player_letter):
	# Initialitazion our variable with a function playerMove
	move = playerMove(board)
	# Assign player_letter to board list by index move
	if board[move] == " ":
		board[move] = player_letter

	# Call procedure to show the board
	tictactoeBoard(board)

	# Check if player win againt AI
	if checkWin(board, player_letter):
		print()
		tictactoeBoard(board)
		print("Player's Win!!!")
		loop = False
		return loop

	# Check if there no winner
	if isFull(board)==True:
		print("\nTie")
		loop = False
		return loop

# Create function of computer just to make our code little bit nicer
def computer(board, player_letter, com_letter):
	# Initialitazion our variable with a function comMove
	move = comMove(board, player_letter, com_letter)

	print("Computer's move: "+ str(move))
	# Assign com_letter to board list by index move
	if board[move] == " ":
		board[move] = com_letter

	# Call procedure to show the board
	tictactoeBoard(board)

	# Check if AI win againt Player
	if checkWin(board, com_letter):
		print()
		tictactoeBoard(board)
		print("Computer's Win!!!")
		loop = False
		return loop

	# Check if there no winner
	if isFull(board)==True:
		print("\nTie")
		loop = False
		return loop

# Create procedure main
def main():
	# Initialization our board list
	board = [" "] * 10;
	# Call procedure to show the board
	tictactoeBoard(board)
	print()
	print("====================================")
	print()
	# The first thing that we must do, is check our input to ensure that inputs are validated
	while True:
	    player_letter = input("Please choose X or O: ")
	    if player_letter == "X" or player_letter == "O":
	        break
	    else:
	        print("Sorry, Try to choose X or O.")
	        continue
	# Assign com_letter with "O" if player_letter is "X" and com_letter "O" if player_letter is "X"
	if player_letter == "X":
		com_letter = "O"
	else:
		com_letter = "X"

	loop = True
	# Random starting turn of game between player and AI
	start = random.randint(1,2)
	while loop:
		# If start is 1 and then player first and computer second
		if start == 1:
			if player(board, player_letter) == False:
			 	break
			print()

			if computer(board, player_letter, com_letter) == False:
				break
			print()
		# If start is 2 and then computer first and player second
		else:
			if computer(board, player_letter, com_letter) == False:
				break
			print()

			if player(board, player_letter) == False:
			 	break
			print()

# Call procedure main to make our program running
main()