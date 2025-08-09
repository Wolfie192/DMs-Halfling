import os

import FreeSimpleGUI as fsg

import pdf


class MainWindow:
	def __init__(self, bin_dir):
		fsg.theme("DarkGrey")
		self.root_dir = bin_dir
		self.location = (75, 25)
		self.size = (800, 600)
		self.window = None
		
		self.season: str = None
		self.scenario: str = None
		self.continue_scenario: bool = False
	
	def start_scenario_button_visible(self) -> bool:
		start_scenario_button_visible: bool = False
		for root, _, files in os.walk(self.root_dir):
			for file in files:
				if file.endswith(".pdf"):
					file_path = os.path.join(root, file)
					season, scenario = pdf.get_scenario_num(file_path)
					
					if season:
						start_scenario_button_visible = True	
		
		return start_scenario_button_visible
	
	def continue_scenario_button_visible(self) -> bool:
		#TODO 
		return False

	def import_spacer_line_visible(self) -> bool:
		import_spacer_line_visible: bool = False
		
		if self.start_scenario_button_visible() or self.continue_scenario_button_visible():
			import_spacer_line_visible = True
		
		return import_spacer_line_visible
	
	def main_menu_layout(self) -> list:
		layout = [
		[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
		[fsg.Button("Start New Scenario", key = "Start New Scenario Button", visible = self.start_scenario_button_visible())],
		[fsg.Button("Continue Scenario", key = "Continue Scenario Button", visible = self.continue_scenario_button_visible())],
		[fsg.Text("", key = "Import Spacer Line", visible = self.import_spacer_line_visible())],
		[fsg.Button("Import New PDF", key = "Import New PDF Button")]
		]
		
		return layout
	
	def extract_pdf_layout(self) -> list:
		layout = [
			[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
			[fsg.Text("Import PDF", font = ["any", 18])],
			[fsg.In(key = "PDF File Path")],
			[fsg.FileBrowse(target = "PDF File Path", file_types = (("PDF Files", "*.pdf"), )), fsg.Button("Import", key = "Import Selected PDF Button")]		
		]
		
		return layout
	
	def select_season_layout(self) -> list:
		layout = [
			[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
			[fsg.Text("Select Season", font = ["any", 18])]
		]	
		
		return layout
	
	def select_scenario_layout(self) -> list:
		layout = [
			[fsg.Text("Pathfinder Society Assistant", font = ["any", 28], justification = "center", expand_x = True)],
			[fsg.Text("Select Scenario", font = ["any", 18])],
		]
		
		return layout
	
	def build(self):
		main_menu_column = fsg.Column(self.main_menu_layout(), key = "Main Menu Column")
		extract_pdf_column = fsg.Column(self.extract_pdf_layout(), key = "Extract PDF Column", visible = False)
		select_season_column = fsg.Column(self.select_season_layout(), key = "Select Season Column", visible = False)
		select_scenario_column = fsg.Column(self.select_scenario_layout(), key = "Select Scenario Column", visible = False)
		
		layout = [
			[main_menu_column, extract_pdf_column, select_season_column, select_scenario_column]
		]
	
		self.window = fsg.Window("Pathfinder Society Assistant", layout, location = self.location, size = self.size, element_padding = 2, margins = (10, 10), resizable = True)
		
		self.main_loop()
	
	def update_select_season_column(self):
		season_list = []
		for root, _, files in os.walk(self.root_dir):
			for file in files:
				file_path = os.path.join(root, file)
				season, scenario = pdf.get_scenario_num(file_path)
				
				if not season in season_list:
					season_list.append(season)
		
		season_list.sort()
		season_list = season_list[1:]
		
		
		for season in season_list:
			self.window.extend_layout(self.window["Select Season Column"], [[fsg.Button(f"Season {season}", key = f"Season Selected Button {season}")]])
			self.window.refresh()
	
	def update_select_scenario_column(self, idx):
		scenario_list: list = []
		for root, _, files in os.walk(self.root_dir):
			for file in files:
				file_path = os.path.join(root, file)
				season, scenario = pdf.get_scenario_num(file_path)
				if season == idx:
					scenario_list.append(scenario)
		
		scenario_list.sort()
		
		for scenario in scenario_list:
			self.window.extend_layout(self.window["Select Scenario Column"], [[fsg.Button(f"Scenario {scenario}", key = f"Scenario Selected Button {scenario}", metadata = idx)]])
			
		self.window.refresh()				
	
	def close(self):
		self.window.close()
	
	def main_loop(self):
		while True:
			event, values = self.window.read(timeout = 1000)
			
			# Event for closing the window
			if event == fsg.WIN_CLOSED or event == "Cancel":
				break
				
			elif event == "Start New Scenario Button":
				self.window["Main Menu Column"].update(visible = False)
				self.window["Select Season Column"].update(visible = True)
				self.update_select_season_column()
				
			elif event == "Continue Scenario Button":
				#TODO
				self.continue_scenario = True
				pass
			
			elif event == "Import New PDF Button":
				self.window["Main Menu Column"].update(visible = False)
				self.window["Extract PDF Column"].update(visible = True)
				
			elif event == "Import Selected PDF Button":
				self.window["Extract PDF Column"].update(visible = False)
				self.window["Main Menu Column"].update(visible = True)
				
				pdf.extract_file(self.root_dir, values["PDF File Path"])
			
				self.window["Start New Scenario Button"].update(visible = self.start_scenario_button_visible())
				self.window["Import Spacer Line"].update(visible = self.import_spacer_line_visible())
				
				self.window.refresh()
			
			elif event.startswith("Season Selected Button"):
				idx = str(event.split(" ")[-1])
				self.window["Select Season Column"].update(visible = False)
				self.window["Select Scenario Column"].update(visible = True)
				
				self.update_select_scenario_column(idx)
			
			elif event.startswith("Scenario Selected Button"):
				self.scenario = str(event.split(" ")[-1])
				self.season = self.window[f"Scenario Selected Button {self.scenario}"].metadata
				break
		self.close()
	
