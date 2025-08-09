from MainWindow import MainWindow
import DMWindow
import PlayerWindow


def start_app(bin_dir):
	main_window = MainWindow(bin_dir)
	main_window.build()
	main_window.main_loop()
	
	main_window.close()
	
	print(main_window.season, main_window.scenario)
	
	
	
