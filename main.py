import os
import src.pdf_importer.cui.main_menu as pdf_importer
from src.console import console


def main():
	bin_dir = check_dir("bin")
	src_dir = check_dir("src")
	import_dir = check_dir("Import")
	
	modules_dir = os.path.join(bin_dir, "modules")
	if not os.path.exists(modules_dir):
		os.mkdir(modules_dir)
	
	directory: dict = {
		"bin": bin_dir,
		"src": src_dir,
		"import": import_dir,
		"modules": modules_dir
	}
	
	display()
	main_loop(directory)
	

def display(exception: Exception = None):
	console.clear()
	print("Dm's Halfling, Pathfinder 2e Society Assistant\n\n")
	
	print("[I]mport PDFs\n\n")

	print("[Q]uit\n\n")


def main_loop(directory: dict):
	while(True):
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "import"|"i"|"import pdfs":
				pdf_importer.run(directory)
				display()
			case _:
				exception = Exception("Invalid Input.")
				display(exception)


def check_dir(dir_name):
	if os.path.exists(f"./{dir_name}"):
		dir_path = os.path.abspath(f"./{dir_name}")
	elif os.path.exists(f"../{dir_name}"):
		dir_path = os.path.abspath(f"../{dir_name}")
	else:
		os.mkdir(f"./{dir_name}")
		dir_path = os.path.abspath(f"./{dir_name}")
	
	return dir_path


main()
