from src.scenario_runner.cui import select_scenario
from src.console import console
import os


def run(directory):
	available_season_list: list[str] = []
	
	for root, dirs, files in os.walk(directory["modules"]):
		for dir in dirs:
			if dir == "Bounties":
				available_season_list += [dir]
			elif dir == "Quests":
				available_season_list += [dir]
			elif dir.startswith("Season"):
				available_season_list += [dir]
		
	_display(available_season_list)
	_main_loop(directory, available_season_list)


def _display(available_season_list: list[str] = None):
	console.clear()
	print("DM's Halfling - Select Season\n\n")
	
	for season in available_season_list:
		if not season.startswith("Season"):
			season = f"[{season[0:2]}]{season[2:]}"
		else:
			season = f"{season[0:-2]} [{season[-1]}]"
		print(season)
	
	print()
	
	print("[B]ack | [Q]uit\n\n")


def _main_loop(directory, available_season_list: list[str] = None):
	while(True):
		user_input = input("> ").lower()
		
		match user_input:
			case "q"|"quit":
				console.clear()
				console.close()
			case "b"|"back":
				break
			case "bo"|"bounties":
				directory["selected season"] = os.path.join(directory["modules"], "Bounties")
				select_scenario.run(directory)
				_display(available_season_list)
			case "qu"|"quests":
				directory["selected season"] = os.path.join(directory["modules"], "Quests")
				select_scenario.run(directory)
				_display(available_season_list)
			case "1"|"season 1":
				directory["selected season"] = os.path.join(directory["modules"], "Season 1")
				select_scenario.run(directory)
				_display(available_season_list)
			case "2"|"season 2":
				directory["selected season"] = os.path.join(directory["modules"], "Season 2")
				select_scenario.run(directory)
				_display(available_season_list)
			case "3"|"season 3":
				directory["selected season"] = os.path.join(directory["modules"], "Season 3")
				select_scenario.run(directory)
				_display(available_season_list)
			case "4"|"season 4":
				directory["selected season"] = os.path.join(directory["modules"], "Season 4")
				select_scenario.run(directory)
				_display(available_season_list)
			case "5"|"season 5":
				directory["selected season"] = os.path.join(directory["modules"], "Season 5")
				select_scenario.run(directory)
				_display(available_season_list)
			case "6"|"season 6":
				directory["selected season"] = os.path.join(directory["modules"], "Season 6")
				select_scenario.run(directory)
				_display(available_season_list)
			case _:
				_display(available_season_list)
