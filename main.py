import os

import ui.MainWindow as MainWindow


def check_dir(dir_path):
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)


def main():
	directories: dict = {}
	
	bin_dir = os.path.abspath("./bin")
	check_dir(bin_dir)
	directories["Bin"] = bin_dir
	
	modules_dir = os.path.join(bin_dir, "Modules")
	check_dir(modules_dir)
	directories["Modules"] = modules_dir
	
	saves_dir = os.path.join(bin_dir, "Saves")
	check_dir(saves_dir)
	directories["Saves"] = saves_dir
	

	
	
	MainWindow.build(directories)
	

main()
