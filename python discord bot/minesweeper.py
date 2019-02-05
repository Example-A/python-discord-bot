


import numpy as np
import random

#I made the board extra big to stop errors for counting the number of bombs around each square

#X_input and Y_input
#X_input = 5
#Y_input = 5
#Bombnum = 5
#startnumber = 0

#should have a 1 thick square of no bombs
#"board" is the matrix

#will returm a board with dimesnions x and y input with Bombnum bombs
def generateboard(X_input,Y_input,Bombnum):
	
	#Y_input +=1
	startnumber = 0
	#make a board that is x by y by 2, layer one is for the bombs and numbers, layer 2 is for the flags and stuff to be placed
	board = np.full((X_input+2, Y_input+2),2,"X")

	#print (board)
	while True:
		#can improve randomness here
		bomb_X = random.randint(0,X_input-1)
		bomb_Y = random.randint(0,Y_input-1)
		
		if startnumber == Bombnum:
			break
			
		if board[bomb_X+1,bomb_Y+1,0] == "B":
			pass
		else:
			board[bomb_X+1,bomb_Y+1,0] = "B"
			startnumber += 1
	
	#board has all bombs planted		
	#print (board)
	#print("testing",end="")
	#print("testing")
	
	print("Y:"+str(Y_input))
	print("X:"+str(X_input))
	for x in range(X_input):
		for y in range(Y_input):
			if board[x+1,y+1,0] == "X":
				value = 0
				#go through all squares around it and try adding them to the value, even if they're off the board
			
				#top right
				value += int(board[x,y,0]=="B")
				if board[x,y,0]=="B":
					print(x,",",y,"left up is bomb")
				
				value += int(board[x,y+1,0]=="B")
				if board[x,y+1,0]=="B":
					print(x,",",y,"left middle is bomb")	
					
				value += int(board[x,y+2,0]=="B")
				if board[x,y+2,0]=="B":
					print(x,",",y,"left below is bomb")	
					
				value += int(board[x+1,y,0]=="B")
				if board[x+1,y,0]=="B":
					print(x,",",y,"above is bomb")	
					
				value += int(board[x+1,y+2,0]=="B")
				if board[x+1,y+2,0]=="B":
					print(x,",",y,"below is bomb")	
					
				value += int(board[x+2,y,0]=="B")
				if board[x+2,y,0]=="B":
					print(x,",",y,"right above is bomb")	
					
				value += int(board[x+2,y+1,0]=="B")
				if board[x+2,y+1,0]=="B":
					print(x,",",y,"right is bomb")	
					
				value += int(board[x+2,y+2,0]=="B")
				if board[x+2,y+2,0]=="B":
					print(x,",",y,"right below is bomb")	
				
				board[x+1,y+1,0] = str(value)
	#print(board)		


	#pay attention to this, might get messed up

	#make a 2 dimensional array that's the first one
	temparray= board(:,:,0)

	temparray = np.delete(temparray,(0,0),0)	
	temparray = np.delete(temparray,(0,0),1)
	#print(temparray)	
	temparray = np.delete(temparray,(X_input),0)
	#print(temparray)
	temparray = np.delete(temparray,(X_input,Y_input),1)
	#print(temparray)
	board(:,:,0 = temparray)
	return(temparray)

def boardtoemoji(boardin):
	boardout = ""

	for x in range(int(boardin.size/boardin[0].size)):
		for y in range(boardin[0].size):	
			
			#append emoji text to outout
			if boardin[x,y]=="0":
				boardout += "||:zero:||"
			elif boardin[x,y]=="1":
				boardout += "||:one:||"
			elif boardin[x,y]=="2":
				boardout += "||:two:||"
			elif boardin[x,y]=="3":
				boardout += "||:three:||"
			elif boardin[x,y]=="4":
				boardout += "||:four:||"
			elif boardin[x,y]=="5":
				boardout += "||:five:||"
			elif boardin[x,y]=="6":
				boardout += "||:six:||"
			elif boardin[x,y]=="7":
				boardout += "||:seven:||"
			elif boardin[x,y]=="8":
				boardout += "||:eight:||"
			else:
				boardout += "||:bomb:||"
		boardout += "\n"
	if boardout == "":
		boardout = "no board"
	return boardout

def tap(X_input,Y_input,boardin):
	board = boardin
	gamestate= 0
	"""
	VALUES OF GAMESTATE

	0	Game is bieng played
	1	Game has been lost
	2	Game has been won

	SYMBOL MEANINGS

		LAYER 1				LAYER 2
	B	bomb				marked bomb
	X	placeholder, 		untapped
	0-8 number of bombs		number to show
	Q						Question marked
	E						exploded bomb
	"""

	if board(X_input,Y_input,0) == "B":
		gamestate = 1
		board(X_input,Y_input,1) = "E"
	else:
		board(X_input,Y_input,1) = board(X_input,Y_input,0)
	

	return board,gamestate


if __name__ == "__main__"	:
	main()
				
				
				
			
			
			
			
			
			
			
			
			
			
