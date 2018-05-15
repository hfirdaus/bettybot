#C:\Users\bsdueck\Dropbox\IFTTT
from pathlib import Path
import os
import time
import winsound


yes_file = Path("IFTTT\\yes.txt")
no_file = Path("IFTTT\\no.txt")

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

def TimeForYourPills():
	winsound.PlaySound('wavfile\\TimeForYourPills.wav', winsound.SND_FILENAME)
	start = time.clock()
	time.sleep(30) #for now
	winsound.PlaySound('wavfile\\HereAreYourPills.wav', winsound.SND_FILENAME)
	start = time.clock()
	while True:
		time.sleep(5)
		end = time.clock()
		counter = 1
		while True:
			winsound.PlaySound('wavfile\\HaveYouTakenPills.wav', winsound.SND_FILENAME)
			bool = noInput()
			if bool == 3:
				if (counter == 3):
					winsound.PlaySound('wavfile\\NoPillNoChill.wav', winsound.SND_FILENAME)
					exit()
				counter += 1
				bool = 0
			if bool != 0:
				if bool == 1:
					winsound.PlaySound('wavfile\\AllClear.wav', winsound.SND_FILENAME)
					return
				elif bool == 2:
					if (counter == 3):
						winsound.PlaySound('wavfile\\NoPillNoChill.wav', winsound.SND_FILENAME)
						exit()
					winsound.PlaySound('wavfile\\Remind.wav', winsound.SND_FILENAME)
					time.sleep(10)
					counter += 1

def noInput():
	start = time.clock()
	while True:
		end = time.clock()
		bool = checkfile()
		if ((end-start) > 20):
				bool = 3
		if bool != 0:
			return bool
				
######################
##MAIN
######################
#need to check for file
TimeForYourPills();
