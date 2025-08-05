import FreeSimpleGUI as fsg

import os
import pdf


def bin_directory():
	bin_dir = os.path.abspath("./bin")
	if not os.path.exists(bin_dir):
		os.mkdir(bin_dir)
	return bin_dir
	


def launch_app():
	bin_dir = bin_directory()
	fsg.theme("DarkGrey15")
	main_menu_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Button("Import New PDF", key = "__IMPORT_NEW_PDF_BUTTON__")],
		[fsg.Button("Start New Scenario", key = "__START_NEW_SCENARIO_BUTTON__")]
	]
	
	extract_pdf_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Text("Import PDF", font = ["any", 18], justification = "left")],
		[fsg.In(key = "__PDF_FILE_IMPORT__")],
		[fsg.FileBrowse(target="__PDF_FILE_IMPORT__", file_types = (("PDF Files", "*.pdf"), )), fsg.Button("Import", key = "__IMPORT_SELECTED_PDF__")]
	]

	new_scenario_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)]
	]
	
	main_menu_col = fsg.Column(main_menu_layout, key = "-Main Menu-")
	extract_pdf_col = fsg.Column(extract_pdf_layout, key = "-Extract PDF Menu-", visible = False)
	new_scenario_col = fsg.Column(new_scenario_layout, key = "-New Scenario Menu-", visible = False)
	
	main_layout = [[main_menu_col, extract_pdf_col, new_scenario_col]]
	
	window = fsg.Window("Pathfinder Society Assistant", main_layout, location = (0, 0), size = (500, 250), element_padding = 2, resizable = True)
	
	while True:
		event, values = window.read()
		if event == fsg.WIN_CLOSED or event== "Cancel":
			break
		elif event == "__IMPORT_NEW_PDF_BUTTON__":
			window["-Main Menu-"].update(visible = False)
			window["-Extract PDF Menu-"].update(visible = True)
		elif event == "__IMPORT_SELECTED_PDF__":
			pdf.extract_file(values["__PDF_FILE_IMPORT__"])
			window["-Extract PDF Menu-"].update(visible = False)
			window["-Main Menu-"].update(visible = True)
		elif event == "__START_NEW_SCENARIO_BUTTON__":
			window["-Main Menu-"].update(visible = False)
			window["-New Scenario Menu-"].update(visible = True)
	
	close_window(window)


def close_window(window):
	window.close()
	

if __name__ == "__main__":
	launch_app()
