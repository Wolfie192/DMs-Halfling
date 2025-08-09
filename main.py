import os

import Halfling
import pdf


def main():
	bin_dir = os.path.abspath("./bin")
	pdf.check_dir(bin_dir)
	
	Halfling.start_app(bin_dir)
	

main()
