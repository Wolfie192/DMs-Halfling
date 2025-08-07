import os

import FreeSimpleGUI as fsg

import pdf


def run(root_dir):
	fsg.theme("DarkGrey")
	start_scenario_button_visible: bool = False
	continue_scenario_button_visible: bool = False
	import_spacer_line_visible: bool = False
	
	for root, _, files in os.walk(root_dir):
		for file in files:
			if file.endswith(".pdf"):
				file_path = os.path.join(root, file)
				season, scenario = pdf.get_scenario_num(file_path)
				
				if season:
					start_scenario_button_visible = True
	
	#TODO Continue Scenario button visibility
	
	if start_scenario_button_visible or continue_scenario_button_visible:
		import_spacer_line_visible = True
	
	main_menu_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Button("Start New Scenario", key = "Start New Scenario Button", visible = start_scenario_button_visible)],
		[fsg.Button("Continue Scenario", key = "Continue Scenario Button", visible = continue_scenario_button_visible)],
		[fsg.Text("", key = "Import Spacer Line", visible = import_spacer_line_visible)],
		[fsg.Button("Import New PDF", key = "Import New PDF Button")]
	]
	main_menu_column = fsg.Column(main_menu_layout, key = "Main Menu Column")
	
	extract_pdf_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Text("Import PDF", font = ["any", 18])],
		[fsg.In(key = "PDF File Path")],
		[fsg.FileBrowse(target = "PDF File Path", file_types = (("PDF Files", "*.pdf"), )), fsg.Button("Import", key = "Import Selected PDF Button")]
	]
	extract_pdf_column = fsg.Column(extract_pdf_layout, key = "Extract PDF Column", visible = False)
	
	select_season_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Text("Select Season", font = ["any", 18])]
	]
	select_season_column = fsg.Column(select_season_layout, key = "Select Season Column", visible = False)
	
	select_scenario_layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Text("Select Scenario", font = ["any", 18])],
	]
	select_scenario_column = fsg.Column(select_scenario_layout, key = "Select Scenario Column", visible = False)
	
	layout = [
		[main_menu_column, extract_pdf_column, select_season_column, select_scenario_column]
		]
	
	main_window = fsg.Window("Pathfinder Society Assistant", layout, location = (75, 25), size = (800, 600), element_padding = 2, margins = (10, 10), resizable = True)
	
	while True:
		event, values = main_window.read(timeout = 1000)
		
		if event == fsg.WIN_CLOSED or event == "Cancel":
			break
			
		elif event == "Start New Scenario Button":
			main_window["Main Menu Column"].update(visible = False)
			main_window["Select Season Column"].update(visible = True)
			
			season_list = []
			for root, _, files in os.walk(root_dir):
				for file in files:
					file_path = os.path.join(root, file)
					season, scenario = pdf.get_scenario_num(file_path)
					
					if not season in season_list:
						season_list.append(season)
			
			season_list.sort()
			season_list = season_list[1:]
			
			
			for season in season_list:
				main_window.extend_layout(main_window["Select Season Column"], [[fsg.Button(f"Season {season}", key = f"Season Selected Button {season}")]])
				main_window.refresh()
			
		elif event == "Continue Scenario Button":
			#TODO
			pass
		
		elif event == "Import New PDF Button":
			main_window["Main Menu Column"].update(visible = False)
			main_window["Extract PDF Column"].update(visible = True)
			
		elif event == "Import Selected PDF Button":
			main_window["Extract PDF Column"].update(visible = False)
			main_window["Main Menu Column"].update(visible = True)
			added_pdf = pdf.extract_file(root_dir, values["PDF File Path"])
			
			if added_pdf or start_scenario_button_visible:
				start_scenario_button_visible = True
				import_spacer_line_visible = True
			
			main_window["Start New Scenario Button"].update(visible = start_scenario_button_visible)
			main_window["Import Spacer Line"].update(visible = import_spacer_line_visible)
			
			main_window.refresh()
		
		elif event.startswith("Season Selected Button"):
			idx = str(event.split(" ")[-1])
			main_window["Select Season Column"].update(visible = False)
			main_window["Select Scenario Column"].update(visible = True)
			
			scenario_list: list = []
			for root, _, files in os.walk(root_dir):
				for file in files:
					file_path = os.path.join(root, file)
					season, scenario = pdf.get_scenario_num(file_path)
					if season == idx:
						scenario_list.append(scenario)
			
			scenario_list.sort()
			
			for scenario in scenario_list:
				main_window.extend_layout(main_window["Select Scenario Column"], [[fsg.Button(f"Scenario {scenario}", key = f"Scenario Selected Button {scenario}", metadata = idx)]])
				main_window.refresh()			
		
		elif event.startswith("Scenario Selected Button"):
			scenario = str(event.split(" ")[-1])
			season = main_window[f"Scenario Selected Button {scenario}"].metadata
			print(season, scenario)
	
	main_window.close()
