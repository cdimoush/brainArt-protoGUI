import threading
import subprocess
import time

boot_preview = False

subprocess.call('python3 art/art_generator.py', shell=True)  # Boot the art gene

while not boot_preview:
	try:
		check = subprocess.getoutput('ps ~A')  # makes a list of all programs that are running
		if 'art_generator' not in check:  # If the art generater program is no longer running
			boot_preview = True
	except KeyboardInterrupt: 
		exit()

subprocess.call('python3 art_preview.py', shell=True)  # Boot the preview GUI