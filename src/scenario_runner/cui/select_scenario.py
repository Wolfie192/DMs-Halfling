import src.scenario_runner.cui.page_manager as page_manager
from src.console import console
import os


def run(directory):
	available_scenarios: dict = {}
	
	for root, dirs, files in os.walk(directory["selected season"]):
		for dir in dirs:
			if dir == "Images":
				continue
			elif dir[-1] == ")":
				tier_str = dir.split(" ")[-1]
				scenario_num = dir.split(" ")[-2]
				if int(scenario_num) < 10:
					scenario_num = f"0{scenario_num}"
				name_str = f"{scenario_num}-{tier_str.split("-")[0].replace("(", "")}"
				available_scenarios[dir] = {
					"name": name_str,
					"path": os.path.join(root, dir)
				}
			else:
				scenario_num = dir.split(" ")[-1]
				if int(scenario_num) < 10:
					scenario_num = f"0{scenario_num}"
				available_scenarios[dir] = {
					"name": scenario_num,
					"path": os.path.join(root, dir)
				}
	
	available_scenarios = dict(sorted(available_scenarios.items(), key = lambda item: item[1]["name"]))
	
	_display(available_scenarios)
	_main_loop(available_scenarios)


def _display(scenario_list):
	console.clear()
	print("DM's Halfling - Select Scenario\n\n")
	
	for scenario in scenario_list.keys():
		print(scenario_list[scenario]["name"])
	
	print("[B]ack | [Q]uit\n\n")


def _main_loop(available_scenarios):
	while(True):
		user_input = input("> ").lower()
		
		try:
			user_input = int(user_input)
		except ValueError:
			pass
		
		available_scenario_names = []
		
		for key, value in available_scenarios.items():
			available_scenario_names.append(value["name"])
	
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case u if u in available_scenario_names:
				for key,  value in available_scenarios.items():
					if value["name"] == user_input:
						page_manager.run(value["path"])
				_display(available_scenarios)
			case u if isinstance(u, int):
				if user_input < 10:
					user_input = f"0{user_input}"
				for key, value in available_scenarios.items():
					if value["name"] == str(user_input):
						page_manager.run(value["path"])
				_display(available_scenarios)
			case _:
				_display(available_scenarios)
