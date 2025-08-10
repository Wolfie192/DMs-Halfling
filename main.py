import Halfling
import os
from tools import PDF


def main():
	bin_dir = os.path.abspath("./bin")
	PDF.check_dir(bin_dir)
	
	Halfling.start_app(bin_dir)
	

main()
