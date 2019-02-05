


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
	board = np.full((X_input+2, Y_input+2),"X")

	#print (board)
	while True:
		#can improve randomness here
		bomb_X = random.randint(0,X_input-1)
		bomb_Y = random.randint(0,Y_input-1)
		
		if startnumber == Bombnum:
			break
			
		if board[bomb_X+1,bomb_Y+1] == "B":
			pass
		else:
			board[bomb_X+1,bomb_Y+1] = "B"
			startnumber += 1
	
	#board has all bombs planted		
	#print (board)
	#print("testing",end="")
	#print("testing")
	
	print("Y:"+str(Y_input))
	print("X:"+str(X_input))
	for x in range(X_input):
		for y in range(Y_input):
			if board[x+1,y+1] == "X":
				value = 0
				#go through all squares around it and try adding them to the value, even if they're off the board
			
				#top right
				value += int(board[x,y]=="B")
				if board[x,y]=="B":
					print(x,",",y,"left up is bomb")
				
				value += int(board[x,y+1]=="B")
				if board[x,y+1]=="B":
					print(x,",",y,"left middle is bomb")	
					
				value += int(board[x,y+2]=="B")
				if board[x,y+2]=="B":
					print(x,",",y,"left below is bomb")	
					
				value += int(board[x+1,y]=="B")
				if board[x+1,y]=="B":
					print(x,",",y,"above is bomb")	
					
				value += int(board[x+1,y+2]=="B")
				if board[x+1,y+2]=="B":
					print(x,",",y,"below is bomb")	
					
				value += int(board[x+2,y]=="B")
				if board[x+2,y]=="B":
					print(x,",",y,"right above is bomb")	
					
				value += int(board[x+2,y+1]=="B")
				if board[x+2,y+1]=="B":
					print(x,",",y,"right is bomb")	
					
				value += int(board[x+2,y+2]=="B")
				if board[x+2,y+2]=="B":
					print(x,",",y,"right below is bomb")	
				
				board[x+1,y+1] = str(value)
	#print(board)		
	board = np.delete(board,(0,0),0)	
	board = np.delete(board,(0,0),1)
	#print(board)	
	board = np.delete(board,(X_input),0)
	#print(board)
	board = np.delete(board,(X_input,Y_input),1)
	#print(board)
	return(board)

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
		
if __name__ == "__main__"	:
	main()
				
				
				
			
			
			
			
			
			
			
			
			
			
