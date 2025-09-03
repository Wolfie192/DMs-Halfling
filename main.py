import os 
import src.pdf_importer.cui.main_menu as pdf_importer
import src.scenario_runner.cui.select_season as select_season
from src.console import console
from src.configs.directory import DIRECTORY


def main():
	bin_dir = _check_dir("bin")
	src_dir = _check_dir("src")
	import_dir = _check_dir("Import")
	
	modules_dir = os.path.join(bin_dir, "modules")
	if not os.path.exists(modules_dir):
		os.mkdir(modules_dir)
	
	configs_dir = os.path.join(src_dir, "configs")
	
	DIRECTORY["bin"] = bin_dir
	DIRECTORY["src"] = src_dir
	DIRECTORY["import"] = import_dir
	DIRECTORY["modules"] = modules_dir
	DIRECTORY["configs"] = configs_dir
	
	_display()
	_main_loop()
	

def _display():
	console.clear()
	print("Dm's Halfling, Pathfinder 2e Society Assistant\n\n")
	
	print("[I]mport PDFs")
	print("[S]tart New Scenario\n\n")

	print("[Q]uit\n\n")


def _main_loop():
	while True:
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "import"|"i"|"import pdfs":
				pdf_importer.run()
				_display()
			case "s"|"start"|"start new"|"start new scenario"|"new"|"scenario":
				select_season.run()
				_display()
			case _:
				_display()


def _check_dir(dir_name):
	if os.path.exists(f"./{dir_name}"):
		dir_path = os.path.abspath(f"./{dir_name}")
	elif os.path.exists(f"../{dir_name}"):
		dir_path = os.path.abspath(f"../{dir_name}")
	else:
		os.mkdir(f"./{dir_name}")
		dir_path = os.path.abspath(f"./{dir_name}")
	
	return dir_path


main()
