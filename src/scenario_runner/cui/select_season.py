from src.scenario_runner.cui import select_scenario
from src.console import console
import os
from src.configs.directory import DIRECTORY


def available_season_list() -> list:
	season_list: list = []
	
	for root, folders, files in os.walk(DIRECTORY["modules"]):
		for folder in folders:
			if folder == "Bounties":
				season_list += [folder]
			elif folder == "Quests":
				season_list += [folder]
			elif folder.startswith("Season"):
				season_list += [folder]
	
	return season_list


def run():
	_display()
	_main_loop()


def _display():
	console.clear()
	print("DM's Halfling - Select Season\n\n")
	
	for season in available_season_list():
		if not season.startswith("Season"):
			season = f"[{season[0:2]}]{season[2:]}"
		else:
			season = f"{season[0:-2]} [{season[-1]}]"
		print(season)
	
	print()
	
	print("[B]ack | [Q]uit\n\n")


def _main_loop():
	while True:
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case "bo"|"bounties":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Bounties")
				select_scenario.run()
				_display()
			case "qu"|"quests":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Quests")
				select_scenario.run()
				_display()
			case "1"|"season 1":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 1")
				select_scenario.run()
				_display()
			case "2"|"season 2":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 2")
				select_scenario.run()
				_display()
			case "3"|"season 3":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 3")
				select_scenario.run()
				_display()
			case "4"|"season 4":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 4")
				select_scenario.run()
				_display()
			case "5"|"season 5":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 5")
				select_scenario.run()
				_display()
			case "6"|"season 6":
				DIRECTORY["selected season"] = os.path.join(DIRECTORY["modules"], "Season 6")
				select_scenario.run()
				_display()
			case _:
				_display()
