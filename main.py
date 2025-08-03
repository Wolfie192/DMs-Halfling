import os


def main():
	directories: dict[str: os.path] = {}

	if not os.path.exists("Import"):
		os.mkdir("Import")
	directories["imports"] = os.path.abspath("Import")
	
	finished_imports_dir = os.path.join(directories["imports"], "Finished")
	if not os.path.exists(finished_imports_dir):
		os.mkdir(finished_imports_dir)
	directories["finished imports"] = finished_imports_dir
	

main()
