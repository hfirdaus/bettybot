#C:\Users\bsdueck\Dropbox\IFTTT
from pathlib import Path
import os
import time
import winsound


yes_file = Path("IFTTT\\yes.txt")
no_file = Path("IFTTT\\no.txt")
fall_file = Path("IFTTT\\actualfall.txt")

def checkfile():
	#check if there is a yes file that exists
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
		return 2
		
	#there is no file		
	else:
		return 0


	
		
		
#ARE YOU OKAY?
def AreYouOkay():
	winsound.PlaySound('wavfile\\AreYouOk.wav', winsound.SND_FILENAME)
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				#PLAY LOUD NOISE and say i havent detected anything
				winsound.PlaySound('wavfile\\AreYouOk.wav', winsound.SND_FILENAME)
				bool = noInput()
		if bool != 0:
			if bool == 1:
				#if they are okay ask if they are in any pain
				print("$ - The person said yes")
				pain()
			elif bool == 2:
				#if they are not, call emergency
				print("$ - The Person Said No")
				Emergency()
				

def pain():
	winsound.PlaySound('wavfile\\AnyPain.wav', winsound.SND_FILENAME)
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				#PLAY LOUD NOISE and say i havent detected anything
				winsound.PlaySound('wavfile\\AnyPain.wav', winsound.SND_FILENAME)
				bool = noInput()
		if bool != 0:
			if bool == 1:
				#the person said they are in pain, emergency
				print("$ - The person said yes")
				Emergency()
				
			elif bool == 2:
				#if they are not, ask if they can get up
				print("$ - The Person Said No")
				CanYouGetUp()

				
def CanYouGetUp():
	winsound.PlaySound('wavfile\\CanYouGetUp.wav', winsound.SND_FILENAME)
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				#PLAY LOUD NOISE and say i havent detected anything
				winsound.PlaySound('wavfile\\CanYouGetUp.wav', winsound.SND_FILENAME)
				bool = noInput()
		if bool != 0:
			if bool == 1:
				#the person said they can get up, check to see if up
				print("$ - The person said yes")
				WaitTillUp()
			elif bool == 2:
				#if they are not, call emergency
				print("$ - The Person Said No")
				Emergency()

				
				
				
def Emergency():
	winsound.PlaySound('wavfile\\Emergency.wav', winsound.SND_FILENAME)
	os.remove(fall_file)
	exit()

def noInput():
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				bool = 2
				Emergency()
		if bool != 0:
			if bool == 1:
				return bool
			elif bool == 2:
				#if they are not, call emergency
				return bool
				#print("$ - The Person Said No")
				#Emergency()
				
def WaitTillUp():
	#add the logic for yes and no
	time.sleep(5)
	areYouDizzy()
	exit()
	
	
def areYouDizzy():
	winsound.PlaySound('wavfile\\NowUpPainOrDizziness.wav', winsound.SND_FILENAME)
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				#PLAY LOUD NOISE and say i havent detected anything
				winsound.PlaySound('wavfile\\NowUpPainOrDizziness.wav', winsound.SND_FILENAME)
				bool = noInput()
		if bool != 0:
			if bool == 2:
				#the person said they can get up, check to see if up
				print("$ - The person said no")
				winsound.PlaySound('wavfile\\AllClear.wav', winsound.SND_FILENAME)
				os.remove(fall_file)
				exit()
			elif bool == 1:
				#if they are dizzy or in pain, call emergency
				print("$ - The Person Said Yes")
				Emergency()
	
	
######################
##MAIN
######################
#need to check for file
while True:
	if fall_file.is_file():
		AreYouOkay()


