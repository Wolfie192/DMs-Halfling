import os
import FreeSimpleGUI as sg

import tools.ModuleManager as mm


def get_scenarios_data(directories) -> dict:
	available_scenarios: dict = {
		"Bounties": {
			"Available": False,
			"Scenarios": []
		},
		"Quests": {
			"Available": False,
			"Scenarios": []
		},
		"Season 1": {
			"Available": False,
			"Scenarios": []
		},
		"Season 2": {
			"Available": False,
			"Scenarios": []
		},
		"Season 3": {
			"Available": False,
			"Scenarios": []
		},
		"Season 4": {
			"Available": False,
			"Scenarios": []
		},
		"Season 5": {
			"Available": False,
			"Scenarios": []
		},
		"Season 6": {
			"Available": False,
			"Scenarios": []
		},
		"Season 7": {
			"Available": False,
			"Scenarios": []
		}
	}
	
	for root, _, files in os.walk(directories["Modules"]):
		for file in files:
			if file.endswith(".txt"):
				file_path = os.path.join(root, file)
				dir_name: str = os.path.splitext(file_path)[0].split("\\")[-3]
				file_name: str = os.path.splitext(file_path)[0].split("\\")[-2]
				available_scenarios[dir_name]["Available"] = True
				available_scenarios[dir_name]["Scenarios"].append(file_name.split(" ")[-1])
	
	return available_scenarios

				
def build(directories):
	available_scenarios = get_scenarios_data(directories)
	sg.theme("DarkGrey")
	
	window_layout = [
		[select_season_column(available_scenarios), select_scenario_column()]
	]
	
	window = sg.Window("New Scenario", window_layout, relative_location = (0, 0), resizable = True, element_padding = 10, margins = (10, 10))
	
	main_loop(window, available_scenarios, directories)


def main_loop(window, available_scenarios, directories):
	while True:
		event, values = window.read(timeout = 1000)
		if event == sg.WIN_CLOSED:
			break
		elif event.endswith("Season Button"):
			selected_season = None
			match event:
				case "Bounties Season Button":
					selected_season = "Bounties"
				case "Quests Season Button":
					selected_season = "Quests"
				case "Season 1 Season Button":
					selected_season = "Season 1"
				case "Season 2 Season Button":
					selected_season = "Season 2"
				case "Season 3 Season Button":
					selected_season = "Season 3"
				case "Season 4 Season Button":
					selected_season = "Season 4"
				case "Season 5 Season Button":
					selected_season = "Season 5"
				case "Season 6 Season Button":
					selected_season = "Season 6"
				case "Season 7 Season Button":
					selected_season = "Season 7"
			window["Select Season Column"].update(visible = False)
			update_scenario_column(selected_season, window, available_scenarios)
			window["Select Scenario Column"].update(visible = True)
			window.refresh()
		elif event.endswith("Scenario Button"):
			selected_scenario = event.split(" ")[0]
			break
			
	mm.setup_module(selected_season, selected_scenario, directories)
	window.close()
			
				

	window.close()

def select_season_column(available_scenarios) -> sg.Column:
	layout = []
	
	for key, _ in available_scenarios.items():
		if available_scenarios[key]["Available"]:
			button = sg.Button(f"{key}", key = f"{key} Season Button", expand_x = True, expand_y = True)
			layout.append([button])
	
	layout.append([sg.Sizer(h_pixels = 300)])
	
	frame = sg.Frame("Select Season", layout, expand_x = True, expand_y = True)
	
	column_layout = [
		[frame]
	]

	return sg.Column(column_layout, key = "Select Season Column", expand_x = True, expand_y = True)


def select_scenario_column() -> sg.Column:
	layout = []
	
	return sg.Column(layout, key = "Select Scenario Column", expand_x = True, expand_y = True, visible = False)


def update_scenario_column(selected_season, window, available_scenarios):
	button_list = []
	available_scenarios[selected_season]["Scenarios"].sort(key = int)
	for item in available_scenarios[selected_season]["Scenarios"]:
		button = sg.Button(f"{item}", key = f"{item} Scenario Button", expand_x = True, expand_y = True)
		button_list.append(button)
	
	i = 0
	while i < len(button_list):
		if i + 2 > len(button_list):
			window.extend_layout(window["Select Scenario Column"], [[button_list[i]]])
		else:
			window.extend_layout(window["Select Scenario Column"], [[button_list[i], button_list[i + 1]]])
		i += 2
	
	window.extend_layout(window["Select Scenario Column"], [[sg.Sizer(h_pixels = 300)]])


if __name__ == "__main__":
	bin_dir = os.path.abspath("../bin")
	module_dir = os.path.join(bin_dir, "Modules")
	
	get_scenarios_data({"Modules": module_dir})
