# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 4

#==========================================
# Purpose: vertical checks a list of lists to see if the same value is present across all columns
# Input Parameter(s): board, which is a list of 3 lists, each sublist containing 3 elements
# Return Value(s): either one of the two values in the board list, or None
#==========================================

def vertical(board):
	if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
		return board[0][0]
	
	elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
		return board[0][1]
	
	elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
		return board[0][2]
	
	else:
		return None

#==========================================
# Purpose: horizontal checks a list of lists to see if the same value is present across all rows
# Input Parameter(s): board, which is a list of 3 lists, each sublist containing 3 elements
# Return Value(s): either one of the two values in the board list, or None
#==========================================

def horizontal(board):
	if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
		return board[0][0]
	
	elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
		return board[1][0]
	
	elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
		return board[2][0]
	
	else:
		return None

#==========================================
# Purpose: diagonal checks a list of lists to see if the same value is present across all diagonals
# Input Parameter(s): board, which is a list of 3 lists, each sublist containing 3 elements
# Return Value(s): either one of the two values in the board list, or None
#==========================================

def diagonal(board):
	if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
		return board[0][0]
	
	elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
		return board[2][0]
	
	else:
		return None

#==========================================
# Purpose: find_winner uses all three previously defined functions to find a winner in a game of tic-tac-toe
# Input Parameter(s): board, which is a list of 3 lists, each sublist containing 3 elements
# Return Value(s): either one of the two values in the board list, or Draw, if all functions return None
#==========================================

def find_winner(board):
	if horizontal(board) != None:
		return horizontal(board)
	
	elif vertical(board) != None:
		return vertical(board)
	
	elif diagonal(board) != None:
		return diagonal(board)
	
	else:
		return "Draw"
