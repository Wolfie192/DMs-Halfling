import os

import MainWindow
import pdf


def main():
	bin_dir = os.path.abspath("./bin")
	pdf.check_dir(bin_dir)
	
	MainWindow.run(bin_dir)
	

main()
