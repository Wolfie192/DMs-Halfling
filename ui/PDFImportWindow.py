import os
import FreeSimpleGUI as sg

from tools import pdf_extractor


def build(directories) -> sg.Window:
	sg.theme("DarkGrey")
	
	window_layout = [
		[main_column()]
	]
	
	window = sg.Window("PDF Importer", window_layout, relative_location = (0, 0), resizable = True, element_padding = 10, margins = (10, 10))
	
	main_loop(window, directories)
	
	return window


def main_loop(window, directories):
	while True:
		event, values = window.read(timeout = 1000)
		if event == sg.WIN_CLOSED:
			window.metadata = "Win Closed"
			break
		if event == "Import Selected Button":
			files = values["Selected Files Input"].split(";")
			for file in files:
				file_path = os.path.abspath(file)
				error = pdf_extractor.extract_file(directories, file_path)
				if error:
					window.metadata = error
			break
					
	window.close()


def main_column() -> sg.Column:
	files_selected = sg.In(key = "Selected Files Input", expand_x = True)
	files_picker = sg.FilesBrowse("Browse", target = "Selected Files Input", file_types = (("PDFs", "*.pdf"),))
	import_button = sg.Button("Import Selected", key = "Import Selected Button")
	
	layout = [
		[files_selected],
		[files_picker, import_button]
	]
	
	return sg.Column(layout, key = "Main Column", expand_x = True, expand_y = True)
