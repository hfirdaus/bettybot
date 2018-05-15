#C:\Users\bsdueck\Dropbox\IFTTT
from pathlib import Path
import os
import time
import winsound
import subprocess
import os

play_game_file = Path("IFTTT\\game.txt") #needs to be the location where the game is being played
game_file = Path("Google\\move.txt") #needs to be the location where the game is being played
yes_file = Path("IFTTT\\yes.txt")
no_file = Path("IFTTT\\no.txt")

#Game is consisting of 5 sequences
#stage 1 - 	right -> up
#stage 2 -	right -> up -> left
#stage 3 -	right -> up -> left -> left 
#stage 4 -	right -> up -> left -> left -> right 
#stage 5 -	right -> up -> left -> left -> right -> down
#			1		3		2		2		1		4

#Right 	= 	1
#Left 	= 	2
#Up 	=	3
#Down 	= 	4

#check to see if they have responded
def checkfile():
	#check if there is a game file that exists
	while True:
		if game_file.is_file():
			time.sleep(1)
			return 1

def checkfile2():
	while True:#check if there is a yes file that exists
		if yes_file.is_file():
			time.sleep(1)
			while True:
				try:
					os.remove(yes_file)
					break
				except:
					pass
			return 1
			
		#check if there is a no file that exists
		elif no_file.is_file():
			time.sleep(1)
			while True:
				try:
					os.remove(no_file)
					break
				except:
					pass
			winsound.PlaySound('wavfile\\Thanks.wav', winsound.SND_FILENAME) # want to play again?
			exit()
		#there is no file
		
		
def checkfile3():
	#check if there is a game file that exists
	start = time.clock()
	while True:
		if play_game_file.is_file():
			time.sleep(1)
			while True:
				try:
					os.remove(play_game_file)
					break
				except:
					pass
			return 1	
			
def parseInput():
	input = ''
	while True:
			try:
				f = open(game_file)
				break
			except:
				pass
	for line_of_text in f:
		list = line_of_text.split(' ')
		for g in list:
			if g == 'right':
				input = input + '1'
			elif g == 'left':
				input = input + '2'
			elif g == 'up':
				input = input + '3'
			else:
				input = input + '4'
	print (input)
	f.close()
	return input
	
	
#check the file input to see if the move is correct
def checkmove(round):
	print ("checkmove")
	print ("round", round)
	#check if there is a game file that exists
	input = parseInput()	
	if round == 1:
		if input == "13":
			return 1
			#Congratulations
		else:
			return 0
			#try again
	elif round == 2:
		if input == "132":
			return 1
			#Congratulations
		else:
			return 0
			#try again
	elif round == 3:
		if input == "1322":
			return 1
			#Congratulations
		else:
			return 0
			#try again
	elif round == 4:
		if input == "13221":
			return 1
			#Congratulations
		else:
			return 0
			#try again
	else:
		if input == "132214":
			return 1
			#Congratulations
		else:
			return 0
			#try again

			
def playround(round):
	test = "C:\\Program Files\\MobileRobots\\Aria\\bin64\\game"
	test = test + str(round) + ".exe"
	os.startfile("C:\\Program Files\\MobileRobots\\Aria\\bin64\\demo.exe")
	return 0

	
	
	
#MAIN
#Hey, How is it going?, want to do something?, I can play music, tell a joke, make a call, or play a memory game!
winsound.PlaySound('wavfile\\WantToDoSomething.wav', winsound.SND_FILENAME)
checkfile3()

round = 1
while round < 6:
	bool = 0
	while bool == 0:
		
		winsound.PlaySound('wavfile\\PlayGame.wav', winsound.SND_FILENAME) #Play the file that says watch closely
		#playround(round) #execute the file
		time.sleep(12 + (round*4)) #need to change this to howeve r long the move takes
		#now you tell me the directions i moved
		winsound.PlaySound('wavfile\\RepeatMoves.wav', winsound.SND_FILENAME) #Play the file that asks them to repeat the moves
		checkfile() #wait for their response
		bool = checkmove(round)
		while True:
			try:
				os.remove(game_file)
				break
			except:
				pass	
		if bool == 0:
			#try again
			winsound.PlaySound('wavfile\\TryAgain.wav', winsound.SND_FILENAME) #Play the file that says watch closely
		else:
			#congrats
			winsound.PlaySound('wavfile\\GotIt.wav', winsound.SND_FILENAME) #Play the file that says watch closely
		winsound.PlaySound('wavfile\\KeepPlaying.wav', winsound.SND_FILENAME) # want to play again?
		checkfile2()

	round = round + 1

