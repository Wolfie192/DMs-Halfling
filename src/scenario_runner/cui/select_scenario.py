from src.console import console
import os
from src.configs.directory import DIRECTORY


def available_scenarios() -> dict:
	scenarios: dict = {}
	
	for root, folders, files in os.walk(DIRECTORY["selected season"]):
		for folder in folders:
			if folder == "Images":
				continue
			elif folder[-1] == ")":
				tier_str = folder.split(" ")[-1]
				scenario_num = folder.split(" ")[-2]
				if int(scenario_num) < 10:
					scenario_num = f"0{scenario_num}"
				name_str = f"{scenario_num}-{tier_str.split("-")[0].replace("(", "")}"
				scenarios[folder] = {
					"name": name_str,
					"path": os.path.join(root, folder)
				}
			else:
				scenario_num = folder.split(" ")[-1]
				if int(scenario_num) < 10:
					scenario_num = f"0{scenario_num}"
				scenarios[folder] = {
					"name": scenario_num,
					"path": os.path.join(root, folder)
				}
	
	scenarios = dict(sorted(scenarios.items(), key = lambda item: item[1]["name"]))
	
	return scenarios


def run():
	_display()
	_main_loop()


def _display():
	console.clear()
	scenario_dict: dict = available_scenarios()
	print("DM's Halfling - Select Scenario\n\n")
	
	for scenario in scenario_dict.keys():
		print(scenario_dict[scenario]["name"])
	
	print("[B]ack | [Q]uit\n\n")


def _main_loop():
	scenario_dict: dict = available_scenarios()
	
	while True:
		user_input = input("> ").lower()
		
		try:
			user_input = int(user_input)
		except ValueError:
			pass
		
		available_scenario_names = []
		
		for key, value in scenario_dict.items():
			available_scenario_names.append(value["name"])
	
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case _:
				_display()
