import FreeSimpleGUI as sg


def continue_scenario_button_visible() -> bool:
	#TODO 
	return False


def extract_pdf_layout() -> list:
	layout = [
		[sg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[sg.Text("Import PDF", font = ["any", 18])],
		[sg.In(key = "PDF File Path")],
		[sg.FileBrowse(target = "PDF File Path", file_types = (("PDF Files", "*.pdf"), )), sg.Button("Import", key = "Import Selected PDF Button")]		
	]
	
	return layout
	
	
def select_season_layout() -> list:
	layout = [
		[sg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[sg.Text("Select Season", font = ["any", 18])]
	]	
	
	return layout


def select_scenario_layout() -> list:
	layout = [
		[sg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[sg.Text("Select Scenario", font = ["any", 18])],
	]
	
	return layout
