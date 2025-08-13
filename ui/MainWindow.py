import os
import FreeSimpleGUI as sg
from ui import NewScenarioWindow, PDFImportWindow


def build(directories):
	sg.theme("DarkGrey")
	
	window_layout = [
		[main_menu_column(directories)],
		[sg.Sizer(h_pixels = 300)]
	]
	
	window = sg.Window("DM's Halfling Assistant", window_layout, relative_location = (0, 0), resizable = True, element_padding = 10, margins = (10, 10))
	
	main_loop(window, directories)


def main_loop(window, directories):
	while True:
		event, values = window.read(timeout = 1000)
		if event == sg.WIN_CLOSED:
			break
		elif event == "Import PDFs Button":
			pdf_window = PDFImportWindow.build(directories)
			if not pdf_window.metadata:
				window["Start New Scenario Button"].update(visible = True)
				window.refresh()
			elif pdf_window.metadata == "Win Closed":
				pass
		elif event == "Start New Scenario Button":
			window.close()
			NewScenarioWindow.build(directories)
		elif event == "Continue Scenario Button":
			#TODO Set up ability to continue from a save and set up saving progress to allow for continuing from a crash.
			window.close()
	
	window.close()


def main_menu_column(directories) -> sg.Column:
	new_scenario_button_visible: bool = False
	continue_scenario_button_visible: bool = False
	
	for root, _, files in os.walk(directories["Modules"]):
		for file in files:
			if file.endswith(".txt"):
				new_scenario_button_visible = True
	
	for root, _, files in os.walk(directories["Saves"]):
		for file in files:
			if file.endswith(".json"):
				continue_scenario_button_visible = True
				
	import_pdf_button = sg.Button("Import PDFs", key = "Import PDFs Button", expand_x = True)
	start_new_scenario_button = sg.Button("Start New Scenario", key = "Start New Scenario Button", expand_x = True, visible = new_scenario_button_visible)
	continue_scenario_button = sg.Button("Continue Scenario", key = "Continue Scenario Button", expand_x = True, visible = continue_scenario_button_visible)
	
	layout = [
		[start_new_scenario_button],
		[continue_scenario_button],
		[import_pdf_button]
	]
	
	return sg.Column(layout, key = "Main Menu Column", expand_x = True, expand_y = True)
