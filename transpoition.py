#! /usr/bin/env python
import math
from colorama import Fore,init
init()
G = Fore.GREEN
Y = Fore.YELLOW
R = Fore.RESET
def decrypt(text):
	key = int(input("Enter Key:"))
	columns = round(len(text)/key)
	final = [""] *key
	rows= key
	shaded = (columns*rows)-len(text)
	column = 0
	row = 0
	for l in text:
		final[column] += l
		column+=1
		if (column == columns) or (column == columns-1 and row >= rows - shaded ):
			row+=1
			column = 0
	res = "".join(final)
	print(f"{Y}{res}{R}")

def encrypt(text,key):
	final = [""]*key
	for j in range(0,len(text),key):
		for i in range(key):
			if(i+j<len(text)):
				final[i]+=text[i+j]
	res = ""
	for i in range(len(final)):
		res+=(final[i])
	print(f"{Y}{res}")


while True:
	choose = input(f"{G}Enter E for encrypt,Enter D for decrypt\nType exit for closing of program:{R}")
	if choose == "exit":
		break
	elif choose == "E":
		message = input("Enter message to encrypt:  ")
		key = int(input("Enter key to encrypt:  "))
		encrypt(message,key)
	elif choose == "D":
		message = input("Enter message to decrypt:  ")
		decrypt(message)
	else:
		print("Try again, i dont understand")
final = [""]*8

