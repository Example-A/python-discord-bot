# Work with Python 3.6
import discord
import numpy as np
import os
import sys

#add minesweeper.py to the path
pathstring = "C:/Users/Owner/Downloads/python discord bot/minesweeper.py"
sys.path.append(os.path.abspath(pathstring))
import minesweeper

TOKEN = 'NTQxMTI1NTk3MjkyOTIwODMy.Dza62g.57Fa3vKZ02U-BURXTabaO35gs0o'

#mboard is the current board
#boardX and BoardY are length and height respectivley

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!startminesweeper'):
		#input should be !minesweeper X,Y,B
		#x is length, Y is height, b is number of bombs
		input = message.content
		print(input)
		input_coordinates = ""
		X_input = ""
		Y_input = ""
		B_input = "" # number of bombs
		progressnumber = 0
		
		#X and Y are swapped
		for n in input:
			if n== "0" or\
				n== "1" or \
				n== "2" or \
				n== "3" or \
				n== "4" or \
				n== "5" or \
				n== "6" or \
				n== "7" or \
				n== "8" or \
				n== "9":
				if 	progressnumber == 0:
					X_input += n
				elif progressnumber == 1:
					Y_input += n
				elif progressnumber == 2:
					B_input += n
			elif n == ",":
				progressnumber += 1		
		
		#sanitize input
		X_input = int(X_input)
		Y_input = int(Y_input)
		B_input = int(B_input)
		
		#set these to true if numbers too big
		
		error = False
		
		#abort if X input is out of range
		if X_input > 30 or X_input < 0:
			await client.send_message(message.channel, ("X input: "+str(X_input)+" is out of range").format(message))
			return
			error = True
			
		#abort if Y input is out of range
		if Y_input > 30 or Y_input < 0:
			await client.send_message(message.channel, ("Y input: "+str(Y_input)+" is out of range").format(message))
			return
			error = True
		
		#abort if B input is out of range
		if B_input > 30 or B_input < 0:
			await client.send_message(message.channel, ("B input:"+str(B_imput)+" is out of range").format(message))
			return
			error = True
		
		#print and stuff if no error
		if not error:
			print("X:",X_input)
			print("Y:",Y_input)
			print("B:",B_input)
		
			mboard = minesweeper.generateboard(X_input,Y_input,B_input)
			print(mboard)
			#print (minesweeper.boardtoemoji(mboard))
			await client.send_message(message.channel, ("""minesweeper.boardtoemoji("""mboard""")""").format(message))
	
	if message.content.startswith('!tap'):
		
		input = message.content
		X_input = ""
		Y_input = ""
		progressnumber = 0
		
		#X and Y are swapped
		for n in input:
			if n== "0" or\
				n== "1" or \
				n== "2" or \
				n== "3" or \
				n== "4" or \
				n== "5" or \
				n== "6" or \
				n== "7" or \
				n== "8" or \
				n== "9":
				if 	progressnumber == 0:
					X_input += n
				elif progressnumber == 1:
					Y_input += n
			elif n == ",":
				progressnumber += 1		
		
		#sanitize input
		X_input = int(X_input)
		Y_input = int(Y_input)
		
		#set these to true if numbers too big
		
		error = False
		
		#abort if X input is out of range
		if X_input > boardX or X_input < 1:
			await client.send_message(message.channel, ("X input: "+str(X_input)+" is out of range").format(message))
			return
			error = True
			
		#abort if Y input is out of range
		if Y_input > boardY or Y_input < 1:
			await client.send_message(message.channel, ("Y input: "+str(Y_input)+" is out of range").format(message))
			return
			error = True
		
		#print and stuff if no error
		if not error:
			print("X:",X_input)
			print("Y:",Y_input)
			#add code fot testing the bomb
			
			mboard,gamestate = minesweeper.tap(X_input,Y_input,mboard)
			print(mboard)
			msg = (mboard(:,:,1)).format(message)
			await client.send_message(message.channel, msg)

"""
	if message.content.startswith('!flag'):

	if message.content.startswith('!questionmark'):"""





			
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)