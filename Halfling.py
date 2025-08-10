from classes.Window import MainWindow
from tools import ScenarioManager as sm


def start_app(bin_dir):
	main_window = MainWindow(bin_dir)
	main_window.build()
	main_window.main_loop()
	
	sm.setup_new_session(bin_dir, main_window.season, main_window.scenario)
	#TODO Process scenario and create pages, get variables, etc.
	
	#TODO create scenario object with pages and variables, then create initial save file.
	
	#TODO Load first page
	
