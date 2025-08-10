from MainWindow import MainWindow


def start_app(bin_dir):
	main_window = MainWindow(bin_dir)
	main_window.build()
	main_window.main_loop()
	
	print(main_window.season, main_window.scenario)
	
