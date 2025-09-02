import os
import sys
import shutil

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def close():
	sys.exit()


def width() -> int:
	return shutil.get_terminal_size().columns

def height() -> int:
	return shutil.get_terminal_size().lines
