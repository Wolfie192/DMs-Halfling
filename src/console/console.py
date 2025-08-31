import os
import sys

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def close():
	sys.exit()
